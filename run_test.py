from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scraper import (
    scrape_first_five_articles,   # ← updated function name
    translate_titles_google,
    analyze_repeated_words
)
import re


def get_driver():
    """Create local Chrome driver"""
    options = webdriver.ChromeOptions() #create chrome configuration object
    options.add_argument("--start-maximized")
    options.add_argument("--lang=es")
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': 'es,es-ES'}
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), #launches chrome 
        options=options #OUR CONFIGURED OPTIONS
    )
    return driver


def handle_cookies(driver, wait):
    """Handle cookie popup (desktop + mobile selectors)"""
    try:
        btn = wait.until(
            EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button"))
        )
        btn.click()
        print("Cookies accepted (desktop)")
    except:
        try:
            btn = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button[data-accept-action='true']")
                )
            )
            btn.click()
            print(" Cookies accepted (mobile)")
        except:
            print(" No cookie popup found")


if __name__ == "__main__":
    driver = None

    try:
        print("="*80)
        print("EL PAÍS OPINION SCRAPER - LOCAL RUN")
        print("="*80)

        driver = get_driver()
        wait = WebDriverWait(driver, 15)

        # Open El País
        print("\n Opening El País homepage...")
        driver.get("https://elpais.com/")
        handle_cookies(driver, wait)

        # Validate Spanish language

        body_text = driver.find_element(By.TAG_NAME, "body").text
        assert re.search(r'[ñÑáéíóúÁÉÍÓÚüÜ]', body_text), "Website not in Spanish"
        print(" Spanish language verified")

        # Navigate to Opinion section (stable navigation)
        print("\n Opening Opinion section...")
        driver.get("https://elpais.com/opinion/")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2.c_t a")))
        print(" Opinion section loaded")

        # Scrape articles (new scraper logic)
        articles = scrape_first_five_articles(driver)

        # Translate titles
        print("\n Translating titles...")
        titles_list = [article['title'] for article in articles]
        translated_titles = translate_titles_google(titles_list)

        for idx, article in enumerate(articles):
            article['translated_title'] = translated_titles[idx]
            print(f"\n{idx+1}. Spanish: {article['title']}")
            print(f"   English: {translated_titles[idx]}")

        # Analyze repeated words
        analyze_repeated_words(articles)

        print("\n Local execution completed successfully!")
        print("="*80)

    except Exception as e:
        print(f"\n Error: {str(e)}")
        import traceback
        traceback.print_exc()

    finally:
        if driver:
            driver.quit()
            print("\n Browser closed")

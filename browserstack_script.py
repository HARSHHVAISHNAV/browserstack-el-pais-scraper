import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scraper import (
    scrape_first_five_articles,
    translate_titles_google,
    analyze_repeated_words
)
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions

load_dotenv()

USERNAME = os.environ.get('BROWSERSTACK_USERNAME')
ACCESS_KEY = os.environ.get('BROWSERSTACK_ACCESS_KEY')


BROWSER_CONFIGS = [
    {
        'name': 'Chrome on Windows 10',
        'os': 'Windows',
        'os_version': '10',
        'browser': 'Chrome',
        'browser_version': 'latest',
    },
    {
        'name': 'Firefox on macOS Monterey',
        'os': 'OS X',
        'os_version': 'Monterey',
        'browser': 'Firefox',
        'browser_version': 'latest',
    },
    {
        'name': 'Safari on macOS Ventura',
        'os': 'OS X',
        'os_version': 'Ventura',
        'browser': 'Safari',
        'browser_version': 'latest',
    },
    {
        'name': 'Chrome on Samsung Galaxy S21',
        'device': 'Samsung Galaxy S21',
        'os_version': '11.0',
        'browser': 'chrome',
    },
    {
        'name': 'Safari on iPhone 13',
        'device': 'iPhone 13',
        'os_version': '15',
        'browser': 'safari',
    }
]


def is_mobile(config):
    return 'device' in config


def create_browserstack_driver(config):
    
    browser = config.get('browser', 'chrome').lower()

    if browser == 'chrome':
        options = ChromeOptions()
    elif browser == 'firefox':
        options = FirefoxOptions()
    else:
        options = SafariOptions()

    bstack_options = {
        'userName': USERNAME,
        'accessKey': ACCESS_KEY,
        'buildName': 'ElPais Scraper Final',
        'sessionName': f'El País Test - {config["name"]}',
    }

    if is_mobile(config):
        bstack_options['deviceName'] = config['device']
        bstack_options['realMobile'] = 'true'
        bstack_options['osVersion'] = config['os_version']
    else:
        bstack_options['os'] = config['os']
        bstack_options['osVersion'] = config['os_version']
        bstack_options['browserVersion'] = config['browser_version']

    options.set_capability('bstack:options', bstack_options)

    return webdriver.Remote(
        command_executor="https://hub-cloud.browserstack.com/wd/hub",
        options=options
    )


def handle_cookies(driver, wait):
    try:
        btn = wait.until(EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button")))
        btn.click()
        print(" Cookies accepted")
    except:
        try:
            btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-accept-action='true']")))
            btn.click()
            print("Cookies accepted (mobile)")
        except:
            print(" No cookie popup")


def go_to_opinion_section(driver, wait, config):
    try:
        if is_mobile(config):
            print("Mobile navigation (direct URL)")
            
            # Mobile browsers often fail to open hamburger menus reliably.
            # Direct navigation is the stable automation strategy.
            driver.get("https://elpais.com/opinion/")
            
        else:
            print(" Desktop navigation")
            opinion = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(@href,'/opinion')]")
                )
            )
            driver.execute_script("arguments[0].click();", opinion)

        # Wait until article list loads
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2.c_t a")))
        print(" Opinion section loaded")

    except Exception:
        raise Exception("Failed navigating to Opinion section")

def run_test_on_browser(config):
    browser_name = config['name']
    driver = None

    try:
        print(f"\n🚀 Running: {browser_name}")

        driver = create_browserstack_driver(config)
        wait = WebDriverWait(driver, 20)

        driver.get("https://elpais.com/")
        handle_cookies(driver, wait)

        go_to_opinion_section(driver, wait, config)

        articles = scrape_first_five_articles(driver)

        titles = [a['title'] for a in articles]
        translated = translate_titles_google(titles)

        for i in range(len(articles)):
            articles[i]['translated_title'] = translated[i]

        analyze_repeated_words(articles)

        return f"✅ {browser_name} - SUCCESS"

    except Exception as e:
        return f"❌ {browser_name} - FAILED: {str(e)[:80]}"

    finally:
        if driver:
            driver.quit()


def run_parallel_tests():
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(run_test_on_browser, c) for c in BROWSER_CONFIGS]

        for future in as_completed(futures):
            print(future.result())


if __name__ == "__main__":
    run_parallel_tests()
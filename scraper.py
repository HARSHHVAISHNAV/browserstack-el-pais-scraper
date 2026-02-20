import os
import re #remove punctuations
import requests #used to download images from URLs
import time 
from collections import Counter
from selenium.webdriver.common.by import By # to locate elements like button on the webpage by ID, CSS selector, tag name
from selenium.webdriver.support.ui import WebDriverWait #smart wait 
from selenium.webdriver.support import expected_conditions as EC #wait conditions
from deep_translator import GoogleTranslator

def scrape_first_five_articles(driver):
    wait = WebDriverWait(driver, 15)
    articles_data = []
    os.makedirs("article_images", exist_ok=True)

    print("Fetching article URLs...")

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    article_links = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2.c_t a"))
    )

    urls = [link.get_attribute("href") for link in article_links[:5]]
    print(f"Found {len(urls)} articles")

    for idx, url in enumerate(urls, 1):
        print(f"\nOpening article {idx}")
        driver.get(url)
        time.sleep(3)

        try:
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

            title = driver.find_element(By.TAG_NAME, "h1").text.strip()

            image_path = None
            try:
                img = driver.find_element(By.CSS_SELECTOR, "article img")
                img_url = img.get_attribute("src")
                if img_url.startswith("http"):
                    image_path = download_image(img_url, idx)
            except:
                pass

            articles_data.append({
                "title": title,
                "image_path": image_path
            })

        except Exception as e:
            print("Error:", e)

        driver.back()
        time.sleep(2)

    return articles_data


def download_image(url, article_num):
    try:
        r = requests.get(url, timeout=10)
        filename = f"article_images/article_{article_num}.jpg"
        with open(filename, 'wb') as f:
            f.write(r.content)
        return filename
    except:
        return None


def translate_titles_google(titles):
    translator = GoogleTranslator(source='es', target='en')
    return [translator.translate(t) for t in titles]


def analyze_repeated_words(articles_data):
    all_titles = " ".join([a['translated_title'] for a in articles_data])
    words = re.findall(r'\b[a-zA-Z0-9]+\b', all_titles.lower())
    counts = Counter(words)

    print("\nRepeated Words:")
    for word, count in counts.items():
        if count >= 2:
            print(word, "=", count)

# only for better local testing
def scrape_first_five_articles_new_tabs(driver):
    """
    LOCAL RUN VERSION
    Opens each article in a new tab (for better viewing locally)
    BrowserStack version uses same-tab navigation.
    """
    wait = WebDriverWait(driver, 15)
    articles_data = []
    os.makedirs("article_images", exist_ok=True)

    print("Fetching article URLs...")

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)   


    # Extract URLs using JavaScript (prevents stale element error)
    urls = driver.execute_script("""
        let links = document.querySelectorAll('h2.c_t a');
        let results = [];
        for (let i = 0; i < Math.min(5, links.length); i++) {
            results.push(links[i].href);
        }
        return results;
    """)

    print(f"Found {len(urls)} articles")

    parent_window = driver.current_window_handle

    for idx, url in enumerate(urls, 1):
        print(f"\nOpening article {idx} in new tab")

        # Open new tab
        driver.execute_script(f"window.open('{url}', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])

        try:
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

            title = driver.find_element(By.TAG_NAME, "h1").text.strip()

            image_path = None
            try:
                img = driver.find_element(By.CSS_SELECTOR, "article img")
                img_url = img.get_attribute("src")
                if img_url.startswith("http"):
                    image_path = download_image(img_url, idx)
            except:
                pass

            articles_data.append({
                "title": title,
                "image_path": image_path
            })

        except Exception as e:
            print("Error:", e)

    # Switch back to main tab
    driver.switch_to.window(parent_window)

    return articles_data
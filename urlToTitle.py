import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=3)  # Run 3 parallel Selenium instances

def get_title_from_url(url):
    """Fetches title and description from a webpage with optimized speed."""
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    chromedriver_path = os.path.join(script_dir, 'chromedriver.exe')

    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    title, description = "No title available.", "No description available."

    try:
        driver.get(url)
        WebDriverWait(driver, 5).until(lambda d: d.title.strip() != "")
        title = driver.title.strip()

        try:
            description_meta = driver.find_element(By.CSS_SELECTOR, "meta[name='description']")
            description = description_meta.get_attribute("content").strip()
        except:
            paragraphs = driver.find_elements(By.TAG_NAME, "p")
            if paragraphs:
                description = " ".join([p.text.strip() for p in paragraphs[:2] if p.text.strip()])

    except Exception as e:
        print(f"Error fetching {url}: {e}")

    finally:
        driver.quit()

    return title, description

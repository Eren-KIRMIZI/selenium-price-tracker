from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def create_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )


def scrape_book(driver, product):
    driver.get(product["url"])
    time.sleep(2)

    name = driver.find_element(By.CSS_SELECTOR, "div.product_main h1").text
    price_text = driver.find_element(By.CSS_SELECTOR, "p.price_color").text

    price = float(
        price_text.replace("£", "").strip()
    )

    return {
        "site": product["site"],
        "name": name,
        "price": price
    }

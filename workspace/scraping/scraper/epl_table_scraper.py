from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import pandas as pd

class WebScraper:
    def __init__(self, url):
        """
        Initialize the WebScraper with url
        """
        self.url = url

        # default to headless chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--disable-gpu")  # Disable GPU (optional, improves performance on some systems)
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model (useful on servers)
        
        self.driver = webdriver.Chrome(options=chrome_options)

    def load_page(self):
        """
        Load page (Understat recommended)
        """
        self.driver.get(self.url)

    def click_element(self, element_id, timeout=10):
        """
        Make a selection from the table by clicking an element
        """
        try:
            print("scraper is locating element...")
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
            print("element located: ", element)
            print("element html: ", element.get_attribute('outerHTML'))
        except Exception as e:
            print(f"error clicking element {element_id}: {e}")
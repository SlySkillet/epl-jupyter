from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import pandas as pd

class UnderstatScraper:
    def __init__(self, url="https://understat.com/league/EPL"):
        """
        Initialize the WebScraper with url
        """
        self.url = url

        # default to headless chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode

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
            print("scraper is locating element... check")
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
            print("element located: ", element)
            print("element html: ", element.get_attribute('outerHTML'))

            # click element
            self.driver.execute_script("arguments[0].click();", element)
            print("clicked the button")
        except Exception as e:
            print(f"error clicking element {element_id}: {e}")
            self.driver.quit()
            exit()

        # NOTE: CHECK IF THE FOLLOWING BLOCK IS NECESSARY
        try:
            print("checking table update...")
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, "league-chemp")) # id of the table div
            )
            print("confirmed table updated successfully")
        except Exception as e:
            print(f"error waiting for table update: {e}")
            self.driver.quit()
            exit()

    def scrape_table(self, table_id="league-chemp"):
        try:
            html = self.driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            div = soup.find("div", {
                "id": table_id
            })
            if div:
                table = div.find("table")
                if table:
                    print("found table")
                    rows = table.find_all("tr")
                    data = []
                    for row in rows:
                        cells = row.find_all("td")
                        if len(cells) == 0:
                            cells = row.find_all("th")
                        data.append([cell.get_text(strip=True) for cell in cells])
                    if data:
                        df = pd.DataFrame(data[1:], columns=data[0])
                        return df
                    else:
                        print("no data")
                else:
                    print("table not found")
            else:
                print("div not found")
        except Exception as e:
            print(f"Error scraping table: {e}")
    def close(self):
        print("closing driver...")
        self.driver.quit()
        print("driver closed")

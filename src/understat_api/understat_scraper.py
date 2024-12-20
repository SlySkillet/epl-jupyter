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

    def retrieve_raw_data(self, side):
        """
        This method takes in home or away side and runs the full UnderstatScraper
        """
        # validate input
        valid_sides = {'home', 'away'}
        if side not in valid_sides:
            raise ValueError(f"Invalid value for 'side'. Expected one of {valid_sides}, received {side}")
        print(f"Retrieving raw data from Understat.com EPL {side} table")

    def close(self):
        print("closing driver...")
        self.driver.quit()
        print("driver closed")

class UnderstatScraperOrchestrator:
    def __init__(self, league='EPL'):
        """
        This should eventually initialize with logic to determine the league in question and pass the correct url to
        UnderstatScraper
        """
        self.league = league

    def scrape_side(self, side):
        """
        This method takes in home or away side and runs the full UnderstatScraper
        """
        # validate input
        valid_sides = {'home', 'away'}
        if side not in valid_sides:
            raise ValueError(f"Invalid value for 'side'. Expected one of {valid_sides}, received '{side}'")
        print(f"Retrieving raw data from Understat.com EPL {side} table")

        # directory to translate side into the correct id
        id_directory = {
            'home': 'home-away2',
            'away': 'home-away3'
        }

        # run scraper
        try:
            scraper = UnderstatScraper()
            scraper.load_page()
            scraper.click_element(id_directory[side])
            raw_data = scraper.scrape_table()
            return raw_data
        finally:
            scraper.close()

    def scrape_side_to_csv(self, side):
        """
        Runs scraper and writes it to a csv in ../data/raw
        """
        raw_data = self.scrape_side(side)
        file_path = f"../data/raw/{side}_table_raw.csv"

        print(f"writing data to {file_path}")

        raw_data.to_csv(file_path, index=False)

        print("Finished")

    def scrape_all_to_csv(self):
        """
        Scrape both home and away to their respective raw csv files. Most analysis in this project will require
        this. It's in one method here for convenience.
        """
        self.scrape_side_to_csv(side='home')
        self.scrape_side_to_csv(side='away')

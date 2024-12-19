import requests
from datetime import datetime
import os
import json

class OddsFetcher:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def fetch_odds(self, matchday, bookmakers="mybookieag", regions="us", markets="h2h,totals"):
        params = {
            "apiKey": self.api_key,
            "regions": regions,
            "markets": markets,
            "oddsFormat": "decimal",
            "dateFormat": "iso",
            "commenceTimeFrom": f"{matchday}T00:00:00Z",
            "commenceTimeTo": f"{matchday}T23:59:59Z",
            "bookmakers": bookmakers
        }

        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            print(f"successfully retrieved {bookmakers} odds for {matchday}")
            return data
        else:
            print(f"Error: {response.status_code}, {response.text}")

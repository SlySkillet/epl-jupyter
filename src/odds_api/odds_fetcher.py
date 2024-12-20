import requests
from datetime import datetime
import os
import json

class OddsFetcher:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

        self.api_usage = None

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
            # save api_usage to OddsFetcher object for reference
            requests_used = response.headers['X-Requests-Used']
            requests_remaining = response.headers['X-Requests-Remaining']
            self.api_usage = {
                'requests_used': requests_used,
                'requests_remaining': requests_remaining
            }

            print(f"successfully retrieved {bookmakers} odds for {matchday}")
            data = response.json()
            return data
        else:
            print(f"Error: {response.status_code}, {response.text}")

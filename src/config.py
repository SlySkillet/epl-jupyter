from dotenv import load_dotenv
import os

load_dotenv()

ODDS_API_KEY = os.getenv("ODDS_API_API_KEY")
BASE_URL = "https://api.the-odds-api.com/v4/sports/soccer_epl/odds"

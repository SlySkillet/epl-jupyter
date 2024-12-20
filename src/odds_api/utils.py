import pandas as pd

def parse_odds_data(data):
    """
    Processes JSON data from the OddsApi, converts it into a DataFrame, and saves it to a CSV file.
    This function must be run from the root directory of the notebooks or the root of the outputs directory,
    as the file path for saving the DataFrame is specified relative to '../data'.

    Args:
        data (dict): JSON response from `OddsFetcher.fetch_odds`.
    """

    def find_matchday(date_string):
        """Helper function to break out date from datetime string"""
        return date_string.split('T')[0]

    odds_list = []

    matchday = find_matchday(data[0]["commence_time"])

    for match in data:
        # confirm data input is all from the same matchday
        if find_matchday(match["commence_time"]) != matchday:
            raise ValueError("Check data input, all matches must be from the same matchday")

        # create a string representing the matchup
        home_team, away_team = match["home_team"], match["away_team"]
        matchup = f"{home_team} v. {away_team}"

        # create a match_odds dictionary
        match_odds = {
            "match": matchup,
            "1": None,
            "x": None,
            "2": None,
            "ovr_und_point": None,
            "over": None,
            "under": None,
        }

        # retrieve h2h market from mybookie
        h2h_market = match["bookmakers"][0]["markets"][0]["outcomes"]

        # translate h2h market to match_odds dictionary format
        for outcome in h2h_market:
            if outcome["name"] == home_team:
                match_odds["1"] = outcome["price"]
            elif outcome["name"] == away_team:
                match_odds["2"] = outcome["price"]
            elif outcome["name"] == "Draw":
                match_odds["x"] = outcome["price"]

        # retrieve totals market from mybookie
        totals_market = match["bookmakers"][0]["markets"][1]["outcomes"]

        # translate totals market to match_odds dictionary format
        match_odds["ovr_und_point"] = totals_market[0]["point"]

        for outcome in totals_market:
            if outcome['name'] == "Over":
                match_odds["over"] = outcome["price"]
            elif outcome["name"] == "Under":
                match_odds["under"] = outcome["price"]

        # append to odds_list for conversion to DataFrame
        odds_list.append(match_odds)

    odds_df = pd.DataFrame(odds_list)
    print(odds_df)
    odds_df.to_csv(f"../data/processed/odds/odds_matchday_{matchday}.csv", index=False)
    print(f"Data saved to '/data/processed/odds/odds_matchday_{matchday}.csv'")

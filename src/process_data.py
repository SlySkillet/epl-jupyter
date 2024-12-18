import pandas as pd

class ProcessData:
    def __init__(self, home_table_raw_path=None, away_table_raw_path=None):
        """
        Initializes the ProcessData object by preparing home and away data tables for analysis

        Args:
            home_table_raw_path (str, optional): File path to the raw CSV containing home team data.
            away_table_raw_path (str, optional): File path to the raw CSV containing away team data.

        """
        self.home_table_raw_path = home_table_raw_path
        self.away_table_raw_path = away_table_raw_path

        self.home_df = None
        self.away_df = None

        # load and clean data
        self.home_df = self._load_and_clean_data(self.home_table_raw_path)
        self.away_df = self._load_and_clean_data(self.away_table_raw_path)

        # calucluate gpm_scored
        self._calculate_gpm(self.home_df)
        self._calculate_gpm(self.away_df)


    def _load_and_clean_data(self, file_path):
        """
        Loads and cleans data from csv

        Args:
            file_path (str): File path to raw csv
        """
        columns_to_drop = [
            'W',
            'D',
            'L',
            'PTS',
            'xG',
            'xGA',
            'xPTS',
        ]

        # read csv and save to dataframe
        df = pd.read_csv(file_path)

        # drop unneeded columns
        df_clean = df.drop(columns=columns_to_drop)

        return df_clean

    def _calculate_gpm(self, input_df):
        """
        Calculate goals per match scored and conceded and saves to a new column
        Args:
            input_df (pandas.DataFrame): a DataFrame containing cleaned home or away table
        """
        input_df["gpm_scored"] = input_df["G"] / input_df["M"]
        input_df["gpm_conceded"] = input_df["GA"] / input_df["M"]


    def save_to_csv(self, directory_path):
        """
        Saves to csv at the specified path
        Args:
            directory_path (str): path to save file
        """
        path = directory_path if directory_path[-1] == '/' else directory_path + '/'

        self.home_df.to_csv(f"{path}home_table.csv")
        self.away_df.to_csv(f"{path}away_table.csv")

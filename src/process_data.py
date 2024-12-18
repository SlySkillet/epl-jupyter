import pandas as pd

class ProcessData:
    def __init__(self, home_table_raw_path=None, away_table_raw_path=None):
        self.home_table_raw_path = home_table_raw_path
        self.away_table_raw_path = away_table_raw_path

        self.home_df = None
        self.away_df = None

        self.home_df = self._load_and_clean_data(self.home_table_raw_path)
        self.away_df = self._load_and_clean_data(self.away_table_raw_path)

    def _load_and_clean_data(self, file_path):
        columns_to_drop = [
            'W',
            'D',
            'L',
            'PTS',
            'xG',
            'xGA',
            'xPTS',
        ]

        df = pd.read_csv(file_path)
        df_clean = df.drop(columns=columns_to_drop)

        return df_clean

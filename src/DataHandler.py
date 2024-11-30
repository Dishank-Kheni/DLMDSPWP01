import pandas as pd
from sqlalchemy import create_engine

from src.Exceptions import DataLoadException


class DataHandler:
    def _init_(self, db_name='DLMDSPWP01_DB.db'):
        self.engine = create_engine(f'sqlite:///{db_name}')

    def load_csv_to_df(self, file_path):
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError:
            raise DataLoadException(
                f"File not avaialable: {file_path} , please provide proper path!")

    def save_to_db(self, df, table_name):
        df.to_sql(table_name, self.engine, if_exists='replace', index=False)

import pandas as pd
from sqlalchemy import create_engine

from src.Exceptions import DataLoadException


def load_csv_to_df(file_path):
    """Load CSV into DataFrame."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise DataLoadException(f"File not found: {file_path}")


class DataHandler:
    def _init_(self, db_name='data_analysis.db'):
        self.engine = create_engine(f'sqlite:///{db_name}')

    def save_to_db(self, df, table_name):
        """Save DataFrame to SQLite database."""
        df.to_sql(table_name, self.engine, if_exists='replace', index=False)

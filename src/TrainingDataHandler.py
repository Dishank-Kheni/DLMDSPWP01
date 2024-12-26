from src.DataHandler import DataHandler


class TrainingDataHandler(DataHandler):
    """Handles loading and processing of training data."""

    def _init_(self, db_name='data_analysis.db'):
        super()._init_(db_name)
        self.table_name = 'training_data'

    def save_to_db(self, df):
        """Saves DataFrame to the training data table in the database."""
        df.to_sql(self.table_name, self.engine,
                  if_exists='replace', index=False)

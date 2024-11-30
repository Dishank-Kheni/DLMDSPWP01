from Exceptions import DataHandler;

class TrainingDataHandler(DataHandler):
    def _init_(self):
        super()
        self.table_name = 'training_data'

    def save_to_db(self, df):
        """Saves DataFrame to the training data table in the database."""
        df.to_sql(self.table_name, self.engine, if_exists='replace', index=False)
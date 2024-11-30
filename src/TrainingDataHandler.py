from src.DataHandler import DataHandler


class TrainingDataHandler(DataHandler):
    def _init_(self):
        super().__init__()
        self.table_name = 'training_data'

    def save_to_db(self, df):
        super().save_to_db(df, self.table_name)

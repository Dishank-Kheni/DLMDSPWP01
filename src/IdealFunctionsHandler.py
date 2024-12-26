from src.DataHandler import DataHandler


def select_best_fit_functions(training_df, ideal_df):
    best_fit = {}
    max_deviations = {}
    training_columns = [col for col in training_df.columns if col != 'x']
    ideal_columns = [col for col in ideal_df.columns if col != 'x']

    for train_col in training_columns:
        min_deviation = float('inf')
        best_function = None

        for ideal_col in ideal_columns:
            # Calculate the sum of squared deviations for the current pairing
            deviations = training_df[train_col] - ideal_df[ideal_col]
            deviation_sum = (deviations ** 2).sum()

            # Update if this is the minimum deviation so far
            if deviation_sum < min_deviation:
                min_deviation = deviation_sum
                best_function = ideal_col
                # Track the largest deviation
                max_deviation = abs(deviations).max()

        # Store the best match for this training function
        best_fit[train_col] = best_function
        max_deviations[train_col] = max_deviation
    return best_fit, max_deviations


class IdealFunctionsHandler(DataHandler):
    """Handles loading and selecting the ideal functions."""

    def _init_(self, db_name='data_analysis.db'):
        super()._init_(db_name)
        self.table_name = 'ideal_functions'

    def save_to_db(self, df):
        super().save_to_db(df, self.table_name)

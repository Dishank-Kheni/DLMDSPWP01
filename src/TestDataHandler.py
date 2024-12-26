import numpy as np

from src.DataHandler import DataHandler


def map_test_data(test_df, chosen_funcs, ideal_df, max_deviations):
    """Maps test data to chosen ideal functions based on deviation criteria."""
    mapped_results = []

    for index, row in test_df.iterrows():
        x_test, y_test = row['x'], row['y']

        for train_func, ideal_func in chosen_funcs.items():
            # Extract the row in the ideal_df corresponding to x_test
            ideal_row = ideal_df[ideal_df['x'] == x_test]
            if ideal_row.empty:
                continue  # Skip if x_test is not found in the ideal_df

            # Get the y value for the ideal function
            y_ideal = ideal_row[ideal_func].values[0]
            deviation = abs(y_test - y_ideal)

            # Check if the deviation satisfies the threshold
            if deviation <= max_deviations[train_func] * np.sqrt(2):
                mapped_results.append({
                    'x': x_test,
                    'y': y_test,
                    'ideal_function': ideal_func,
                    'deviation': deviation
                })

    return mapped_results


class TestDataHandler(DataHandler):
    """Handles mapping of test data to the chosen ideal functions."""

    def _init_(self, db_name='data_analysis.db'):
        super()._init_(db_name)
        self.results_table = 'test_results'

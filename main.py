import pandas as pd

from src.DataHandler import load_csv_to_df
from src.Exceptions import DataLoadException
from src.IdealFunctionsHandler import (IdealFunctionsHandler,
                                       select_best_fit_functions)
from src.TestDataHandler import TestDataHandler, map_test_data
from src.TrainingDataHandler import TrainingDataHandler
from src.Visulization import Visualizer, plot_data


def main():
    # Initialize handlers
    training_handler = TrainingDataHandler()
    ideal_handler = IdealFunctionsHandler()
    test_handler = TestDataHandler()
    Visualizer()

    try:
        # Load CSV data
        training_df = load_csv_to_df("data/train.csv")
        ideal_df = load_csv_to_df("data/ideal.csv")
        test_df = load_csv_to_df("data/test.csv")

        # Save training data to database
        training_handler.save_to_db(training_df)
        ideal_handler.save_to_db(ideal_df)

        # Choose the best fit ideal functions
        chosen_funcs, max_deviations = select_best_fit_functions(
            training_df, ideal_df)

        # Map test data to the chosen ideal functions
        mapped_results = map_test_data(
            test_df, chosen_funcs, ideal_df, max_deviations)
        #
        # Convert results to DataFrame and save to SQLite
        results_df = pd.DataFrame(mapped_results, columns=[
                                  'x_value', 'y_test', 'ideal_function', 'deviation'])
        test_handler.save_to_db(results_df, table_name="mapped_results")
        #
        # Visualize results using Bokeh
        plot_data(training_df, test_df, ideal_df, chosen_funcs)

    except DataLoadException as e:
        print(f"Data loading error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "_main_":
    main()

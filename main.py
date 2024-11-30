import pandas as pd

from src.Exceptions import DataLoadException
from src.FunctionHandler import IdealFunctionsHandler
from src.TrainingDataHandler import TrainingDataHandler


def main():
    # Initialize handlers
    training_handler = TrainingDataHandler()
    ideal_handler = IdealFunctionsHandler()

    try:
        # Load CSV data
        training_df = training_handler.load_csv_to_df("data/train.csv")
        ideal_df = ideal_handler.load_csv_to_df("data/ideal.csv")

        # Save training data to database
        training_handler.save_to_db(training_df)
        ideal_handler.save_to_db(ideal_df)

        # Choose the best fit ideal functions
        chosen_funcs, max_deviations = ideal_handler.select_best_fit_functions(
            training_df, ideal_df)
        print("Chosen Ideal Functions:", chosen_funcs)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "_main_":
    main()

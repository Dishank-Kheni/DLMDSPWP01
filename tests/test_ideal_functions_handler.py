import logging
import unittest

import pandas as pd

from src.IdealFunctionsHandler import (IdealFunctionsHandler,
                                       select_best_fit_functions)


class TestIdealFunctionsHandler(unittest.TestCase):
    def setUp(self):
        # Mock training and ideal data
        self.training_df = pd.DataFrame({
            'x': [1, 2, 3],
            'y1': [2, 4, 6],
            'y2': [1, 2, 3],
            'y3': [0, 0, 0],
            'y4': [10, 20, 30]
        })
        self.ideal_df = pd.DataFrame({
            'x': [1, 2, 3],
            'ideal_y1': [2, 4, 6],  # Perfect match for y1
            'ideal_y2': [1.1, 2.1, 3.1],  # Close to y2
            'ideal_y3': [0.1, 0.2, 0.3],  # Close to y3
            'ideal_y4': [9, 19, 29],  # close to y4
            'ideal_y5': [2.05, 4.05, 6.05],  # Slightly off for y1
            'ideal_y6': [1.05, 2.05, 3.05],  # Slightly off for y2
            'ideal_y7': [0, 0, 0.1],  # Closer to y3 than ideal_y3
            'ideal_y8': [10.1, 20.1, 30.1]  # very close for y4
        })

        self.expected_results = {
            'y1': 'ideal_y1',  # Best match for y1
            'y2': 'ideal_y6',  # Closest match for y2
            'y3': 'ideal_y7',  # Closest match for y3
            'y4': 'ideal_y8'  # Closest match for y4
        }
        self.handler = IdealFunctionsHandler()

    def test_select_best_fit_functions(self):
        # Call the function
        best_fit, max_deviations = select_best_fit_functions(
            self.training_df, self.ideal_df)

        logging.log(0, msg=best_fit)
        # Verify the number of selected functions matches the number of training columns
        self.assertEqual(len(best_fit), len(self.expected_results))

        # Verify that each training column maps to the correct ideal column
        for train_col, ideal_col in self.expected_results.items():
            self.assertIn(train_col, best_fit)
            self.assertEqual(best_fit[train_col], ideal_col)


if __name__ == '_main_':
    unittest.main()

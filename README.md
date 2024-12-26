# DLMDSPWP01

Python Practical Work.

## Project Overview

This project involves data analysis and visualization using Python. The main components of the project include loading data from CSV files, processing the data, mapping test data to ideal functions, and visualizing the results using Bokeh.

## Project Structure

. ├── .gitignore ├── .vscode/ │ └── settings.json ├── data/ │ ├── ideal.csv │ ├── test.csv │ └── train.csv ├── main.py ├── README.md ├── src/ │ ├── pycache/ │ ├── DataHandler.py │ ├── Exceptions.py │ ├── IdealFunctionsHandler.py │ ├── TestDataHandler.py │ ├── TrainingDataHandler.py │ └── Visulization.py └── tests/ └── test_ideal_functions_handler.py

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Dishank-Kheni/DLMDSPWP01.git
   cd DLMDSPWP01
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script to process the data and generate visualizations:

   ```sh
   python main.py
   ```

2. The results will be saved in an HTML file named `data_visualization.html`.

## Project Components

### DataHandler

Handles loading data from CSV files and saving data to an SQLite database.

### IdealFunctionsHandler

Handles loading and selecting the ideal functions.

### TestDataHandler

Handles mapping of test data to the chosen ideal functions based on deviation criteria.

### TrainingDataHandler

Handles loading and processing of training data.

### Visualization

Handles data visualization using Bokeh.

## Testing

Unit tests are provided in the `tests` directory. To run the tests, use the following command:

```sh
python -m unittest discover -s tests
```

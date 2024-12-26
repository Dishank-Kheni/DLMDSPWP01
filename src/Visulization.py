from bokeh.io import output_file
from bokeh.plotting import figure, show


def plot_data(training_df, test_df, ideal_df, chosen_funcs):
    p = figure(title="Training vs Ideal Functions with Test Data",
               x_axis_label="x_value", y_axis_label="y_value")
    for col, ideal_col in chosen_funcs.items():
        p.line(training_df['x'], training_df[col],
               legend_label=f'{col}', line_width=2)
        p.line(ideal_df['x'], ideal_df[ideal_col],
               legend_label=f'{ideal_col}', line_dash="4 4")

    p.circle(test_df['x'], test_df['y'], size=5,
             color="red", legend_label="Test Data")
    p.legend.title = "Legend"
    show(p)


class Visualizer:
    """Handles data visualization using Bokeh."""

    def _init_(self):
        output_file("data_visualization.html")

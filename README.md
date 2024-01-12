# CSV Data Visualizer Documentation

## Overview

This script implements a simple CSV data visualization tool using PyQt5 for the user interface and pyqtgraph for plotting. Users can load a CSV file, select columns for visualization, and choose to plot either the entire dataset or specific columns.

## Class: DataVisualizer(QMainWindow)

### Class Description:
- The main application class that inherits from QMainWindow.
- Manages the user interface, file loading, and data visualization.

### Class Attributes:
- `self.data`: Stores the loaded CSV data as a pandas DataFrame.

### Class Methods:

#### 1. __init__(self)
- **Description:**
    - Initializes the DataVisualizer class and sets up the main window, widgets, and layout.
- **Widget Hierarchy:**
    - QMainWindow
        - QWidget (central_widget)
            - QVBoxLayout (layout)
                - QLabel (status_label)
                - QPushButton (load_button)
                - QListWidget (column_list)
                - PlotWidget (plot_widget)

#### 2. load_csv(self)
- **Description:**
    - Opens a file dialog to allow the user to select a CSV file.
    - Attempts to load the selected CSV file using pandas and updates the UI accordingly.
    - Handles potential exceptions such as an empty file, parsing errors, or general errors.
- **Invoked By:**
    - Clicking the "Load CSV" button.

#### 3. populate_column_list(self)
- **Description:**
    - Clears the column selection list and adds the option "Entire Dataset" along with the column names from the loaded CSV file.
- **Invoked By:**
    - After successfully loading a CSV file.

#### 4. plot_selected_columns(self)
- **Description:**
    - Handles the selection change event in the column_list.
    - Determines which columns to plot based on user selection.
    - Updates the status label with information about the selected columns.
- **Invoked By:**
    - Selection change event in the column_list.

#### 5. plot_data(self, data)
- **Description:**
    - Clears the plot_widget and plots the selected data using pyqtgraph.
    - Handles both DataFrame (multiple columns) and Series (single column) cases.
    - Sets the plot labels and shows the grid.
- **Invoked By:**
    - load_csv and plot_selected_columns methods.

## Execution Block:

- Creates an instance of the QApplication class.
- Creates an instance of the DataVisualizer class.
- Shows the main window.
- Executes the application.

**End of Documentation**

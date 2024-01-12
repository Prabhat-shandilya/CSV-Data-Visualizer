import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton,
    QFileDialog, QWidget, QLabel, QListWidget
)
import pyqtgraph as pg

class DataVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the main window
        self.setWindowTitle('CSV Data Visualizer')
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create labels for displaying status messages
        self.status_label = QLabel("Load a CSV file to visualize data")
        self.layout.addWidget(self.status_label)

        # Create a button to load CSV file
        self.load_button = QPushButton('Load CSV')
        self.load_button.clicked.connect(self.load_csv)
        self.layout.addWidget(self.load_button)

        # Create a list widget for column selection
        self.column_list = QListWidget()
        self.column_list.itemSelectionChanged.connect(self.plot_selected_columns)
        self.layout.addWidget(self.column_list)

        # Create a pyqtgraph plot widget
        self.plot_widget = pg.PlotWidget()
        self.layout.addWidget(self.plot_widget)

        # Initialize data attribute
        self.data = None

    def load_csv(self):
        """Open a file dialog to load a CSV file and update the UI."""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open CSV File", "", "CSV Files (*.csv)"
        )

        if file_path:
            try:
                # Read CSV file using pandas
                self.data = pd.read_csv(file_path)
                # Populate the column selection list
                self.populate_column_list()
                self.status_label.setText("CSV file loaded successfully")
            except pd.errors.EmptyDataError:
                self.status_label.setText("The selected file is empty")
            except pd.errors.ParserError:
                self.status_label.setText("Error parsing CSV file")
            except Exception as e:
                self.status_label.setText(f"Error loading CSV file: {str(e)}")

    def populate_column_list(self):
        """Populate the column selection list with column names."""
        self.column_list.clear()
        self.column_list.addItem("Entire Dataset")  # Add 'Entire Dataset' option
        self.column_list.addItems(self.data.columns)

    def plot_selected_columns(self):
        """Plot the selected columns or entire dataset based on user selection."""
        selected_item = self.column_list.currentItem()

        if not selected_item or selected_item.text() == "Entire Dataset":
            # If no columns are selected or 'Entire Dataset' is selected, plot entire dataset
            self.plot_data(self.data)
            self.status_label.setText("Plotting entire dataset")
        else:
            # Extract selected column's data and plot
            selected_data = self.data[selected_item.text()]
            self.plot_data(selected_data)
            self.status_label.setText(f"Plotting column: {selected_item.text()}")

    def plot_data(self, data):
        """Plot the data using pyqtgraph."""
        # Plotting
        self.plot_widget.clear()
        if isinstance(data, pd.DataFrame):
            # If DataFrame, plot each column separately
            for i, col in enumerate(data.columns):
                self.plot_widget.plot(data.index, data[col], pen=pg.mkPen(color=(i, 5)))
        else:
            # If a single column, plot it
            self.plot_widget.plot(data.index, data, pen=pg.mkPen(color=(0, 255, 0)))

        # Set plot labels
        self.plot_widget.setLabel('bottom', 'X-Axis')
        self.plot_widget.setLabel('left', 'Y-Axis')

        # Show the plot
        self.plot_widget.showGrid(True, True)


if __name__ == '__main__':
    # Create and run the application
    app = QApplication(sys.argv)
    window = DataVisualizer()
    window.show()
    sys.exit(app.exec_())

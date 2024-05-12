import pandas as pd
import matplotlib.pyplot as plt

def plot_data(file_path):
    """
    Function to plot a scatterplot of data from a file.

    Args:
        file_path (str): Path to the data file.
    """
    # Reading the data from the file using pandas
    data = pd.read_csv(file_path, skiprows=1, names=['x', 'y'], delimiter=', ', engine='python')

    # Creating a scatter plot of the data using matplotlib
    plt.scatter(data['x'], data['y'])
    plt.xlabel('x')  # Setting the label for the x-axis
    plt.ylabel('y')  # Setting the label for the y-axis
    plt.title('Scatter Plot')  # Setting the title of the plot
    plt.show()  # Displaying the plot

# File path
file_path = 'x_y_coordinates.txt'  # File path of the data file

# Call the plot_data function and pass the file path as the input parameter
plot_data(file_path)

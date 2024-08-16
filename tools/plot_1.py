import matplotlib.pyplot as plt
import numpy as np
import argparse

def plot_lines(file, label):
    """ 
    Reads the first column of data from a file, plots it, and displays the plot.

    Args:
        file: Path to the file.
        label: Label for the data (for legend).
    """
    # Read only the first column from the file
    data = np.genfromtxt(file, delimiter=",", usecols=(0,), skip_header=1)

    print(data)
    # Plot the line with the label
    plt.plot(data, label=label)

    # Add labels and title
    plt.xlabel("X-axis (assuming data from first column)")
    plt.ylabel("Y-axis (assuming values in subsequent columns)")
    plt.title("Line Plot from First Column of File")

    # Add legend
    plt.legend()

    # Display the plot
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot data from a file with a label.")
    parser.add_argument('file', type=str, help='Path to the file.')
    parser.add_argument('label', type=str, help='Label for the data.')

    args = parser.parse_args()

    plot_lines(args.file, args.label)

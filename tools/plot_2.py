import matplotlib.pyplot as plt
import numpy as np
import argparse

def plot_lines(file1, file2, label1, label2):
    """ 
    Reads the first column of data from two files, plots them as lines, and displays the plot.

    Args:
        file1: Path to the first file.
        file2: Path to the second file.
        label1: Label for the data from the first file (for legend).
        label2: Label for the data from the second file (for legend).
    """
    # Read only the first column from each file
    data1 = np.genfromtxt(file1, delimiter=",", usecols=(0,), skip_header=1)
    data2 = np.genfromtxt(file2, delimiter=",", usecols=(0,), skip_header=1)

    print(data1)
    # Plot the lines with labels
    plt.plot(data1, label=label1)
    plt.plot(data2, label=label2)

    # Add labels and title
    plt.xlabel("X-axis (assuming data from first column)")
    plt.ylabel("Y-axis (assuming values in subsequent columns)")
    plt.title("Line Plot from First Columns of Two Files")

    # Add legend
    plt.legend()

    # Display the plot
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot data from two files with labels.")
    parser.add_argument('file1', type=str, help='Path to the first file.')
    parser.add_argument('file2', type=str, help='Path to the second file.')
    parser.add_argument('label1', type=str, help='Label for the data from the first file.')
    parser.add_argument('label2', type=str, help='Label for the data from the second file.')

    args = parser.parse_args()

    plot_lines(args.file1, args.file2, args.label1, args.label2)


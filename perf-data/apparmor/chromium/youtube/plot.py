import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt

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

# Example usage (replace with your actual filenames and labels)
file1 = "./cpu_load.txt"
file2 = "./cpu_load_with_aa.txt"
label1 = "yt_play"
label2 = "yt_play_with_apparmor"
plot_lines(file1, file2, label1, label2)


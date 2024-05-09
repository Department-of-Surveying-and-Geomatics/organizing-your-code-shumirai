import pandas as pd
import matplotlib.pyplot as plt

def get_file():

    file_name = ("peters.csv")

def plot_data(file_obj):

    data = pd.read_csv("peters.csv")
    x = data.iloc[:,0]
    y = data.iloc[:,1]

plt.figure(figsize=(8,6))
plt.scatter(x_values,y_values,c="blue")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("scatterplot of data")
plt.grid(True)
plt.legend()
plt.show()



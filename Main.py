import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
df = pd.read_csv('customer_data.csv')

# Output the names of the columns so user can choose which to put on each axis
print("Available columns:")
for col in df.columns:
    print(col)

# Have the user input the axis' and type of graph they want
x_column = input("Enter the column name for the x-axis: ")
y_column = input("Enter the column name for the y-axis: ")
plot_type = input("Enter the plot type (bar, pie, line): ")

# Create a graph based on the user's choice
if x_column in df.columns and y_column in df.columns:
    data = df[[x_column, y_column]]

    if plot_type == "bar":
        data_counts = data.groupby(x_column).count()

        # Increasing order for IncomeRange and YearPurchased
        if x_column in ['IncomeRange', 'YearPurchased']:
            custom_order = sorted(data_counts.index, key=lambda x: int(x.split('-')[0]))
            data_counts = data_counts.reindex(custom_order)

        data_counts.plot(kind='bar')

    elif plot_type == "pie":
        data_pie = data.groupby(x_column).size()
        data_pie.plot(kind='pie', autopct='%1.1f%%')

    elif plot_type == "line":
        data_line = data.groupby(x_column).sum()
        data_line.plot(kind='line', marker='o')

    # Customizes the graph for asthetics
    plt.title(f'Number of {y_column} by {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(f'Number of {y_column}')
    plt.xticks(rotation=45, fontsize=8)

    plt.show()

#If the user input is invalid 
else:
    print("Invalid input. Please check the column names in your data.")

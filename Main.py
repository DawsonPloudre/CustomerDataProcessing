import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
df = pd.read_csv('customer_data.csv')

# Print the available column names so the user can choose
print("Available columns:")
for col in df.columns:
    print(col)

# Prompt the user to enter the column names for x and y
x_column = input("Enter the column name for the x-axis: ")
y_column = input("Enter the column name for the y-axis: ")

# Create a bar graph
if x_column in df.columns and y_column in df.columns:
    data = df[[x_column, y_column]]
    data_counts = data.groupby(x_column).count()

    # Create a custom sorting order for IncomeRange
    if(x_column == 'IncomeRange'):
        custom_order = sorted(data_counts.index, key=lambda x: int(x.split('-')[0]))
        data_counts = data_counts.reindex(custom_order)
    else:
        data_counts = data.groupby(x_column).count()

    data_counts.plot(kind='bar')

    # Customize the graph
    plt.title(f'Number of {y_column} by {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(f'Number of {y_column}')
    plt.xticks(rotation=45, fontsize=8)
    plt.show()
else:
    print("Invalid column names. Please check the column names in your data.")

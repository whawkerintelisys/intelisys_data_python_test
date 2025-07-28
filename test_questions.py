# Python Interview Test with Pandas DataFrames
import pandas as pd
import numpy as np
from openpyxl import Workbook
from openpyxl.styles import PatternFill

# Sample DataFrames
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, np.nan, 40],
    'salary': [50000, 60000, 55000, 70000]
})

df2 = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Eve'],
    'department': ['HR', 'IT', 'Marketing']
})


if __name__ == "__main__":
    # Test Question 1
    # Question 1: Write a function to find rows where a column value is above the column mean
    print()  # Should print rows where salary > mean

    # Test Question 2
    # Question 2: Write a function to replace missing values with column median
    print()  # Should fill NaN with median age

    # Test Question 3
    # Question 3: Write a function to group by a column and calculate the sum and count
    print()  # Should print sum and count of salary by age

    # Test Question 4
    # Question 4: Write a function to merge two DataFrames and keep only matching rows
    print()  # Should print merged DataFrame with matching names

    # Test Question 5
    # Question 5: Write a function using lambda to create a new column with a custom transformation
    print()

    # Test Question 6
    # Question 6: Write a function put the dataframe from question 5 into a spreadsheet not using 
    # pandas but rather openpyxl and highlight one whole column
        # Should save .xlsx file with highlighted column

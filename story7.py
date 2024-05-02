import pandas as pd
import matplotlib.pyplot as plt

#In Python, using zero-based indexing, the fifth column would be indexed as 4.
columns_to_read = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]

data= pd.read_excel('/Users/Sangeetha/Downloads/mis-2022q4-qprpt.xlsx', sheet_name='T2', skiprows=6, usecols=columns_to_read)

print(data.head())
print(data.info())
print(data.columns)


aluminum= [209, 209, 209, 209, 215, 219, 215, 215]



# Extend the quarters list to include the transition quarters
extended_quarters = ['1st Quarter 2021', '2nd Quarter 2021', '3rd Quarter 2021', '4th Quarter 2021',
                     '1st Quarter 2022', '2nd Quarter 2022', '3rd Quarter 2022', '4th Quarter 2022']

# Plot the data
plt.plot(extended_quarters, aluminum, marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Quarter')
plt.ylabel('Production Amount (In thousand metric tons)')
plt.title('US Production of Aluminum By Quarter (2021-2022)')
plt.legend()

# Show the plot
plt.grid(True)
plt.show() 

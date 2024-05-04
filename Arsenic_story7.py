import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




arsenic= [6920, 6470, 7480, 8300, 5600, 10600]



# Extend the quarters list to include the transition quarters
years = ['2017','2018','2019','2020','2021','2022']


# Plot the data
plt.plot(years, arsenic, color="red")
#plt.plot(x_values, aluminum_2022_interp, color="blue", label="2022")

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Consumption Amount in metric tons')
plt.title('US Consumption, estimated, all forms of arsenic')
plt.show()


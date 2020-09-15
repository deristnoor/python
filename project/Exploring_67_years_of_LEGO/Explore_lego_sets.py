# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:34:57 2020

@author: ACER
"""

# Import modules
import pandas as pd

#matplotlib inline
# Read sets data as `sets`
sets = pd.read_csv('datasets/sets.csv')

# Create a summary of average number of parts by year: `parts_by_year`
parts_by_year = sets.groupby("year")["num_parts"].mean()
print(parts_by_year.head())

# Plot trends in average number of parts by year
import matplotlib.pyplot as plt
ax = parts_by_year.plot(x="year",y="num_parts", kind="line")
ax.set_xlabel('Year')
ax.set_ylabel('Number of Parts')
ax.set_title('Lego Sets Over Year')
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:29:01 2020

@author: ACER
"""


# Import modules
import pandas as pd

# Read colors data
colors = pd.read_csv('datasets/colors.csv')

# Print the first few rows
print(colors.head())

# colors_summary: Distribution of colors based on transparency
# -- YOUR CODE FOR TASK 4 --
colors_summary = colors.groupby('is_trans').count()
print(colors_summary)
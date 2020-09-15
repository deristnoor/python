# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:37:36 2020

@author: ACER
"""

# Import modules
import pandas as pd

# themes_by_year: Number of themes shipped by year
# -- YOUR CODE HERE --
sets = pd.read_csv('datasets/sets.csv')
unique_duplicates = sets.drop_duplicates(subset=["year","theme_id"])
unique_year = unique_duplicates["year"].value_counts()
themes = unique_year.sort_index()
themes_by = themes.reset_index()
themes_by_ = themes_by.sort_index()
themes_by_year = themes_by_.rename(columns={'index':'year','year':'theme_id'})
print(themes_by_year.head())

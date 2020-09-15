# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 10:53:41 2020

@author: ACER
"""


# importing modules
import pandas as pd

# Read datasets/yearly_deaths_by_clinic.csv into yearly
yearly = pd.read_csv("datasets/yearly_deaths_by_clinic.csv")

# Print out yearly
print(yearly)

# Calculate proportion of deaths per no. births
import pandas as pd
yearly = pd.read_csv("datasets/yearly_deaths_by_clinic.csv")

proportion_deaths = yearly['deaths']/yearly['births']
yearly['proportion_deaths'] = proportion_deaths

# Extract clinic 1 data into yearly1 and clinic 2 data into yearly2
yearly1 = yearly[yearly.clinic == 'clinic 1']
yearly2 = yearly[yearly.clinic == 'clinic 2']

# Print out yearly1
print(yearly1)

ax = yearly1.plot(x="year", 
    y="proportion_deaths", 
    label="Clinic 1")
yearly2.plot(x="year", 
    y="proportion_deaths", 
    label="Clinic 2", ax=ax)
ax.set_ylabel('Proportion deaths')
ax.set_title('Proportion Deaths on Both Clinic')

# Read datasets/monthly_deaths.csv into monthly
monthly = pd.read_csv('datasets/monthly_deaths.csv', parse_dates=['date'])

# Calculate proportion of deaths per no. births
proportion_deaths = monthly['deaths']/monthly['births']
monthly['proportion_deaths'] = proportion_deaths

# Print out the first rows in monthly
print(monthly.head())

# Plot monthly proportion of deaths
ax = monthly.plot(x="date", 
    y="proportion_deaths")
ax.set_ylabel('Proportion deaths')
ax.set_title('Monthly Proportion of Deaths')

# Date when handwashing was made mandatory
import pandas as pd
handwashing_start = pd.to_datetime('1847-06-01')
print(handwashing_start)

# Split monthly into before and after handwashing_start
before_washing = monthly[monthly.date < '1847-06-01 00:00:00']
after_washing = monthly[monthly.date >= '1847-06-01 00:00:00']

# Plot monthly proportion of deaths before and after handwashing
ax = before_washing.plot(x="date", 
    y="proportion_deaths", 
    label="Before handwashing start")
after_washing.plot(x="date", 
    y="proportion_deaths", 
    label="after handwashing start", ax=ax)
ax.set_ylabel('Proportion deaths')

# Difference in mean monthly proportion of deaths due to handwashing
before_proportion = before_washing.proportion_deaths
after_proportion = after_washing.proportion_deaths
mean_diff = after_proportion.mean() - before_proportion.mean()
print("mean_diff =", mean_diff)

# A bootstrap analysis of the reduction of deaths due to handwashing
boot_mean_diff = []
for i in range(3000):
    boot_before = before_proportion.sample(frac=1, replace=True)
    boot_after = after_proportion.sample(frac=1, replace=True)
    boot_mean_diff.append(boot_after.mean() - boot_before.mean())

# Calculating a 95% confidence interval from boot_mean_diff 
confidence_interval = pd.Series(boot_mean_diff).quantile([0.025,0.975])
print("Confidence Interval:\n",confidence_interval)

# The data Semmelweis collected points to that:
doctors_should_wash_their_hands = True
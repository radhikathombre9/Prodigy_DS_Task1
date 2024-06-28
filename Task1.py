# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:25:18 2024

@author: Radhika
"""

import pandas as pd
import matplotlib.pyplot as plt
 
Data = pd.read_csv(r"C:\Users\Radhika\Downloads\P_Data_Extract_From_World_Development_Indicators\TASK1 DATA.csv")
Data

Data.info

Data.describe
Data.shape
Data.columns

Data['Country Name'].unique()
Data['Country Code'].unique()
Data['Series Name'].unique()
Data['Series Code'].unique()


# =============================================================================
# # line chart
# =============================================================================

# Population Growth (annual 5) from 2014 -2022
series_code = 'SP.POP.GROW'
countries = ['India', 'Afghanistan', 'Australia', 'Canada', 'China', 'France',
        'Japan', 'Nepal', 'Pakistan']
    
filtered_df = Data[(Data['Series Code'] == series_code) & (Data['Country Name'].isin(countries))]

plt.figure(figsize=(10, 6))

for country in countries:
    country_data = filtered_df[filtered_df['Country Name'] == country]
    years = [str(year) for year in range(2014, 2023)]
    plt.plot(years, country_data.iloc[0, 4:].values, label=country)

plt.xlabel('Year')
plt.ylabel('Population growth (annual %)')
plt.title('Population Growth (Annual %) from 2014 to 2022')
plt.legend()
plt.show()

# =============================================================================
# Bar Plot
# =============================================================================
#Total Population in 2022
series_code = 'SP.POP.TOTL'  # Population, Total (% of total population)
year = '2022'

filtered_df = Data[Data['Series Code'] == series_code]
plt.figure(figsize=(12, 6))
plt.bar(filtered_df['Country Name'], filtered_df[year], color='skyblue')
plt.xlabel('Country')
plt.ylabel('Total Population (% of total)')
plt.title(f'Total Population (% of total) in {year}')
plt.xticks(rotation=90)
plt.show()

# Female and male population in 2022

female_series_code = 'SP.POP.TOTL.FE.IN'  # Population, female
male_series_code = 'SP.POP.TOTL.MA.IN'    # Population, male
year = '2021'

female_df = Data[Data['Series Code'] == female_series_code]
male_df = Data[Data['Series Code'] == male_series_code]

female_df = female_df.sort_values('Country Name')
male_df = male_df.sort_values('Country Name')

countries = female_df['Country Name'].values

female_population = female_df[year].values
male_population = male_df[year].values

plt.figure(figsize=(14, 8))
bar_width = 0.35
index = range(len(countries))

plt.bar(index, female_population, bar_width, label='Female Population', color='pink')
plt.bar([i + bar_width for i in index], male_population, bar_width, label='Male Population', color='blue')

plt.xlabel('Country')
plt.ylabel('Population')
plt.title(f'Female and Male Population in {year}')
plt.xticks([i + bar_width / 2 for i in index], countries, rotation=90)
plt.legend()
plt.tight_layout()
plt.show()


# =============================================================================
# Histogram
# =============================================================================
#  Population Growth in 2022

series_code = 'SP.POP.GROW'  
year = '2022'

filtered_df = Data[Data['Series Code'] == series_code]

plt.figure(figsize=(10, 6))
plt.hist(filtered_df[year], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Population Growth (annual %)')
plt.ylabel('Frequency')
plt.title(f'Distribution of Population Growth (annual %) in {year}')
plt.show()  


    
    
    
    
    
    
    
    
    
    
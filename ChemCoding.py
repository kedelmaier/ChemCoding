#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 23:11:11 2021

@author: Kaitlyn Edelmaier & Christopher Schneider
"""

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import numpy as np
from prettytable import PrettyTable 

# Create timeseries plot of the diurnal variation of AOD at 440, 500, 870 nm wavelenegths 
def create_aod_plot(month, data):
    # Plot data
    fig= plt.figure(figsize=(7.5,4))
    plt.plot(data['Timestamp'],data['AOD_440'], label = "AOD_440", color = 'b')
    plt.plot(data['Timestamp'],data['AOD_500'], label = "AOD_500", color = 'g')
    plt.plot(data['Timestamp'],data['AOD_870'], label = "AOD_870", color = 'r')
    # Apply dateformatter to the x-axis in order to extract only HH:MM from the timestamp
    plt.gca().xaxis.set_major_formatter(date_form)
    # Change plot title, y axis name, x axis name, and add font style, weight, type
    plt.rcParams['font.weight'] = 'bold'
    plt.title("Reno, NV: " +  month + " 23, 2013", fontsize=fontsize, fontweight = fontweight, **font)
    plt.ylabel("AOD (Unitless)", fontsize=fontsize, fontweight = fontweight, **font)
    plt.xlabel("Time HH:MM", fontsize = fontsize, fontweight = fontweight, **font)
    # Add legend to top left corner of the plot
    plt.legend(loc='upper left')
    # Show plot
    plt.show()
    
# Calculate min, max, average, median, and standard deviation values 
# of AOD at the three wavelengths 440, 500, 870 nm
# Create table to display values
def create_aod_table(data):
    
# 440 nm wavelength
    #Find max
    max_440 = data['AOD_440'].max()
    #Find min
    min_440 = data['AOD_440'].min()
    #Calculate mean
    mean_440 = data['AOD_440'].mean()
    # Find median
    median_440 = data['AOD_440'].median()
    # Calculate standard deviation
    std_440 = data['AOD_440'].std()
    
# 500 nm wavelength
    # Find max
    max_500 = data['AOD_500'].max()
    # Find min
    min_500 = data['AOD_500'].min()
    # Calculate mean
    mean_500 = data['AOD_500'].mean()
    # Find median
    median_500 = data['AOD_500'].median()
    # Calculate standard deviation
    std_500 = data['AOD_500'].std()
    
# 870 nm wavelength
    # Find max
    max_870 = data['AOD_870'].max()
    # Find min
    min_870 = data['AOD_870'].min()
    # Calculate mean
    mean_870 = data['AOD_870'].mean()
    # Find median
    median_870 = data['AOD_870'].median()
    # Calculate standard deviation
    std_870 = data['AOD_870'].std()
    
    # Create table displaying values
    table = PrettyTable(["", "AOD_440", "AOD_500", "AOD_870"])
    # Add rows containing values of each calculation
    table.add_row(["Min", min_440, min_500, min_870])
    table.add_row(["Max", max_440, max_500, max_870])
    table.add_row(["Mean", mean_440, mean_500, mean_870])
    table.add_row(["Median", median_440, median_500, median_870])
    table.add_row(["Std", std_440, std_500, std_870])
    
    # Output table in console
    print(table)

# Calculate the Angstrom Extinction Exponent (AEE)
def calculate_aee(data, wavelength1, wavelength2):
    # Calculate AEE
    aee = (np.log((data['AOD_' + wavelength1]/ data['AOD_' 
                 + wavelength2]))/np.log(int(wavelength2)/int(wavelength1)))
    # Add AEE values to dataframe
    data['AEE']= aee
    
# Create time series plot of diurnal variation of AEE using AOD at 440 and 870 
# nm wavelengths
def create_aee_plot(data, month):
    # Create plot
    fig= plt.figure(figsize=(7.5,4))
    plt.plot(data['Timestamp'], data['AEE'], color = 'k')
    # Apply dateformatter to the x-axis in order to extract only HH:MM from the timestamp
    plt.gca().xaxis.set_major_formatter(date_form)
    # Change plot title, y-axis name, x-axis name, and the y-limit, and add font weight, size, type
    plt.title('Reno, NV: ' + month + " 23, 2013", fontsize=fontsize, fontweight = fontweight, **font)
    plt.ylabel("AEE (440-870 nm)", fontsize=fontsize, fontweight = fontweight, **font)
    plt.ylim(0,4)
    plt.xlabel("Time (HH:MM)", fontsize=fontsize, fontweight = fontweight, **font)
    # Show plot
    plt.show()
    
# Calculate max, min, mean, median, and std for AEE
# Create table to display values
def create_aee_table(data):
    aee = data['AEE']
    # Find min
    min_aee = aee.min()
    # Find max
    max_aee = aee.max()
    # Calculate mean
    mean_aee = aee.mean()
    # Find median
    median_aee = aee.median()
    # Calculate standard deviation
    std_aee = aee.std()
    
    #Create table displaying values
    table = PrettyTable(["", "AEE"])
    # Add rows containing values of each calculation
    table.add_row(["Min", min_aee])
    table.add_row(["Max", max_aee])
    table.add_row(["Mean", mean_aee])
    table.add_row(["Median", median_aee])
    table.add_row(["Std", std_aee])
    
    #Output table in console
    print(table)

#Read in the data files for Aril and August
file1 = './AERONET_Apr23_2013.csv'
file2 = './AERONET_Aug_23_2013.csv'

# Create date/timestamp format for the dataframe columns
date_format = lambda x: pd.datetime.strptime(x, '%H %M')
date_form = DateFormatter("%H:%M")

# Put april file into pandas dataframe and format the timestamp column
april = pd.read_csv(file1, parse_dates = {"Timestamp" : ["HH", "MM"]}, date_parser=date_format)
# Put August file into pandas dataframe format the timestamp column
august = pd.read_csv(file2, parse_dates = {"Timestamp" : ["HH", "MM"]}, date_parser= date_format)

# Format font style, size, weight for plots
font = {'fontname': "Arial"}
fontsize = 12
fontweight = 'bold'

#
# Activity 1:
# Create diurnal variation of AOD at 440, 500, and 870 nm plot for April 23, 2013 
#
create_aod_plot("April", april)

# Question 1.10.
# What time of day was AOD (440 nm) at it's minimum?
min_index_apr = april['AOD_440'].idxmin()
print("The time of day where AOD 440 nm was at its minimunm was:" + str(april['Timestamp'][min_index_apr]))
# Question 1.11.
# What time of day was AOD (440 nm) at it's maximum?
max_index_apr = april['AOD_440'].idxmax()
print("The time of day where AOD 440 nm was at its maximum was:" + str(april['Timestamp'][max_index_apr]))
# Question 1.13 table
create_aod_table(april)
# create_aee_table(april, "440", "870")

# 
# Activity 2:
# Create a time series plot of the diurnal variation of AEE using AOD at 440 and 870 nm.
#

# Calculate AEE
calculate_aee(april, "440", "870")
# Create the plot for AEE
create_aee_plot(april, "April")
# Question 2.12 table
# Create AEE table
create_aee_table(april)


#
# Activity 3:
# Create diurnal variation of AOD at 440, 500, and 870 nm plot for August 23, 2013 
#

# Create AOD plot
create_aod_plot("August", august)

# Question 3.10.
# What time of day was AOD (440 nm) at it's minimum?
min_index_aug = august['AOD_440'].idxmin()
print("The time of day where AOD 440 nm was at its minimunm was:" + str(august['Timestamp'][min_index_aug]))
# Question 3.11.
# What time of day was AOD (440 nm) at it's maximum?
max_index_aug = august['AOD_440'].idxmax()
print("The time of day where AOD 440 nm was at its maximum was:" + str(august['Timestamp'][max_index_aug]))

# Question 3.13 Table
create_aod_table(august)


# 
# Activity 4:
# Create a time series plot of the diurnal variation of AEE using AOD at 440 and 870 nm.
#
# Calculate AEE
calculate_aee(august, "440", "870")
# Create the plot for AEE
create_aee_table(august)
# Question 4.12 table
# Create AEE table
create_aee_plot(august, "August")


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    data_frame = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data_frame['Year'], data_frame['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    linregress_result = linregress(data_frame['Year'], data_frame['CSIRO Adjusted Sea Level'])
    x = np.arange(data_frame['Year'].min(), 2050 + 1)
    plt.plot(x, linregress_result.slope * x + linregress_result.intercept)

    # Create second line of best fit
    data_frame_recent = data_frame.loc[data_frame['Year'] >= 2000]
    linregress_result_recent = linregress(data_frame_recent['Year'], data_frame_recent['CSIRO Adjusted Sea Level'])
    x_recent = np.arange(2000, 2050 + 1)
    plt.plot(x_recent, linregress_result_recent.slope * x_recent + linregress_result_recent.intercept)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
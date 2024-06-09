# import pandas as pd 
# import matplotlib.pyplot as plt
# df = pd.read_csv("uts/000300.SS.csv")
# print(df.describe())

import numpy as np
import pandas as pd

def histogram_analysis(data, number_of_bins):
    # Perform histogram for each column
    thresholds = {}
    for column in data.columns:
        bin_counts, bin_edges = np.histogram(data[column], bins=number_of_bins)
        
        # Sort bins by counts
        sorted_indices = np.argsort(bin_counts)[::-1]
        bin_counts = bin_counts[sorted_indices]
        bin_max_diff = bin_edges[1:][sorted_indices]
        
        # Calculate sum of bin counts
        temp_sum = 0
        sum_bin_counts = np.sum(bin_counts)
        
        # Find upper bound threshold
        for i in range(number_of_bins):
            temp_sum += bin_counts[i]
            if temp_sum / sum_bin_counts > 0.85:
                break
        thresholds[column] = bin_max_diff[i]
    
    return thresholds

# Read data from CSV
data = pd.read_csv('uts/000300.SS.csv')

# Call histogram_analysis function with your data
result = histogram_analysis(data[['Open', 'High', 'Low', 'Volume']], 10)  # Contoh jumlah bins = 10
print("Upper bound thresholds:", result)

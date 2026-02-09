# This script checks a CSV file for missing values.
# It takes one command line argument - the filename to check.

# Import necessary libraries
import csv 
import numpy as np
import sys

# Check if input to check filename provided  
if len(sys.argv) < 2:
  print('Usage: python check_missing.py <filename>') 
  sys.exit(1)

# Get filename  
filename = sys.argv[1]

# Open the CSV file
with open(filename) as f:

  # Create CSV reader
  reader = csv.reader(f)
  
  # Read first row of headers
  headers = next(reader)  

  # Initialize counts
  num_rows = 0
  num_missing = 0

  # Iterate through each row 
  for row in reader:

    # Increment row count
    num_rows += 1

    # Check each cell for missing values
    for i, d in enumerate(row):
      if d == '' or d == 'nan':
        
        # Print location of missing value
        print(f'Missing value in {filename}, row {num_rows}, column {headers[i]}')
        
        # Increment missing count 
        num_missing += 1

  # Print statistics
  print(f'Total rows: {num_rows}')
  print(f'Total missing: {num_missing}')
  print(f'Missing percentage: {num_missing/num_rows:.2%}')
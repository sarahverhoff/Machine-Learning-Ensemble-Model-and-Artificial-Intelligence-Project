#!/usr/bin/env python
#The example (Melbourne) data is at the file path ../input/melbourne-housing-snapshot/melb_data.csv
#load and explore the data with the following commands:
# save filepath to variable for easier access
#melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
# save filepath to variable for easier access

#melbourne_file_path = 'melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
#melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne data
#melbourne_data.describe()
import pandas as pd
imput = pd.read_csv("melb_data.csv")
print(input.describe()) #fixed the attribute error for the built-on function as to be utilized as the method for print()



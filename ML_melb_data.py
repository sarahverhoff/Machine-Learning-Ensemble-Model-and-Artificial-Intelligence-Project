#!/usr/bin/env python
import pandas as pd
melbourne_file_path = "melb_data.csv"
melbourne_data = pd.read_csv(melbourne_file_path)
melbourne_data.columns #read the index of all column variables or features of the dataset

# dropna drops missing values (think of na as "not available") at first column or feature
#melbourne_data = melbourne_data.dropna(axis=0) 

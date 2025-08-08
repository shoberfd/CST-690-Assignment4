import pandas as pd

# Function to remove duplicates and records with critical missing values
def validate_data(data_frame):
    # Drop rows where 'PNR' or 'Passenger_Name' are missing
    data_frame.dropna(subset=['PNR', 'Passenger_Name'], inplace=True)
    # Remove duplicate records based on the 'PNR' (Passenger Name Record)
    data_frame.drop_duplicates(subset=['PNR'], inplace=True)
    return data_frame
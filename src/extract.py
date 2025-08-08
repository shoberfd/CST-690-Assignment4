import pandas as pd
import logging

# Define a function to securely load data from a file
def load_reservation_data(file_path):
    # Use a try-except block to handle potential file errors
    try:
        data_frame = pd.read_csv(file_path)
        return data_frame
    except Exception as error_msg:
        # Log a critical error if the file cannot be loaded
        logging.error(f"Error occurred while loading data: {error_msg}")
        return None
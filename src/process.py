import pandas as pd
import numpy as np
import logging

def process_reservation_data(data_frame):
    # Use vectorized operations to convert 'Ticket_Price' to numeric.
    # The 'errors=coerce' argument handles invalid strings by turning them into NaN.
    data_frame['Ticket_Price'] = pd.to_numeric(data_frame['Ticket_Price'], errors='coerce')
    
    # FIX for the FutureWarning: Reassign the result back to the column
    # This is the correct, explicit way to fill values without 'inplace=True'
    data_frame['Booking_Status'] = data_frame['Booking_Status'].fillna('Pending')
    
    return data_frame
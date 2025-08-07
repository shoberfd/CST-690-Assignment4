import pandas as pd
from faker import Faker
import numpy as np
from random import choice, randint, uniform
from pathlib import Path

# Initialize Faker and lists
data_generator = Faker()
AIRPORT_CODES = ['SFO', 'MIA', 'DEN', 'HND', 'FRA', 'CDG']
RESERVATION_STATUS = ['Confirmed', 'Cancelled', 'Pending']

# Define function to create a reservation record
def generate_single_record(record_id):
    pnr_code = f"PNR{str(record_id).zfill(6)}"
    return {
        'PNR': pnr_code,
        'Passenger_Name': data_generator.name(),
        'Departure_Airport': choice(AIRPORT_CODES),
        'Arrival_Airport': choice(AIRPORT_CODES),
        'Ticket_Price': round(uniform(150.0, 1800.0), 2),
        'Booking_Status': choice(RESERVATION_STATUS)
    }

# Create a list of 200 initial reservations
all_reservations = [generate_single_record(i) for i in range(1, 201)]

# Deliberately introduce edge cases for debugging practice
# 1. Add some records with missing values
for _ in range(5):
    all_reservations[randint(0, 199)]['Ticket_Price'] = np.nan
    all_reservations[randint(0, 199)]['Booking_Status'] = None
# 2. Duplicate a few existing records
all_reservations.extend([all_reservations[0], all_reservations[10], all_reservations[20]])
# 3. Insert invalid airport codes
all_reservations[15]['Departure_Airport'] = 'YYY'
all_reservations[25]['Arrival_Airport'] = 'ZZZ'
# 4. Introduce incorrect data types in the price column
all_reservations[30]['Ticket_Price'] = 'FREE'
all_reservations[40]['Ticket_Price'] = 'INVALID'

# Convert the list of dictionaries to a DataFrame and save to CSV
data_df = pd.DataFrame(all_reservations)
Path("data").mkdir(exist_ok=True)
data_df.to_csv("data/reservations.csv", index=False)
print("Synthetic flight reservation data created at data/reservations.csv")
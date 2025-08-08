import pandas as pd

# Define a function to process the reservations
def process_reservation_data(data_frame):
    processed_records = []
    # Loop through each row of the DataFrame
    for index, record in data_frame.iterrows():
        try:
            record['Ticket_Price'] = float(record['Ticket_Price'])
            if pd.isna(record['Booking_Status']):
                record['Booking_Status'] = 'Pending'
            processed_records.append(record)
        except:
            # Silently skip records with invalid data
            continue
    return pd.DataFrame(processed_records)
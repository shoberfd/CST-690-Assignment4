import logging
from src.extract import load_reservation_data
from src.process import process_reservation_data
from src.validate import validate_data

# Set up basic logging for the entire workflow
logging.basicConfig(level=logging.INFO)

# Main function to run the complete automation workflow
def run_automation_workflow(file_path):
    logging.info("Starting the flight-booking automation workflow...")
    
    # Step 1: Load the raw data from the specified path
    reservations_df = load_reservation_data(file_path)
    
    # Step 2: Validate the data
    reservations_df = validate_data(reservations_df)
    
    # Step 3: Process the data
    reservations_df = process_reservation_data(reservations_df)
    
    logging.info(f"Workflow finished. Successfully processed {len(reservations_df)} records.")

# Entry point of the script
if __name__ == "__main__":
    run_automation_workflow('data/reservations.csv')
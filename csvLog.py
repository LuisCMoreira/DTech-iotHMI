import csv
from datetime import datetime


def mainLog( data):
    file_path = './logs/logFile.csv'

    columns = [ 'Event', 'Time', 'Position']
    data = [[data] + [datetime.now().strftime("%Y-%m-%d %H:%M:%S")] + ['axisposition']] 

    try:
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # If the file is empty, write the header (column names) to the CSV file
            if csvfile.tell() == 0:
                writer.writerow(columns)
            
            # Write the data rows to the CSV file
            for row in data:
                writer.writerow(row)
                
            print(f"Data successfully appended to '{file_path}'.")
            
    except IOError as e:
        print(f"Error writing to CSV file: {e}")

# Example usage


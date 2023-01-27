import csv
import random
import string
from .Constants import *

class Helper:
  def __init__(self, old_filename, new_filename):
    self.old_filename = old_filename
    self.new_filename = new_filename

  # Get non-anonymized data from file
  def __read_data(self):
    data = []

    with open(self.old_filename, 'r') as csvfile:
      csv_reader = csv.DictReader(csvfile)
      
      for row in csv_reader:
        data.append(row)
    return data
  
  # Create a random string for names
  def __anonymize_name(self, name):
    random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
    return f'{name[0]}{random_string}' #Keep the first letter the same
  
  # Create a random string for address
  def __anonymize_address(self, address):
    random_num = random.randint(1, 99)
    random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
    return f'{random_num} {random_string} {address.split(" ")[-1]}' #Keep the end of the address the same

  #Anonymize each field
  def anonymize_all_data(self, data):
    anonymized_data = []
    for row in data:
      # Append the data and anonymize each field using private functions
      anonymized_data.append({COLUMN_HEADERS[0]: self.__anonymize_name(row[COLUMN_HEADERS[0]]),
                              COLUMN_HEADERS[1]: self.__anonymize_name(row[COLUMN_HEADERS[1]]),
                              COLUMN_HEADERS[2]: self.__anonymize_address(row[COLUMN_HEADERS[2]]),
                              COLUMN_HEADERS[3]: row[COLUMN_HEADERS[3]]
                            })
    return anonymized_data

  # Save to file
  def save_anonymized_data(self):
    print(f'Saving anonymized data to {self.new_filename}...')
    data = self.__read_data()
    data = self.anonymize_all_data(data)

    with open(self.new_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    
    print('... Done!')


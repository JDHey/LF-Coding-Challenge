import csv
import random
import string
import datetime
from .Constants import *

class Mock_data_helper:
  def __init__(self, num_rows = 10, filename = 'people.csv'):
    self.num_rows = num_rows
    self.filename = filename

  def __generate_random_name(self, is_first_name = True):
    if (is_first_name):
      return random.choice(FIRST_NAMES)
    else:
      return random.choice(LAST_NAMES)
  
  def __generate_random_address(self):
    return f'{random.randint(11,99)} { random.choice(ADDRESSES) }'
  
  def __generate_random_date(self):
    return datetime.date(random.randint(1900, 2020), random.randint(1, 12), random.randint(1, 28))

  #Generates fields for each row
  def __generate_data(self):
    data = []

    # Loop to generate the mock data
    for i in range(self.num_rows):
      data.append({COLUMN_HEADERS[0]: self.__generate_random_name(True),
                  COLUMN_HEADERS[1]: self.__generate_random_name(False),
                  COLUMN_HEADERS[2]: self.__generate_random_address(),
                  COLUMN_HEADERS[3]: self.__generate_random_date().strftime('%d/%m/%Y')
                })
    return data

  #Save to csv
  def generate_mock_data(self):
    print(f'Saving new mock data to {self.filename}...')
    data = self.__generate_data()

    with open(self.filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=COLUMN_HEADERS)
        writer.writeheader()
      
        for row in data:
            writer.writerow(row)
    print('... Done!')
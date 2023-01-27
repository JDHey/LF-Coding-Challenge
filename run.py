import os
import csv
from anonymize import Generator, Anonymizer


if __name__ == '__main__':
  print('START MAIN')

  SAVE_LOCATION = './output/'
  NUM_ROWS = 100

  # Create the data folder if it doesn't exist
  if not os.path.exists(SAVE_LOCATION):
    os.mkdir(SAVE_LOCATION)

  # Generate the mock data
  filename = os.path.join(SAVE_LOCATION,'people.csv')
  helper = Generator.Mock_data_helper(num_rows = NUM_ROWS, filename = filename)
  helper.generate_mock_data()

  # Anonymize the mock data
  helper = Anonymizer.Helper(old_filename = filename, new_filename = os.path.join(SAVE_LOCATION,'anonymized_people.csv'))
  helper.save_anonymized_data()

  print('END MAIN')
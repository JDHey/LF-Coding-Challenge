from anonymize import Generator
import os
import csv

## Unit tests

# Test that the mock data is generated and has the correct number of rows
def test_generate_mock_data_file_exists(dir):
  print('Testing mock data generation')
  NUM_ROWS = 100
  filename = os.path.join(dir,'test_people.csv')
  helper = Generator.Mock_data_helper(num_rows = NUM_ROWS, filename = filename)
  helper.generate_mock_data()
  assert os.path.exists(filename)

  with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # skip header
    rows = 0
    for row in reader:
      rows += 1
  print (f'{rows} rows in {filename} file')
  assert rows == NUM_ROWS
  print('Passed!')


##MAIN
if __name__ == '__main__':
  #Generate temp test folder
  SAVE_LOCATION = 'test_temp_data/'
  if not os.path.exists(SAVE_LOCATION):
    os.mkdir(SAVE_LOCATION)

  try:
    print('Running unit tests...')
    test_generate_mock_data_file_exists(SAVE_LOCATION)
  finally:
    #Delete temp test folder and contents
    for file in os.listdir(SAVE_LOCATION):
      os.remove(os.path.join(SAVE_LOCATION, file))
    os.rmdir(SAVE_LOCATION)
  
  print('GENERATOR - COMPLETED ALL TESTS')
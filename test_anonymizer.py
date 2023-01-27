from anonymize import Anonymizer
import os
import csv

## Unit tests
def test_anonymize_name():
  print('Testing name anonymization')
  helper = Anonymizer.Helper(old_filename = 'test.csv', new_filename = 'test.csv')
  assert helper._Helper__anonymize_name('John') != 'John'
  assert helper._Helper__anonymize_name('Jane') != 'Jane'
  assert helper._Helper__anonymize_name('Joe') != 'Joe'
  assert helper._Helper__anonymize_name('Jill') != 'Jill'
  assert helper._Helper__anonymize_name('Jack') != 'Jack'
  print('Passed!')

def test_anonymize_address():
  print('Testing address anonymization')
  helper = Anonymizer.Helper(old_filename = 'test.csv', new_filename = 'test.csv')
  assert helper._Helper__anonymize_address('123 Main St') != '123 Main St'
  assert helper._Helper__anonymize_address('456 Test St') != '456 Test St'
  assert helper._Helper__anonymize_address('789 Main St') != '789 Main St'

  #Keep suffix
  assert helper._Helper__anonymize_address('123 Main St')[-2:] == 'St'
  assert helper._Helper__anonymize_address('456 Test Drve')[-4:] == 'Drve'
  assert helper._Helper__anonymize_address('789 Main Place') [-5:] == 'Place'
  print('Passed!')

##MAIN
if __name__ == '__main__':
  print('Running unit tests...')
  test_anonymize_name()
  test_anonymize_address()
  print('ANONYMIZER - COMPLETED ALL TESTS')
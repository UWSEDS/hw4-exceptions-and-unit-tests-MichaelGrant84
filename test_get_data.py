"""
Unit test for get_data.py
"""

import unittest
import urllib3
import os
import imp

get_data = imp.load_source('get_data','get_data.py')
remove_data = imp.load_source('remove_data','remove_data.py')

class TestGetData(unittest.TestCase):

    #test for when file locally present
    def test_Local(self):
        expected_out = 'Looks like this file already exist.'
        get_data.get_data('https://data.seattle.gov/resource/4xy5-26gy.csv')
        result = get_data.get_data('https://data.seattle.gov/resource/4xy5-26gy.csv')
        self.assertEqual(result, expected_out)

    #test for when page link is bad
    def test_BadURL(self):
        expected_out = 'Page or file does not exist.'
        result = get_data.get_data('https://data.seattle.gov/resource/4xy5-26gy.csvvv')
        self.assertEqual(result, expected_out)
        result = get_data.get_data('https://data.seattle.gov/resource/')
        self.assertEqual(result, expected_out)
        result = get_data.get_data('https://data.seatsadasdtle.gov/')
        self.assertEqual(result, expected_out)

    #test for when file is not present locally but exists in the web
    def test_NotPresent(self):
        expected_out = 'File downloaded.'
        #must make sure to remove the file first before testing for correctness on file download
        remove_data.remove_data('https://data.seattle.gov/resource/4xy5-26gy.csv')
        result = get_data.get_data('https://data.seattle.gov/resource/4xy5-26gy.csv')
        self.assertEqual(result, expected_out)

    #test to see if the data was succesfully removed
    def test_RemoveData(self):
        expected_out = 'File removed.'
        #make sure file is present before testing the remove
        get_data.get_data('https://data.seattle.gov/resource/4xy5-26gy.csv')
        result = remove_data.remove_data('https://data.seattle.gov/resource/4xy5-26gy.csv')
        self.assertEqual(result, expected_out)
        result = remove_data.remove_data('https://data.seattle.gov/resource/4xy5-26gy.csv')
        expected_out = 'This file does not exist.'
        self.assertEqual(result, expected_out)

if __name__ == '__main__':
    unittest.main()

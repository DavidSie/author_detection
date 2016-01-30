__author__ = 'davidsiecinski'
import fileReader
import unittest
import os

class fileReaderTests(unittest.TestCase):

    def test_prepare_enironment(self):
        filereader=fileReader.fileReader()
        base_path="test_path"
        filereader.prepare_enironment(base_path)
        learning_path=base_path+"/learning"
        test_path=base_path+"/test"
        # self.assertEqual(os.path.exists(learning_path), True)
        # self.assertEqual(os.path.exists(test_path), True)
        # creates file after exiting from the test

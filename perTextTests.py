__author__ = 'davidsiecinski'
import unittest
import perText

class perTextTests(unittest.TestCase):

    def test_number_of_words(self):
        pertext=perText.perText()
        self.assertEqual(pertext.number_of_words("one two three"), 3)
    def test_number_of_sentences(self):
        pertext=perText.perText()
        self.assertEqual(pertext.number_of_sentences("One interesting sentence. And second."), 2)

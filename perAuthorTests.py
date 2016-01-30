from __future__ import division
__author__ = 'davidsiecinski'
import unittest
import perAuthor


class perAuthorTests(unittest.TestCase):

    def test_avg_number_of_words(self):
        perauthor=perAuthor.perAuthor()
        texts=[]
        texts.append("One two three. Far Far away.")
        texts.append("Short sentence.")
        self.assertEqual(perauthor.avg_number_of_words(texts), 4)

    def test_avg_number_of_words2(self):
        perauthor=perAuthor.perAuthor()
        texts=[]
        texts.append("One two three. Far away.")
        texts.append("Short sentence.")
        self.assertEqual(perauthor.avg_number_of_words(texts), 3.5)

    def test_avg_length_of_words(self):
        perauthor=perAuthor.perAuthor()
        texts=[]
        texts.append("One two three.")
        texts.append("Short sentence.")
        self.assertAlmostEquals(perauthor.avg_length_of_words(texts),4.8)

    def test_avg_length_of_words2(self):
        perauthor=perAuthor.perAuthor()
        texts=[]
        texts.append("three?")
        texts.append("Short!")
        self.assertEqual(perauthor.avg_length_of_words(texts),5)
         # don't count ! nor ?

    def test_avg_number_of_nouns_per_text(self):
        perauthor=perAuthor.perAuthor()
        texts=[]
        texts.append("Cow. Ship. ")
        texts.append("Girl wearing bikini")
        self.assertEqual(perauthor.avg_number_of_nouns_per_text(texts), 2)
        #     count(Cow,ship,girl,bikini)/2

    def test_avg_number_of_verbs_per_text(self):
        perauthor=perAuthor.perAuthor()
        texts=[]
        texts.append("I was cooking")
        texts.append("He drives every day.")
        self.assertEqual(perauthor.avg_number_of_verbs_per_text(texts), 1.5)

    def test_avg_number_of_numbers_per_text(self):
        perauthor=perAuthor.perAuthor()
        texts=[]
        texts.append("Since 1945 until 1989 ")
        texts.append("He drive every three days.")
        self.assertAlmostEquals(perauthor.avg_number_of_numbers_per_text(texts), 1.5)
    # doesn't detect 'second'

    def test_avg_number_of_question_marks_per_text(self):
        perauthor=perAuthor.perAuthor()
        texts=[]
        texts.append("How long did it take?")
        texts.append("He drives every 2-nd day.")
        self.assertAlmostEquals(perauthor.avg_number_of_question_marks_per_text(texts), 0.5)

    def test_avg_number_of_exclamation_marks_per_text(self):
        perauthor=perAuthor.perAuthor()
        texts=[]
        texts.append("How long did it take?")
        texts.append("That's the end of the world!")
        self.assertAlmostEquals(perauthor.avg_number_of_exclamation_marks_per_text(texts), 0.5)

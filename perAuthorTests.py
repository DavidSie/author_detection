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

    def test_avg_length_of_words(self):
        perauthor=perAuthor.perAuthor()
        texts=[]
        texts.append("One two three.")
        texts.append("Short sentence.")
        self.assertAlmostEquals(perauthor.length_of_words(texts),4.8)

    def test_avg_length_of_words2(self):
        perauthor=perAuthor.perAuthor()
        texts=[]
        texts.append("three?")
        texts.append("Short!")
        self.assertEqual(perauthor.length_of_words(texts),5)
         # don't count ! nor ?

    def test_avg_number_of_nouns(self):
        perauthor=perAuthor.perAuthor()
        texts=[]
        texts.append("One two three. Far Far away.")
        texts.append("Short sentence.")
        self.assertEqual(perauthor.avg_number_of_nouns(texts), 2)
        # count (One two three sentence)/2

    def test_avg_number_of_verbs(self):
        perauthor=perAuthor.perAuthor()
        texts=[]
        texts.append("I was cooking")
        texts.append("He drives every day.")
        self.assertEqual(perauthor.number_of_verbs(texts), 1)

    def test_avg_number_of_numbers(self):
        perauthor=perAuthor.perAuthor()
        texts=[]
        texts.append("Since 1945 until 1989 ")
        texts.append("He drives every 2-nd day.")
        self.assertAlmostEquals(perauthor.avg_number_of_numbers(texts), 1.5)

    def test_avg_number_of_question_marks(self):
        perauthor=perAuthor.perAuthor()
        texts=[]
        texts.append("How long did it take?")
        texts.append("He drives every 2-nd day.")
        self.assertAlmostEquals(perauthor.avg_number_of_question_marks(texts), 0.5)

    def test_avg_number_of_exclamation_marks(self):
        perauthor=perAuthor.perAuthor()
        texts=[]
        texts.append("How long did it take?")
        texts.append("That's the end of the world!")
        self.assertAlmostEquals(perauthor.avg_number_of_exclamation_marks(texts), 0.5)

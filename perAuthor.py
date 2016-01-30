__author__ = 'davidsiecinski'
import perText
import nltk

class perAuthor:


    def avg_number_of_words(self,list_of_strings):
        pertext= perText.perText()
        sum=0.0;
        for string in list_of_strings:
            sum+=pertext.number_of_words(string)
        return sum/len(list_of_strings)

    def avg_length_of_words(self,list_of_strings):
        sum_of_length_of_all__words=0.0
        number_of_all_words=0
        for text in list_of_strings:
             for word in text.split():
                    list_of_letters=list(word)
                    # list1,list2,list3,list4=[]
                    while '!' in list_of_letters: list_of_letters.remove('!')
                    while '?' in list_of_letters: list_of_letters.remove('?')
                    while '.' in list_of_letters: list_of_letters.remove('.')
                    while ',' in list_of_letters: list_of_letters.remove(',')
                    sum_of_length_of_all__words+=len(list_of_letters)
                    number_of_all_words+=1

        return sum_of_length_of_all__words/number_of_all_words

    def avg_number_of_nouns_per_text(self,list_of_strings):
        sum_of_all__nouns=0.0
        # nltk.download() for the first time
        for sentence in list_of_strings:
            tokens = nltk.word_tokenize(sentence)
            for word, tag in nltk.tag.pos_tag(tokens):
                if 'NN' in tag:
                    sum_of_all__nouns+=1

        return sum_of_all__nouns/len(list_of_strings)

    def avg_number_of_verbs_per_text(self,list_of_strings):
        sum_of_all_verbs=0.0
        for sentence in list_of_strings:
            tokens = nltk.word_tokenize(sentence)
            for word, tag in nltk.tag.pos_tag(tokens):
                if 'VB' in tag:
                    sum_of_all_verbs+=1
        return sum_of_all_verbs/len(list_of_strings)

    def avg_number_of_numbers_per_text(self, list_of_strings):
        sum_of_all_verbs=0.0
        for sentence in list_of_strings:
            tokens = nltk.word_tokenize(sentence)
            for word, tag in nltk.tag.pos_tag(tokens):
                if 'CD' in tag:
                    sum_of_all_verbs+=1
        return sum_of_all_verbs/len(list_of_strings)

    def avg_number_of_question_marks_per_text(self, list_of_strings):
        sum_of_all_question_marks=0.0
        for string in list_of_strings:
            for sign_flow in string.split(' '):
                if '?' in sign_flow:
                    sum_of_all_question_marks+=1
        return sum_of_all_question_marks/len(list_of_strings)

    def avg_number_of_exclamation_marks_per_text(self,list_of_strings):
        sum_of_all_question_marks=0.0
        for string in list_of_strings:
            for sign_flow in string.split(' '):
                if '!' in sign_flow:
                    sum_of_all_question_marks+=1
        return sum_of_all_question_marks/len(list_of_strings)

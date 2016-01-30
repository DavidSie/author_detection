__author__ = 'davidsiecinski'


class perText:

    def number_of_words(self,string):
        return len(string.split())

    def number_of_sentences(self,string):

        list_dot=string.split('.')
        while '' in list_dot: list_dot.remove('')
        list_question=[]
        for str in list_dot:
            list_question=list_question+(str.split('!'))
        list_exclamation=[]
        for str in list_question:
            list_exclamation=list_exclamation+(str.split('!'))
        return len(list_exclamation)

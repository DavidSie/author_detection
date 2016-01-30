__author__ = 'davidsiecinski'
import fileReader
import perText
import perAuthor
from sklearn.naive_bayes import MultinomialNB

filereader=fileReader.fileReader()
pertext=perText.perText()
perauthor=perAuthor.perAuthor()
autors_index=[]
clf = MultinomialNB()

def prepare_feature_list(list_of_texts):
    features=[]
    features.append(perauthor.avg_length_of_words(list_of_texts))
    features.append(perauthor.avg_number_of_exclamation_marks_per_text(list_of_texts))
    features.append(perauthor.avg_number_of_nouns_per_text(list_of_texts))
    features.append(perauthor.avg_number_of_numbers_per_text(list_of_texts))
    features.append(perauthor.avg_number_of_question_marks_per_text(list_of_texts))
    features.append(perauthor.avg_number_of_verbs_per_text(list_of_texts))
    features.append(perauthor.avg_number_of_words(list_of_texts))
    for text in list_of_texts:
        features.append(pertext.number_of_words(text))
        features.append(pertext.number_of_sentences(text))
    return features

def learn(path):
    data=filereader.load_all_data_to_learn(path)
    X=[]
    y=[]
    for author_with_texts in data:
        author,list_of_texts=author_with_texts
        if author not in autors_index:
            autors_index.append(author)
        y.append( autors_index.index(author))
        X.append(prepare_feature_list(list_of_texts))
    clf.fit(X, y)

def detect(path):
    X=[]
    if path=="" or path==None:
        path="data/test"
    else:
        path+="/data/test"
    list_of_texts=filereader.load_all_files_from_dir(path)
    for text in list_of_texts:
        list_with_txt=[]
        list_with_txt.append(text)
        print(clf.predict(prepare_feature_list(list_with_txt)))



        # for text in list:
        #     print "inner loop" + author_touple




ans=True
while ans:
    print ("""
    init [dir_name] - creates directory
    learn [dir_name] -learning from learn folder
    detect [dir_name] - detecting from test folder
    quit - quit
    """)
    ans=raw_input("What would you like to do? ")
    path=""
    try:
        path=ans.split(" ")[1]
    except:
        pass
    if "init" in ans.lower():
        filereader.prepare_enironment(path)
        print("\n init")
        exit(0)
    elif "learn" in ans.lower():
        print "______________________________________________________ \n"
        print "each author should have the same amount of examples \n"
        learn(path)
    elif "detect" in ans.lower():
        print "______________________________________________________ \n"
        print "detecting \n"
        detect(path)
    elif "quit" in  ans.lower():
      print("\n Goodbye")
      exit(0)
    elif ans !="":
      print("\n Not Valid Choice Try again")


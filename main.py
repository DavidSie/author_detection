__author__ = 'davidsiecinski'
import fileReader
import perText
import perAuthor

filereader=fileReader.fileReader()
pertext=perText.perText()
perauthor=perAuthor.perAuthor()

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
      print("\n learn")
    elif "detect" in ans.lower():
      print("\n Student Record Found")
    elif "quit" in  ans.lower():
      print("\n Goodbye")
      exit(0)
    elif ans !="":
      print("\n Not Valid Choice Try again")
import os

fileName ='hang.book'
words = []
def saveFile():
    with open(fileName,'w') as file:
        for word in words:
            file.write(word+',')

if os.path.isfile(fileName):
    with open(fileName,'r') as file:
        temp_words = file.read()
        temp_words = temp_words.split(',')
        words = [x for x in temp_words if x.strip()]



print("Gib ein Wort an: ")
givenWord = input()
words.append(givenWord)
saveFile()





def showWords():
    for item in words:
        print(item,end=",")

showWords()


def removeWord(deleteWord):

    if deleteWord in words:
        words.remove(deleteWord)
        print(deleteWord+" has been removed!")
        saveFile()

    else:
        print("Word is not in Book")


removeWord('Hurensohn')
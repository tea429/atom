




def checkPalindrome(word):

    word = word.upper()
    range = len(word)
    letter = word[range::-1]
    letter = letter.upper()


    if word == letter:
        print(word+" is a Palindrome")
    else:
        print(word+" is no Palindrome")

isItorNot = input("Is your incoming word a Palindrome?: ")


checkPalindrome(isItorNot)

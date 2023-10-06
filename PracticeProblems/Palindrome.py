# Michael Williamson
# Palindrome
# 7/23/2020

userInput = input("What word, phrase, or number do you wish to check? ")


def removeSpace(passedstring):
    return passedstring.replace(" ", "")


check = removeSpace(userInput)
reverse = check[::-1]
if check == reverse:
    print("\"" + userInput + "\"" + " is a palindrome!")
else:
    print("\"" + userInput + "\"" + " is not a palindrome.")

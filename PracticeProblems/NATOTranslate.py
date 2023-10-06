# Michael Williamson
# NATO Phonetic/Morse Code Translator
# 7/29/2020

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'} 

NATO_PHONETIC_DICT = { 'A':'Alpha', 'B':'Bravo', 
                    'C':'Charlie', 'D':'Delta', 'E':'Echo', 
                    'F':'Foxtrot', 'G':'Golf', 'H':'Hotel', 
                    'I':'India', 'J':'Juliet', 'K':'Kilo', 
                    'L':'Lima', 'M':'Mike', 'N':'November', 
                    'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 
                    'R':'Romeo', 'S':'Sierra', 'T':'Tango', 
                    'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 
                    'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}

sentence = input("What phrase would you like to convert to NATO Phonetic/Morse Code or decrypt (Only alphabet)? ")
sentence = sentence.upper()
sentence = sentence.replace(" ", "")

nato = ""
morse = ""

for i in sentence:
    nato = nato + NATO_PHONETIC_DICT[i] + " "
    morse = morse + MORSE_CODE_DICT[i] + " "


print("Nato Phonetic: " + nato)
print("Morse Code: " + morse)
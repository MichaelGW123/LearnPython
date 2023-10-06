# Michael Williamson
# Wikipedia Summary Program
# 7/28/2020

import wikipedia

result = input("What would you like a summary on? ")

summary = wikipedia.summary(result, sentences = 2)

print(summary)
# Michael Williamson
# 1/10/2022
# Given the quote: "Always do your best. Your best is going to change from moment to moment;
# it will be different when you are healthy as opposed to sick. Under any circumstance, simply do
# your best, and you will avoid self-judgment, self-abuse and regret." Complete the program so
# that it will take a word as input and output the number of times that word appears in the
# quote.
# Sample Input: "best" -> Sample Output: 3
import time
import string
start_time = time.time()

# Second attempt
target = 'best'
quote_dictionary = {}

def count_occurences(file, target, quote_dictionary):
    if len(quote_dictionary) == 0:
        for line in file:
            line_stripped = line.translate(str.maketrans('', '', string.punctuation))
            for word in line_stripped.split():
                if word not in quote_dictionary:
                    quote_dictionary[word] = 1
                else:
                    quote_dictionary[word] += 1
    
    if target in quote_dictionary:
        return quote_dictionary[target]
    else:
        return 0


with open(r'C:\Users\Michael JITN\Documents\Work\Arete Interview\Excersies\Problem 2\test.txt', 'r') as file:
    count = count_occurences(file, target, quote_dictionary)

print("Target word is: ", target)
print("And its occurences: ", count)
print("--- %s seconds ---" % (time.time() - start_time))

# Optimization - has to check every word. 
# Dictionary, O(n) for first run, O(1) for all occurences after for the same input
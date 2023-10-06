# Michael Williamson
# 1/10/2022
# Given a text input, find the longest word and output it.
# Sample Input: "This is an awesome text" -> Sample Output: "awesome"
import time
start_time = time.time()

# Second attempt O(N)
def find_longest(file):
    temp_longest = ''
    for line in file:
        for word in line.split():
           if len(word) > len(temp_longest):
                temp_longest = word
    return temp_longest


with open(r'C:\Users\Michael JITN\Documents\Work\Arete Interview\Excersies\Problem 1\test.txt', 'r') as file:
    longest = find_longest(file)

print("Longest word is: ", longest)
print("And its length is: ", len(longest))
print(f"--- {time.time() - start_time}s seconds ---")

# Potential Optimization - Sort
# Merge sort based on length O(nlogn) + O(1). O(1) because accessing the last element.
# If accessing multiple times, could use search methods for n length word
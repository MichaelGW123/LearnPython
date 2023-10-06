# Michael Williamson
# 1/10/2022
# You are given a list of items and need to find all the possible orders of the items. The output
# should be a list containing all possible orders.
# Sample Input:[‘a’,’b’] -> Sample Output: [(‘a’,’b’),(‘b’,’a’)]
import time
import itertools
start_time = time.time()

# First attempt
input = ['first', 'second']

permutations = list(itertools.permutations(input, len(input)))

print(permutations)
print("--- %s seconds ---" % (time.time() - start_time))
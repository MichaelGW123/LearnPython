# Michael Williamson
# 1/10/2022
# You are given a list of items and need to find all the possible orders of the items. The output
# should be a list containing all possible orders.
# Sample Input:[‘a’,’b’] -> Sample Output: [(‘a’,’b’),(‘b’,’a’)]
import time
start_time = time.time()

# First attempt
input = ['first', 'second', 'third']

def permutations(l):
    if len(l) == 1:
        return [l]
    return [[l[i]] + p for i in range(len(l))for p in permutations(l[:i] + l [i+1:])]

print(permutations(input))
print("--- %s seconds ---" % (time.time() - start_time))
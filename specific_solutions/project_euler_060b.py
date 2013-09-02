"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these
four primes, 792, represents the lowest sum for a set of four primes with
this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.

"""


import time
t1 = time.time()
from numpy import *

def prime_import():
    infile = open('prime_list_e8.txt', 'r') # specifiy which file to use
    prime_list = infile.read()
    prime_list = prime_list.split(',')
    prime_list = prime_list[:-1]
    infile.close()
    #print prime_list[:20]
    for index in xrange(len(prime_list)):
        prime_list[index] = int(prime_list[index])
    #print prime_list[:20]
    return prime_list

def prime_check_maker(prime_list):
    # Generates a list with an entry for each possible prime: 0-composite,
    # 1-prime
    prime_check = [0] * (prime_list[-1] + 1)
    for prime in prime_list:
        prime_check[prime] = 1
    return prime_check

def is_prime(n):
    #return n in prime_list
    if n < prime_list[-1] + 1:
        return prime_check[n]   #returns error if number too high
    stop = int(n / 2) + 1
    if stop > prime_list[-1]:
        stop1 = prime_list[-1] + 1 # Freezes the indexed prime check
        too_big = True
    else:
        stop1 = stop
        too_big = False
    index = 1   # None will be divisible by 2
    while index < len(prime_list):
        if n % prime_list[index] == 0:
            return False
        index += 1
    if not too_big:
        return True
    print "uh oh",
    too_high.append(n)
    print "-->", n, len(too_high)
    return False
    for trial in xrange(prime_list[-1] + 2, stop + 1, 2):
        if n % trial == 0:
            return False
    return True

def concat_pairs(prime_list, limit):
    # Builds a boolean, square, 2D array showing which prime pairs concatenat
    # to form primes.  The entries in each row/colomn match to:
    # 3, 7, 11, 13, 17, 19, 23, 29, 31...
    # ALSO makes a list of all concatenating primes (as tuples).
    for entry in prime_list:
        if entry > limit:
            max_index = prime_list.index(entry)
            break
    header = prime_list[:max_index]
    size = len(header)
    pair_grid = zeros((size, size), '?')
    #print "GRID"
    #print header
    #print pair_grid
    pair_list = []
    for index1 in xrange(size):
        for index2 in xrange(index1 + 1, size):
            a = int(str(header[index1]) + str(header[index2]))
            b = int(str(header[index2]) + str(header[index1]))
            if is_prime(a) and is_prime(b):
                #print a,b, '\t',
                pair_grid[index1][index2] = True
                pair_grid[index2][index1] = True
                pair_list += [(header[index1], header[index2])]
    #print "FINAL GRID"
    print "PAIR COUNT", pair_grid.sum() / 2, len(pair_list)
    return pair_grid, pair_list
    
def extend_till(set_size, pair_list):
    # Returns the list of 'set_size'-length concatening prime sets by
    # repeatedly calling on the extend_set function until complete.
    if set_size < 3:
        return pair_list
    counter = set_size - 2
    set_list = pair_list[:]
    while counter > 0:
        set_list = extender(set_list)
        print "Set of length", 1 - (counter - set_size), ":", len(set_list)
        counter -= 1
    return set_list
    
def extender(set_list):
    # Input is a list of n-length tuples of concatenating primes.
    # Output is the list of (n+1)-length tuples.
    # Uses global variables pair_grid and prime_list.
    new_sets = []
    for primes in set_list:
        indices = []
        for element in primes:
            indices += [prime_list.index(element)]
        indices.sort()
        for index in xrange(indices[-1] + 1, len(pair_grid)):
            truth = []
            for target in indices:
                truth += [pair_grid[target][index]]
            if False not in truth:
                added = tuple(list(primes) + [prime_list[index]])
                new_sets += [added]
    return new_sets

################################################################

prime_list = prime_import()
#print prime_list[:20]
prime_check = prime_check_maker(prime_list)
prime_list = [3] + prime_list[3:]   #removes 2 & 5 from prime_list

print "Time to load primes:", time.time() - t1

too_high = []

all_pairs = concat_pairs(prime_list, 10000) # Second variable sets limit!
pair_grid = all_pairs[0]
pair_list = all_pairs[1]
#print pair_list[-3:]

complete_sets = extend_till(5, pair_list)   # 1st variable = 5 for final
print complete_sets[:5]
total = 0
for item in list(complete_sets[0]):
	total += item

print total

print time.time() - t1

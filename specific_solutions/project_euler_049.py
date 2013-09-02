"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms
are prime, and, (ii) each of the 4-digit numbers are permutations of one
another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit increasing
sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?

"""

import time

def prime_list(set_limit):
    factors = [-1, -1] + [0] * (set_limit - 1) 
    for index in xrange(2, set_limit):  # skip 0, 1 & last number
        if factors[index] == 0:         # if index is prime
            multiple = 2 * index
            while multiple <= set_limit:
                factors[multiple] += 1  # for each multiple of the prime
                multiple += index
    #print factors
    #primes = []
    for index2 in xrange(len(factors)):
        if factors[index2] == 0:
            primes.append(index2)
    #return primes

def trim_primes(least):
    for index in xrange(len(primes) - 1, -1, -1):
        if primes[index] < least:
            primes.pop(0)

def digits(n):
    # returns SORTED list of digits for a number
    digs = []
    for digit in str(n):
        digs.append(int(digit))
    digs.sort()
    return digs

def prime_digitize():
    for item in primes:
        prime_digits.append((item, digits(item)))


set_limit = 9999 # input("What is the limit of primes to be generated: ")
t1 = time.time()
primes = []
prime_digits = []
prime_keys = []

prime_list(set_limit)
trim_primes(1000)
prime_digitize()
correct = []

###print len(prime_digits), len(primes)

for index1 in xrange(len(prime_digits)):
    target = prime_digits[index1][1]
    for index2 in xrange(index1 + 1, len(prime_digits)):
        if prime_digits[index2][1] == target:
            difference = primes[index2] - primes[index1]
            third = primes[index2] + difference
            if third in primes:
                index3 = primes.index(third)
                if prime_digits[index3][1] == target:
                    correct.append([primes[index1], primes[index2], \
                                   primes[index3]])

print correct
print time.time() - t1

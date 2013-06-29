"""
This is an attempt at a second prime number generator.  This code
also calculates the number of distinct prime factors of all numbers up to the
limit.
factors:  0 -> -1,  1 -> -1,  primes -> 0,
composites -> number of distinct non-zero prime factors,  i.e. 18 -> 2

Prime list up to 100,000 takes mac:0.44sec, oldpc:0.26, hp:0.36
Prime list up to 1,000,000 takes mac:3.99sec, oldpc:2.75, hp:2.89
Prime list up to 10,000,000 takes mac:45.7sec, oldpc:24.75, hp:29.05
Prime list up to 100,000,000 takes oldpc:5 min 5 sec, hp:?.

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


set_limit = input("What is the limit of primes to be generated: ")
t1 = time.time()
primes = []

prime_list(set_limit)
print len(primes),  # sum(primes)
print


outfile = open("prime_list_test.txt", "w")
for item in primes: #(10**7): #set max here... 10^7 ~ 5 MB
    outfile.write(str(item) + ',')
outfile.close()


print time.time() - t1

"""
It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.

9 = 7 + 2x1^(2)
15 = 7 + 2x2^(2)
21 = 3 + 2x3^(2)
25 = 7 + 2x3^(2)
27 = 19 + 2x2^(2)
33 = 31 + 2x1^(2)

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of
a prime and twice a square?

"""

import time

def prime_list(set_limit):
    #factors = [-1, -1] + [0] * (set_limit - 1) 
    for index in xrange(2, set_limit):  # skip 0, 1 & last number
        if factors[index] == 0:         # if index is prime
            multiple = 2 * index
            while multiple <= set_limit:
                factors[multiple] += 1  # for each multiple of the prime
                multiple += index
    #print factors
    #primes = []
    #for index2 in xrange(len(factors)):
    #    if factors[index2] == 0:
    #        primes.append(index2)
    #return primes

def goldbach_check(n):  # True if odd composite = some prime + 2n^2
    max_k = int((n / 2) ** 0.5)
    for k in xrange(1, max_k + 1):
        if factors[n - 2*k**2] == 0:
            #print n, "=", n - 2*k**2, "+ 2* " + str(k) + "^2"
            return True
    return False
    

set_limit = input("What is the limit of primes to be generated: ")
t1 = time.time()
factors = [-1, -1] + [0] * (set_limit - 1)
prime_list(set_limit)

#print goldbach_check(9), goldbach_check(25), goldbach_check(33)

index = 9           # the 1st odd composite
while True:
    if factors[index] > 0 and goldbach_check(index) is False:   # if composite
        print "answer", index
        break
    index += 2      # next odd no. - only odd composites need to be checked

print time.time() - t1



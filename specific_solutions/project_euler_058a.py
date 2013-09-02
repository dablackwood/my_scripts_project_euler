"""
Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers
lying along both diagonals are prime; that is, a ratio of 8/13 ~= 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?

CORRECT IN 33 SECONDS!!! (30 seconds using only is_prime,
rather than generating sieve)

"""

import time
t1 = time.time()

def is_prime(n):
    check = 2
    if n % check == 0 and n != 2:
        return False
    check = 3
    stop = int(n ** .5)
    while check <= stop:
        if n % check == 0:
            return False
        check = check + 2
    return True

def on_diagonal(n):
    return 4*n - 3

def primes_in_layer(n):
    # finds how many primes are in a given layer = n
    candidates = [(4*n*n - 10*n + 7), (4*n*n - 8*n + 5), (4*n*n - 6*n + 3)]
    okay = []
    for item in candidates:
        #if item < 10**6 and big_list[item] == 0:
        #    okay.append(item)
        #elif item > 10**6 and is_prime(item):
        #    okay.append(item)
        if is_prime(item):
            okay.append(item)
    #prime_trim(candidates[2])
    return len(okay)

def factorize(set_limit):
    factors = [-1, -1] + [0] * (set_limit - 1) 
    for index in xrange(2, set_limit):  # skip 0, 1 & last number
        if factors[index] == 0:         # if index is prime
            multiple = 2 * index
            while multiple <= set_limit:
                factors[multiple] += 1  # for each multiple of the prime
                multiple += index
    return factors

def add_a_layer(results):
    # this is used, rather than proportion
    previous = results[:]
    next = [previous[0] + 1, \
               previous[1] + primes_in_layer(previous[0] + 1), \
               on_diagonal(previous[0] + 1)]
    return next

set_limit = 10**6
#big_list = factorize(set_limit)

results = [2,3,5]
while float(results[1]) / results[2] >= 0.1:
    #print results
    results = add_a_layer(results)

print results
layers = results[0]
print layers, "layers"
print 2*layers - 1, "side length"

print time.time() - t1

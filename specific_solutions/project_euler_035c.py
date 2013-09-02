"""
The number, 197, is called a circular prime because all rotations of
the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""

import copy

def is_prime(n):
    check = 2  # input will always be odd
    if n % check == 0 and n != 2:
        return False
    check = 3
    stop = int(n ** .5)
    while check <= stop:
        if n % check == 0:
            return False
        check = check + 2
    return True

def number_grab(work):
    number = 0
    places = len(work)
    for digit in xrange(places):
        number += work[digit][0] * 10 ** (places - digit - 1)
    return number

def scroll(work):
    first_nine = work.index([9])
    if first_nine == 0: # all possible combinations have been used
        return False
    #for sublist in work:
    #    if len(sublist) == 1:
    #        
    else:
        del work[first_nine - 1][0]
        for index in xrange(first_nine, len(work)):
            work[index] = ok_digits[:]
        return work

def next(work):
    if len(work[-1]) >= 2: # there are still options for the final digit
        del work[-1][0] # delete the previously-used ones digit
        return work
    else:
        work = scroll(work)
        return work

def combinationize(list_of_lists):
    combos = []
    work = copy.deepcopy(list_of_lists)
    while work:
        combos.append(number_grab(work))
        work = next(work)
    return combos

ok_digits = [1, 3, 7, 9]
max_digits = 3  #test
min_digits = 2  #test
number = 0
scratch = []
circ_primes = []

for n_length in xrange(min_digits, max_digits + 1):
    for length in xrange(n_length):
        scratch.append(ok_digits[:])
    combinations = combinationize(scratch)[:]
    for item in combinations:
        if is_prime(item):
            print item, "is prime"
            # this is where the rotations will take place
            
    print combinations, len(combinations)
    scratch = []

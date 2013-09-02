"""
We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?

"""

import time
t1 = time.time()

def roll(scratch):
    for item in scratch[:]:
        item_copy = item
        for rotation in xrange(len(str(item))-1):
            item_copy = int(str(item_copy)[1:] + str(item_copy)[:1])
            #print "check", scratch, item_copy
            scratch.append(item_copy)
    return scratch

def permuter(n):
    if len(str(n)) == 2:
        return [n, 10 * (n % 10) + (n / 10)]
    else:
        scratch = []
        trunc_results = permuter(int(str(n)[1:]))
        for index in xrange(len(trunc_results)):
            scratch.append(int(str(n)[0] + str(trunc_results[index])))
        return roll(scratch)
    return

def startup():
    length = input("How many digits for the pandigital numbers (1-9): ")
    if not 1 <= length <= 9:
        startup()
    else:
        initial = seed(length)

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

primed = []
for item in permuter(7654321):
    if is_prime(item):
        primed.append(item)
primed.sort()
print len(primed), primed[-1]
print time.time() - t1

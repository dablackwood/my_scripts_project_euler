"""
A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number. For example, the sum of the proper
divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that
28 is a perfect number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is
called abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers
is 24. By mathematical analysis, it can be shown that all integers
greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as
the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.

"""

import math
import time
t1 = time.time()

def is_factor(n, k):
    if n % k != 0:
        return 0
    elif n == k * k:
        return 1
    else:
        return 2

def factor_sum(n):
    total = 1
    for trial in xrange(2, 1 + int(math.sqrt(n))):
        ans = is_factor(n, trial)
        if ans == 2:
            total = total + trial + (n / trial)
        elif ans == 1:
            total = total + trial
    return total

def status(n):
    divisors = factor_sum(n)
    if divisors > n:    #abundant
        return 2
    elif divisors == n:
        return 1    #perfect
    else:
        return False    #deficient

def include_multiples(n, limit):
    for mult in xrange(2 * n, limit, n):
        if mult not in abundants:
            abundants.append(mult)
    #abundants.sort()

def add_abundants(limit):
    for item in xrange(2, limit):
        if item not in abundants:
            check = status(item)
            if check == 2:
                abundants.append(item)
                include_multiples(item, limit)
            elif check == 1:
                include_multiples(item, limit)
            #abundants.sort()

def is_sum(n):
    index = 0
    while abundants[index] < 1 + (n / 2):
        #print "x", index, abundants[index]
        if status(n - abundants[index]) == 2:
            #print n, "=", entry, "+", n - entry
            return True
        if index < len(abundants) - 2:
            index += 1
        else:
            return False
    return False

abundants = []
tally = 0
maximum = 20162

add_abundants(1 + (maximum / 2))
abundants.sort()
print len(abundants), time.time() - t1

for test in xrange(1, maximum):
    if not is_sum(test):
        tally += test
    if test % 1000 == 0:
        print test, tally, time.time() - t1

print tally
print time.time() - t1


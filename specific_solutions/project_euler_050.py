"""
The prime 41, can be written as the sum of six consecutive primes:
41=2+3+5+7+11+13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?

"""

import time

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

def add_from_wheel(limit):
    for n in xrange(6, limit, 6):
        prime_list.append(n - 1)
        prime_list.append(n + 1)
    if prime_list[-1] > limit:
        del prime_list[-1]

def sieve(prime_list):
    # set the limit for numbers to test with
    max_tester = prime_list[-1] ** 0.5
    # start with 5, since all multiples of 2 & 3 were not included by the wheel
    tester_index = 2
    tested_index = 3
    while prime_list[tester_index] <= max_tester:
        # test all members of list to see if divisible by list[tester_index]
        # start with the item following tester_index
        tested_index = tester_index + 1
        while tested_index <= len(prime_list) - 1:
            if prime_list[tested_index] % prime_list[tester_index] == 0:
                del prime_list[tested_index]
            else:
                tested_index = tested_index + 1
        tester_index = tester_index + 1

# !!! get set_limit from the program that calls this one.

set_limit = 5000
t1 = time.time()

prime_list = [2,3]
add_from_wheel(set_limit)
sieve(prime_list)
#print prime_list
print len(prime_list),  sum(prime_list)

best = [0, 0]
for start in xrange(100):
    tally = 0
    index = start
    while True:
        tally += prime_list[index]
        if tally >= 10**6:
            tally -= prime_list[index]
            #print tally,
            break
        index += 1

    while True:
        if is_prime(tally):
            break
        else:
            index -= 1
            tally -= prime_list[index]
    #print index - start, tally
    if index - start > best[0]:
        best = [index - start, tally]

print best
print time.time() - t1

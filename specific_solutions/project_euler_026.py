"""
Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.

"""
import time
t1 = time.time()

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

def repeat_cycle(prime):
    k = 1
    while True:
        if ((10 ** k) - 1) % prime == 0:
            return k
        k += 1

#set_limit = input("What is the limit of primes to be generated: ")
set_limit = 1000
prime_list = [2,3]
add_from_wheel(set_limit)
sieve(prime_list)
prime_list.remove(2)
prime_list.remove(5)
maximum = 1
best = 1
for prime in prime_list:
    result = repeat_cycle(prime)
    if result > maximum:
        maximum = result
        best = prime

print best, maximum
print time.time() - t1

"""
The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from
left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


"""
import time

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

def check_truncations(n):
    if len(str(n)) > 2:
        if str(n)[0] != '2' and \
           str(n)[0] != '3' and \
           str(n)[0] != '5' and \
           str(n)[0] != '7':
            return False
        elif str(n)[-1] != '3' and \
             str(n)[-1] != '7':
            return False
    scratch = n
    length = len(str(n))
    while scratch > 9:
        scratch /= 10
        if scratch not in prime_list:
            return False
    while n > 9:
        n = int(str(n)[1:])
        if n not in prime_list:
            return False
    return True
        
#set_limit = input("What is the limit of primes to be generated: ")
t1 = time.time()

good2go = []

set_limit = 1000000
prime_list = [2, 3]
add_from_wheel(set_limit)
sieve(prime_list)
print "sieved", len(prime_list), time.time() - t1
roll = prime_list[4:]

for check in roll:
    if check_truncations(check):
        good2go.append(check)

print good2go, len(good2go)
print time.time() - t1

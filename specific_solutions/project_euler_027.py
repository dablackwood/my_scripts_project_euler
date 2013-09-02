"""
Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.

n^2 + an + b,
abs(a) < 1000,
abs(b) < 1000

"""

def is_prime(n):
    if n in prime_list:
        return True
    elif n < 0:
        return False
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
    n = 7
    while n <= limit:
        prime_list.append(n)
        n = n + 4
        prime_list.append(n)
        n = n + 2

def sieve(list):
    # set the limit for numbers to test with
    max_tester = list[len(list) - 1] ** 0.5
    # start with 5, since all multiples of 2 & 3 were not included by the wheel
    tester_index = 2
    tested_index = 3
    while list[tester_index] <= max_tester:
        # test all members of list to see if divisible by list[tester_index]
        # start with the item following tester_index
        tested_index = tester_index + 1
        while tested_index <= len(list) - 1:
            if list[tested_index] % list[tester_index] == 0:
                del list[tested_index]
            else:
                tested_index = tested_index + 1
        tester_index = tester_index + 1

def trim_end(limit, list):
    while limit < list[len(list) - 1]:
        del list[len(list) - 1]
# !!! get set_limit from the program that calls this one.

def evaluate(a, b, n):
    return (n ** 2) + (a * n) + b

def num_consecutive(a, b):
    n = 1
    while is_prime(evaluate(a, b, n)):
        #print a, b, n, evaluate(a, b, n), is_prime(evaluate(a, b, n))
        n += 1
    return n

prime_list = [2,3,5]
set_limit = 1000
add_from_wheel(set_limit)
trim_end(set_limit, prime_list)
sieve(prime_list)

b_list = prime_list[:]
best = (0, 0, 0)

for b in b_list:
    for a in xrange(-999, 1000):
        consecutive = num_consecutive(a, b)
        if consecutive > best[2]:
            best = (a, b, consecutive)

print best

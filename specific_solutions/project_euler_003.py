# What is the largest prime factor of the number 600851475143 ?


number_in_question = input("What number would you like to find the Largest Prime Factor of: ")
# 600851475143
set_limit = number_in_question / 2

# this is an attempt to make a prime number generator
# using the 6n +/- 1, with sieve of eratosthones

# the goal is to make a list of primes up to some number
# (another goal could be to generate up to the Kth prime)

prime_list = [2,3,5]



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
# set_limit = input("What is the limit of primes to be generated: ")

add_from_wheel(set_limit)
trim_end(set_limit, prime_list)
sieve(prime_list)
# print prime_list
# print len(prime_list)

def check_if_factor(number, list):
    while len(list) > 0:
        if number % list[len(list) - 1] == 0:
            print list[len(list) - 1], "is the largest prime factor of", number
            return list[len(list) - 1]
        del list[len(list) - 1]
    if len(list) == 0:
        print number, "is prime."
    

check_if_factor(number_in_question, prime_list)
        

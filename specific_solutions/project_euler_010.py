"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

prime_list = [2,3,5]

def add_from_wheel(limit):
    n = 7
    while n <= limit:
        prime_list.append(n)
        n = n + 4
        prime_list.append(n)
        n = n + 2


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

def trim_end(limit, list):
    while limit < list[len(list) - 1]:
        del list[len(list) - 1]

set_limit = input("What is the limit of primes to be generated: ")
#print set_limit
add_from_wheel(set_limit)
#print len(prime_list)
trim_end(set_limit, prime_list)
#print len(prime_list)

total = 0
for check in prime_list:
    if is_prime(check) is True:
        total = total + check

#print prime_list
print total

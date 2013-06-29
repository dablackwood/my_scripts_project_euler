"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

def is_prime(n):
    check = 2
    if n % check == 0:
        return False
    check = 3
    stop = int(n ** .5)
    while check <= stop:
        if n % check == 0:
            return False
        check = check + 2
    return True

print "This program finds the Nth prime."
nth = input("N: ")

count = 1
answer = 3
while count < nth:
    if is_prime(answer) is True:
        count = count + 1
    answer = answer + 2
print answer - 2

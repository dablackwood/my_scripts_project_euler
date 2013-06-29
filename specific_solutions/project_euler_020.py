"""
n! means n x (n - 1) x ... x 3 x 2 x 1

Find the sum of the digits in the number 100!

"""

def factorial(n):
    product = 1
    for item in xrange(n):
        product = product * (item + 1)
    return product

print "Find the sum of the digits of n!"
number = input("n: ")
big_number = factorial(number)
# print big_number

total = 0
while big_number > 0:
    last_digit = big_number - (10 * (big_number / 10))
    total = total + last_digit
    big_number = big_number / 10

print total

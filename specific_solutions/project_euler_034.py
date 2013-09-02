"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.



def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product

"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 6
    if n == 4:
        return 24
    if n == 5:
        return 120
    if n == 6:
        return 720
    if n == 7:
        return 5040
    if n == 8:
        return 40320
    if n == 9:
        return 362880
    
def digit_func(n):
    tally = 0
    for letter in str(n):
        tally += factorial(int(letter))
    return tally

for check in xrange(10, 2540161):
    if check == digit_func(check):
        print check


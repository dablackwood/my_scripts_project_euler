"""
The decimal number, 585 = 1001001001_(2) (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)

"""

def reverse(n):
    n = list(str(n))
    n.reverse()
    return n

def is_palindrome(n):
    return list(str(n)) == reverse(n)

def binary(n):
    if n < 0:
        return "-" + binary(n)
    output = ''
    while n != 0:
        if n % 2 == 0:
            bit = '0'
        else:
            bit = '1'
        output = bit + output
        n >>= 1
    return output or '0'

tally = 0
for check in xrange(1, 1000000, 2):
    if is_palindrome(check):
        if is_palindrome(binary(check)):
            #print check, binary(check)
            tally += check

print tally

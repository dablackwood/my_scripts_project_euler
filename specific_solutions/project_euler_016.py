"""
2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^(1000)?

"""

print "Find the sum of the digits of 2^N."
power = input("N: ")
big_number = 2 ** power

total = 0
while big_number > 0:
    last_digit = big_number - (10 * (big_number / 10))
    total = total + last_digit
    big_number = big_number / 10

print total

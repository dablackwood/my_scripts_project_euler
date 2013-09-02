"""
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1^(4) + 6^(4) + 3^(4) + 4^(4)
    8208 = 8^(4) + 2^(4) + 0^(4) + 8^(4)
    9474 = 9^(4) + 4^(4) + 7^(4) + 4^(4)

As 1 = 1^(4) is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.

"""

#for n in xrange(1, 20):
#    print n, (10 ** (n - 1)), (n * (9 ** 3))
total = 0
for check in xrange(32, 6 * 9 ** 5):
    #print
    copy = check
    tally = 0
    while copy > 0:
        digit = copy - (10 * (copy / 10))
        tally = tally + digit ** 5
        #print copy, digit, tally
        copy = copy / 10
    if check == tally:
        total = total + tally
        print tally
print total


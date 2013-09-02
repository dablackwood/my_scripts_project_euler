"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.

"""

import time
t1 = time.time()

def gcf(n, d):
    # for n < d...
    for check in xrange(n, 1, -1):
        if n % check == 0 and d % check == 0:
            return check
    return False

def cancellor(n, d):
    if str(n)[0] == str(d)[0]:
        return (n % 10, d % 10)
    elif str(n)[0] == str(d)[1]:
        return (n % 10, d / 10)
    elif str(n)[1] == str(d)[0]:
        return (n / 10, d % 10)
    elif str(n)[1] == str(d)[1]:
        return (n / 10, d / 10)
    else:
        return False

results = []
for n in xrange(11, 100):
    for d in xrange(11, 100):
        if n < d and \
           '0' not in str(n) and \
           '0' not in str(d) and \
           gcf(n, d) and \
           cancellor(n, d) and \
           n / float(d) == cancellor(n, d)[0] / float(cancellor(n, d)[1]):
             results.append((n, d))
print results



print time.time() - t1

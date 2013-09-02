"""
Considering natural numbers of the form, a^b, where a and b < 100,
what is the maximum digital sum?

"""

import time
t1 = time.time()

def digit_sum(n):
    tally = 0
    for digit in str(n):
        tally += int(digit)
    return tally

max_sum = 0
for a in xrange(1, 100):
    if a % 10 != 0:
        for b in xrange(1, 100):
            tally = digit_sum(a**b)
            if tally > max_sum:
                max_sum = tally

print max_sum

print time.time() - t1

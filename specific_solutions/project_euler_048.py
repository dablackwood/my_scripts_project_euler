"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series,
1^1 + 2^2 + 3^3 + ... + 1000^1000.

"""

import time
t1 = time.time()

def n_to_the_n(n):
    return n ** n
def truncate(n):
    return n % (10 ** 10)

total = 0
for k in xrange(1, 1001):
    total = total + truncate(n_to_the_n(k))
truncate(total)
print total

print time.time() - t1


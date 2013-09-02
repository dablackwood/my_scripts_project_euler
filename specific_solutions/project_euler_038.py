"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?

"""

import time
t1 = time.time()

def is_pandigital(n):
    if len(str(n)) != 9:
        return False
    else:
        listed = list(str(n))
        listed.sort()
        if listed != ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return False
    return True

def procedure(n):
    #print n,
    generated = str(n)
    k = 1
    while len(generated) < 9:
        k += 1
        generated = generated + str(n * k)
        #print generated,
    generated = int(generated)
    if is_pandigital(generated):
        correct.append(generated)
        #print "Found", generated
    else:
        #print
        return False

correct = []
for trial in xrange(1, 10**4):
    procedure(trial)

correct.sort()
print len(correct), correct[-1]

print time.time() - t1

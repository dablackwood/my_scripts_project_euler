"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up
of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d_(1) be the 1^(st) digit, d_(2) be the 2^(nd) digit, and so on. In
this way, we note the following:

    * d_(2)d_(3)d_(4)=406 is divisible by 2
    * d_(3)d_(4)d_(5)=063 is divisible by 3
    * d_(4)d_(5)d_(6)=635 is divisible by 5
    * d_(5)d_(6)d_(7)=357 is divisible by 7
    * d_(6)d_(7)d_(8)=572 is divisible by 11
    * d_(7)d_(8)d_(9)=728 is divisible by 13
    * d_(8)d_(9)d_(10)=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

"""

import time
t1 = time.time()

def is_pandigital(n):
    if len(str(n)) != 10:
        return False
    else:
        listed = list(str(n))
        listed.sort()
        if listed != ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return False
    return True

def evaluate(n):
    if int(str(n)[2:5]) % 3 != 0 or \
       int(str(n)[3:6]) % 5 != 0 or \
       int(str(n)[5:8]) % 11 != 0 or \
       int(str(n)[6:9]) % 13 != 0:
        return False
    else:
        return True

def no_repeats(n):
    for digit in str(n):
        if str(n).count(digit) != 1:
            #print "repeat", n,
            return False
    #print "no repeats", n,
    return True

#print no_repeats(1234567890), no_repeats(12345660987)

correct = []
for last_3 in xrange(17, 1000, 17):
    trial = last_3
    #print trial, len(correct),
    if no_repeats(trial):
        for mid_3 in xrange(14, 1000, 7):
            trial += (mid_3 * 10**3)
            #print trial, len(correct),
            if no_repeats(trial):
                for first_3 in xrange(12, 1000, 2):
                    trial += (first_3 * 10**6)
                    #print trial, len(correct),
                    if no_repeats(trial):
                        for initial in xrange(1, 10):
                            trial += (initial * 10**9)
                            if is_pandigital(trial) and evaluate(trial):
                                correct.append(trial)
                                #print "Found", trial
                            trial = trial % 10**9
                    trial = trial % 10**6
            trial = trial % 10**3

print sum(correct)
print time.time() - t1

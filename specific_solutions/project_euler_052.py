"""
It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.

"""

def digit_list(n):
    digit_list = list(str(n))
    for index in xrange(len(digit_list)):
        digit_list[index] = int(digit_list[index])
    return digit_list

def has_same_digits(n, k):
    n_list = digit_list(n)[:]
    k_list = digit_list(k)[:]
    for digit in n_list:
        #print "n", n_list
        if digit in k_list:
            #print "k", k_list
            k_list.remove(digit)
        else:
            return False
    return True

solved = False
length = 3
while solved != True:
    for check in xrange(3 * 10 ** (length - 1), (10 ** length) - 1, 6):
        #print check,
        x = check / 6
        if has_same_digits(2 * x, 3 * x) and \
           has_same_digits(2 * x, 4 * x) and \
           has_same_digits(2 * x, 5 * x) and \
           has_same_digits(2 * x, 6 * x):
            print "Answer:", x
            print 2 * x
            print 3 * x
            print 4 * x
            print 5 * x
            print 6 * x
            solved = True
            break
    length += 1

#print has_same_digits(100, 150)

"""
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

"""

import time
t1 = time.time()

def is_palindrome(n):
    return n == reversal(n)

def reversal(n):
    reverse = ""
    for digit in str(n):
        reverse = digit + reverse
    return int(reverse)

def iterate(n):
    return n + reversal(n)

def lychrel_chain(n):
    #print n,
    chain = []
    for iterations in xrange(50):
        #print n,
        if n in lychrels:
            #print "lychrel reached"
            lychrels.extend(chain)
            return
        elif n in non_lychrels:
            #print "non_lychrel reached"
            non_lychrels.extend(chain)
            return
        elif iterations > 0 and is_palindrome(n):
            #print "non_lychrel found"
            non_lychrels.extend(chain)
            return
        else:
            chain.append(n)
        n = iterate(n)
    lychrels.extend(chain)
    #print "lychrel found!!!!!", chain[0]

def list_filter(in_list):
    in_list.sort()
    for item in in_list[:]:
        if in_list.count(item) > 1 or item > 10000:
            in_list.remove(item)



lychrels = []
non_lychrels = []

#lychrel_chain(4994)

#print is_palindrome(1234321), is_palindrome(1234)
#print reversal(1234)
#print iterate(47)
for trial in xrange(1, 10000):
    lychrel_chain(trial)
list_filter(non_lychrels)
list_filter(lychrels)
print len(non_lychrels)#, non_lychrels
print len(lychrels)
#print 4994 in lychrels, 4994 in non_lychrels
print time.time() - t1

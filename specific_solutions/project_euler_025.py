"""
The 12th term, F(12), is the first term to contain three digits.
What is the first term in the Fibonacci sequence to contain 1000 digits?

"""

import time
t1 = time.time()

def count(n):
    digits = 1
    while 10 ** digits < n:
        digits = digits + 1
    return digits

def abs_value(n):
    if n < 0:
        n = -n
    return n

def Fibonacci(x):
    a = 1
    b = 1
    for c in xrange(x - 1):
        n = a + b
        a = b
        b = n
    return a

def evaluation(guess):
    return count(Fibonacci(guess))

def check(item_eval):    
    if item_eval == sought:
        return 1
    else:        
        return 0

def next_guess(prev_guess, prev_eval):
    next = (prev_guess * sought) // prev_eval
    return next
    
guesses = []

sought = 1000
w_a_g = 5000
current_guess = w_a_g
eureka = 0
while eureka == 0:
    item_eval = evaluation(current_guess)
    guesses.append([current_guess, item_eval])
    guesses.sort()
    eureka = check(item_eval)
    print current_guess, guesses, eureka
    if eureka == 0:
        current_guess = next_guess(current_guess, item_eval)
    
for span in xrange(-5, 6):
    print current_guess + span, count(Fibonacci(current_guess + span)) 

print time.time() - t1


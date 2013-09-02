"""
The nth term of the sequence of triangle numbers is given by,
t(n) = .5*n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19+11+25 = 55 = t(10).
If the word value is a triangle number then we shall call the word a
triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?

"""
import time
t1 = time.time()

def inv_tri(k):
    under = ((8 * k) + 1) ** 0.5
    if int(under) != under:
        return False
    answer = (under - 1) / 2
    if int(answer) != answer:
        return False
    else:
        return int(answer)

def add_triangular(minimum):
    while triangular[-1] < minimum:
        triangular.append(1 + triangular[-1] + inv_tri(triangular[-1]))

def is_triangular(n):
    if n > triangular[-1]:
        add_triangular(n)
    if n in triangular:
        return True
    else:
        return False

def numerify(word):
    count = 0
    for letter in word:
        count += (ord(letter) - 64)
    return count
    
triangular = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
words = []
tally = 0

in_file = open("project_euler_042_words.txt", "r")
words = in_file.read()
print len(words)
words = words[1:]
words = words[:-1]
words = words.split('","')
print len(words)

for check in words:
    if is_triangular(numerify(check)):
        tally += 1

print tally
print time.time() - t1

"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text
file containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a
name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938x53 = 49714.

What is the total of all the name scores in the file?


"""

import time
t1 = time.time()

def letter_value(n):
    return ord(n) - 64

def word_sum(n):
    total = 0
    for letter in n:
        total += letter_value(letter)
    return total

def word_score(name, position):
    return word_sum(name) * (position + 1)

big_list = []
in_file = open("project_euler_022_names.txt", "r")
big_list = in_file.read()
big_list = big_list[1:]
big_list = big_list[:-1]
big_list = big_list.split('","')
big_list.sort()

big_total = 0
for item in xrange(0, len(big_list)):
    big_total += word_score(big_list[item], item)
    #print word_sum(big_list[item])

print big_total
#print big_list[:2]
in_file.close()
print time.time() - t1

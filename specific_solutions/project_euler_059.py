"""
Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to
ASCII, then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key
on the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and
without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password
key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using cipher1.txt
(right click and 'Save Link/Target As...'), a file containing the
encrypted ASCII codes, and the knowledge that the plain text must
contain common English words, decrypt the message and find the sum of the
ASCII values in the original text.

"""

import time
t1 = time.time()

def bin(x):
    d = {0:'000', 1:'001', 2:'010', 3:'011', \
         4:'100', 5:'101', 6:'110', 7:'111'}
    return ''.join([d[int(dig)] for dig in oct(x)])

def stringify(wordlist):
    strung = ''
    for index in xrange(len(wordlist)):
        strung += chr(int(wordlist[index]))
    return strung

def check_english(string):
    #print string[:20]
    if 'The' in string and 'Gospel' in string:# or 'you' in string:
        print string[:40]
        proceed = input("Does this look right? (1=yes, 2=no) ")
        if proceed == 1:
            return True
        elif proceed == 2:
            return False
        else:
            return check_english(string)
    else:
        return False

def decrypt(numbers, password):
    copied = []
    for character in xrange(len(numbers)):
        key = password[character % 3]
        copied.append(str(int(numbers[character]) ^ key))
    #print "--->", copied[:20]
    return stringify(copied)

def text_sum(text):
    tally = 0
    for character in text:
        tally += ord(character)
    return tally

in_file = open('project_euler_059_cipher1.txt', 'r')
text = in_file.read()
text = text[:-1]
numbers = text.split(',')
#print len(numbers)
#print text_sum('abc')

quick = decrypt(numbers, (103, 111, 100))
print quick

"""

for key1 in xrange(97, 123):
    for key2 in xrange(122, 96, -1):
        for key3 in xrange(97, 123):
            password = (key1, key2, key3)
            # print password
            decrypted = decrypt(numbers, password)
            if check_english(decrypted):
                print password
                print text_sum(decrypted)
                print decrypted
                break
                
"""
#print strung

print time.time() - t1

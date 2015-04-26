# Find letters in words that are the same distance apart in the word as they are in the alphabet

import sys

sentence = sys.stdin.readline()

def my_ord(letter):
    if ord(letter) > ord('X'):
        return ord(letter) - 2
    elif ord(letter) > ord('J'):
        return ord(letter) - 1
    else:
        return ord(letter)

for word in sentence.split(" "):
    for position1, letter1 in enumerate(word):
        position1 += 1
        for position2, letter2 in enumerate(word):
            position2 += 1
            if position1 != position2 and my_ord(letter2) - my_ord(letter1) == position2 - position1:
                print (word, position1, position2)

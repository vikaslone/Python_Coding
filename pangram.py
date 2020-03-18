# Write a Python function to check whether a string is pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"


def pangram_check(s):
    set1 = set(s.replace(' ', '').lower())
    # print(set1)
    cnt = 0
    for i in set1:
        cnt += 1
    return cnt == 26


print(pangram_check('The quick brown fox jumps over the lazy dog'))

print(pangram_check('The quick brown fox'))


# Alternate Method

import string


def pangram_check(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())


print(pangram_check('The quick brown fox jumps over the lazy dog'))

print(pangram_check('The quick brown fox'))

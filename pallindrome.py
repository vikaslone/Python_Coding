# Write a Python function that checks whether a passed in string is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.


def pallindrome_check(inp):
    rev_inp = inp[::-1]
    return inp == rev_inp


print(pallindrome_check('helle'))

# Write a function that checks whether a number is in a given range (inclusive of high and low)


def range_check(num, low, high):
    return low <= num <= high


print(range_check(5, 2, 7))
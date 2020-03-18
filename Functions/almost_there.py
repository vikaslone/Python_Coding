# Given an integer n, return True if n is within 10 of either 100 or 200


def number_proximity(num1):
    return 90 <= num1 <= 110 or 190 <= num1 <= 210


print(number_proximity(94))


# Alternate code


def number_proximity_1(num1):
    return (abs(100-num1) <= 10) or (abs(200-num1) <= 10)


print(number_proximity_1(199))
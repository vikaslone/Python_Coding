# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.


def up_low(str1):
    low_cnt = 0
    up_cnt = 0

    for i in str1:
        # print(i, ' ->', ord(i))
        if ord(i) in range(97, 123):
            low_cnt += 1
        elif ord(i) in range(65, 91):
            up_cnt += 1
        else:
            continue

    return up_cnt, low_cnt


cnt_up, cnt_low = up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
print('count of lower case -> ', cnt_up, 'count of upper case -> ', cnt_low)


# Alternate code

def up_low(str1):
    d = {"upper": 0, "lower": 0}

    for i in str1:
        if i.isupper():
            d["upper"] += 1
        elif i.islower():
            d["lower"] += 1
        else:
            continue

    return d["upper"], d["lower"]


cnt_up, cnt_low = up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
print('count of lower case -> ', cnt_up, 'count of upper case -> ', cnt_low)

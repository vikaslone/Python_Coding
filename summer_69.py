# SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9).
# Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14


def summer_69(int_arr):
    out_sum = 0
    idx_6 = -1
    idx_9 = -1
    if 6 in int_arr:
        idx_6 = int_arr.index(6)
    if 9 in int_arr:
        idx_9 = int_arr.index(9)

    for i in range(0, len(int_arr)):
        if idx_6 >= 0 and (idx_6 <= i <= idx_9):
            continue
        else:
            out_sum += int_arr[i]
    return out_sum


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere


def has_33(list1):
    # print(list1)
    list2 = list1
    # print(list2)
    out = 0
    # print('out -> ', out)
    for i in range(0, len(list1)-1):
        # print('i -> ', i)
        # print('list1[i] -> ', list1[i])
        # print('list2[i+1] -> ', list2[i+1])
        if list1[i] == 3 and list2[i+1] == 3:
            out = 1
            break
        else:
            continue
    if out == 0:
        return False
    else:
        return True


print(has_33([1, 2, 3]))

print(has_33([1, 3, 3]))


# Better Code


def has_33_alt(nums):
    for i in range(0, len(nums)-1):
        if nums[i: i+2] == [3, 3]:
            return True
        else:
            return False


print(has_33_alt([1, 2, 3]))

print(has_33_alt([1, 3, 3]))


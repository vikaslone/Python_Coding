# Write a Python function that takes a list and returns a new list with unique elements of the first list.


def uniq(lst1):
    out_lst = []

    for i in lst1:
        if i in out_lst:
            continue
        else:
            out_lst.append(i)

    return out_lst


print(uniq([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))
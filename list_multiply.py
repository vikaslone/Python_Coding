# Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24


def list_multiply(lst1):
    mul = 1
    for i in lst1:
        mul = mul*i
    return mul


print(list_multiply([1, 2, 3, 4, -5]))

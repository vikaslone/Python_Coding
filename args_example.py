def sum_of_nums(*args):
	print(args)
	return sum(args)

a = sum_of_nums(1,2,3,4,5)
print(a)
b = sum_of_nums(1,2,3)
print(b)
def myfunc(*args):
	y = [x for x in args if x%2 == 0]
	return y

a = list(range(10))
print(a)

y = [x for x in a if x%2 == 0]
print(y)

z = myfunc(1,2,3,4,5,6)
print(z)
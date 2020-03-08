idx = 1
str1 = []
for i in 'hello':
	if idx%2 == 0:
		str1.append(i.upper())
	else:
		str1.append(i.lower())
	idx+=1
	print(idx)

print(''.join(str1))

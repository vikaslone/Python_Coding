# Write a function that capitalizes the first and fourth letters of a name
# Option 1
print('Option 1')

def str_capitalise(str1):
	str2 = list(str1)
	print(str2)
	str3 = []
	for i in range(0,len(str2)):
		if i in (0,3):
			str3.append(str2[i].upper())
		else:
			str3.append(str2[i])

	return ''.join(str3)

print(str_capitalise('oldmcdonald'))

# Option 2

print('Option 2')

def str_capitalise2(str1):
	if len(str1)<4:
		return 'Supplied string too short'
	else:
		return str1[:3].capitalize()+str1[3:].capitalize()

print(str_capitalise2('oldmcdonald'))
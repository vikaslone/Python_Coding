'''
Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater 
if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
'''

def lesser_of_two_numbers(num1, num2):
	if num1%2 ==0 and num2%2 == 0:
		if num1>num2:
			output_num = num2
		else:
			output_num = num1
	else:
		if num1>num2:
			output_num = num1
		else:
			output_num = num2

	return output_num

def lesser_of_two_numbers_v2(num1, num2):
	if num1%2 ==0 and num2%2 == 0:
		return min(num1,num2)
	else:
		return max(num1,num2)

print('\nVersion 1 results')

print(lesser_of_two_numbers(2,4))
print(lesser_of_two_numbers(1,4))
print(lesser_of_two_numbers(5,7))

print('\nVersion 2 results')

print(lesser_of_two_numbers_v2(2,4))
print(lesser_of_two_numbers_v2(1,4))
print(lesser_of_two_numbers_v2(5,7))

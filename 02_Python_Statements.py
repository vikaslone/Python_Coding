# Complete  Pythin BootCamp -> 02-Python Statements -> 07-Statement Assessment Test

#1 Use for, .split(), and if to create a Statement that will print out words that start with 's':

#st = input('Enter the string of your choice: ')
print('#1 Use for, .split(), and if to create a Statement that will print out words that start with s: \n')

st = 'Print only the words that start with s in this sentence \n'
print (st)

st1 = st.split()

for words in st1:
	if words[0] == 's':
		print(words)

#2 Use range() to print all the even numbers from 0 to 10.
print('\n#2 Use range() to print all the even numbers from 0 to 10. \n')

print(list(range(0,11,2)))
'''
Alternate code

for num in range(11):
	if num % 2 == 0:
		print(num)
'''

#3 Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

print('\n#3 Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.\n')

list1 = list(range(1,51))
print('list1 -> ',list1, '\n')

list2 = [x for x in list1 if x % 3 == 0]
print('Output -> ',list2)

#4 Go through the string below and if the length of a word is even print "even!"

print('\n#4 Go through the string below and if the length of a word is even print "even!"\n')

st = 'Print every word in this sentence that has an even number of letters\n'
print(st)

for word in st.split():
	if len(word) % 2 == 0:
		print(word, '<-- has even length')

#5 Write a program that prints the integers from 1 to 100. 
#  But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
#  For numbers which are multiples of both three and five print "FizzBuzz".		
print ('\n#5 Write a program that prints the integers from 1 to 100.',
       'But for multiples of three print "Fizz" instead of the number, and for the multiples of five print '"'Buzz'"'.',
       'For numbers which are multiples of both three and five print '"'FizzBuzz'"'.\n')

for num in range(1,101):
	if num % 3 == 0 and num % 5 == 0:
		print('FizzBuzz')
	elif num % 3 == 0:
		print('Fizz')
	elif num % 5 == 0:
		print('Buzz')
	else:
		print(num)

#6 List Comprehension to create a list of the first letters of every word in the string below:
print('List Comprehension to create a list of the first letters of every word in the string below:')

st = 'Create a list of the first letters of every word in this string'
print(st)

print(list(x[0] for x in st.split()))
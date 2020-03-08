# Write a function takes a two-word string and returns True if both words begin with same letter

def match_first_chars(word1):
	str1 = word1.split()
	print(str1)
	print(str1[0])
	print(str1[1])
	return str1[0][0] == str1[1][0]

print(match_first_chars('Sam Saturn'))
print(match_first_chars('Sam saturn'))

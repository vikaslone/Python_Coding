# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def check_twenty(int1,int2):
	return int1 == 20 or int2 == 20 or int1+int2==20

print(check_twenty(20,1))
print(check_twenty(2,1))
print(check_twenty(2,18))
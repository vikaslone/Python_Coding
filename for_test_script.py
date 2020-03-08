my_list = []
list_sum_all = 0
list_sum_even = 0
list_sum_odd = 0

for i in range(5):
	my_list.append(i)

print('my_list: ', my_list, '\n')

for num in my_list:
	list_sum_all += num
	if num % 2 == 0:
	   list_sum_even += num
	else:
	   list_sum_odd += num	

print('list_sum_all: ', list_sum_all)
print('list_sum_even: ',list_sum_even)
print('list_sum_odd: ', list_sum_odd, '\n')
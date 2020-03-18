def myfunc(**kwargs):
	print(kwargs)
	if 'fruit' in kwargs:
		print('I love {}'.format(kwargs['fruit']))
	elif 'veggie' in kwargs:
		print('I hate {}'.format(kwargs['veggie']))
	else:
		print('I love {}'.format(kwargs['juice']))


myfunc(fruit='Mango',veggie='Lettuce')
myfunc(fruit='Apple')
myfunc(veggie='Beets')
myfunc(juice='Orange')
myfunc(sweet='Kiwi',green='Cabbage',juice='Sapota')
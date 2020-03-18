dict_1 = {'k1':1,'k2':2,'k3':3}

# Below will only print the keys but not values
for d in dict_1:
   print(d)

# Below will print both key and value, called dictionary unapcking
# (key, val) can also be written as key, val
for (key, val) in dict_1.items():
   print(key)
   print(val)
   
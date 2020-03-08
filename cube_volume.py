# Calculate volume of a sphere given its radius


import math as m


def vol(rad):
    return (4.0/3)*m.pi*(rad ** 3)


print(vol(2))
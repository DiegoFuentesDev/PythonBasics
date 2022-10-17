from cmath import pi


radius = float(input('Type the radius of the sphere in cm: '))

volume = (4/3) * pi * (radius**3)

print('Volume: ' + str(volume) + " cm3")
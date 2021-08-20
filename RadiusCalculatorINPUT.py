# formula = 4/3πr3
# print_volume(radius) will now be defined and take on an argument and print volume of a sphere
def print_volume(radius):
    pi = 3.1415926535897932
    result = 4 / 3 * pi * (radius * radius * radius)
    return result


# print_volume function will now be called three times with different values for radius
# \n use to tidy up the output display and text is added to give the output a smoother feel
print('\nWhen the radius is', '11,', 'the volume of the sphere equals', print_volume(11))
print('When the radius is', '22,', 'the volume of the sphere equals', print_volume(22))
print('When the radius is', '33,', 'the volume of the sphere equals', print_volume(33))


# option to enter own radius value to work out the volume of a sphere
pi = 3.1415926535897932
radius = float(input('\nInput a radius value to find the volume of a sphere (optional): '))
volume = 4 / 3 * pi * (radius * radius * radius)

print("\nWhen the radius = %.3f" % radius)
print("Volume of a Sphere equals = %.5f" % volume)

# after user has entered their own optional radius value, user is then offered to enter a new value
# restart has been used to identify the question presented to user followed by an if statement
# if user inputs ‘y’ this will then lead the user to the enter another value, which is interpreted as a float that is up to three-five decimal places
# if restart == ‘y’ it then gives the program permission to carry out the ongoing code

restart = input('\nDo you wish to enter another value? [y/n]: ')
if restart == 'y':
    pi = 3.1415926535897932
    radius = float(input('Enter new radius value: '))
    volume = 4 / 3 * pi * (radius * radius * radius)
    
print("\n When the radius = %.3f" % radius)
print("Volume of a Sphere = %.5f" % volume)

    

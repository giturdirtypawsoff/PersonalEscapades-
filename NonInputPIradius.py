# formula = 4/3πr3
def print_volume(radius):
    pi = 3.1415926535897932
    result = 4 / 3 * pi * (radius * radius * radius)
    return result


# Call your print_volume function three times with different values for radius.
print('Volume of the sphere equals', print_volume(1))
print('Volume of the sphere equals', print_volume(2))
print('Volume of the sphere equals', print_volume(3))

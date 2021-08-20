def my_function():  #
    print('Hello')


my_function()
# Example of defining a function and calling it

my_function()


def my_function(group, name):
    print('Hello, ' + group + ' ' + name)


my_function('Computer Science', 'Classmates')


# Name & Group are parameters
# I have used these to define the function

def arbituary_argument(*code_breakdown):  # arbitrary argument
    print('My greeting was ' + code_breakdown[0])
    print('My class was ' + code_breakdown[1])
    print('I was saying "Hello" to ' + code_breakdown[2])
    print('1+2+3='+ code_breakdown[3])


arbituary_argument('Hello', 'Computer Science', 'Classmates', '6')


# Here is an example of a parameter that has been assigned an argument
# "Answer' is a variable

def local_variable():
    global x
    x = 'local variables are used inside of functions'

local_variable()
print('It is called a local variable. ' + x)

y = 'variable'
def globl_variable():
    print('Here is another example. "Y" is a global '+y)
globl_variable()

# function is defined to print one new line assigned as '.'for visual aid
def new_line(): 
    print('.')

# function is defined to print 3 new lines
def three_lines():  
    new_line()
    new_line()
    new_line()

# function must refer to nested functions and is defined to print 9 new lines   
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

# function is defined to print 25 lines by combining all previous nested functions
def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()
    
# main section of program will now call functions

# console must print placeholder and run nine_lines() function
print("Printing nine_lines()")
nine_lines()
# console must print placeholder and run clear_screen() function
print("Calling clear_screen()")
clear_screen()
# results will now display 9 lines and 25 lines with placeholders 

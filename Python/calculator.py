import math

"""
PseudoCode:
    If interactive (with UI):
        Buttons laid out in same style as 10-key on keyboard.
    If terminal-only:
        Request how many inputs it will need.
        Request what function they are needing between each input.
        Put each input in an array/list and do the same for the operands.
        Perform calculation by putting the inputs and operands in order.

Will do terminal-only first
"""

"""
##With if/elif statements

i = int(1)
while i < inputs:
    if i == 1:
        first = input(str(i)+"st number: ")
        i = i + 1
    elif i == 2:
        second = input(str(i) + "nd number: ")
        i = i + 1
    elif i == 3:
        third = input(str(i) + "rd number: ")
        i = i + 1
    else:
        i = input(str(i) + "th number: ")
        i = i + 1
"""

"""
##With Lists

inputs = int(input("How many are you needing? "))
print(inputs)
values = []
operands = []

i = 0
while i < int(inputs):
    if i  == 0:
        values.append(int(input("What is the First number? ")))
        print(values[i])
        print(i)
        i =+ 1
    elif i == 1: ##BUG: Repeats This section; Jumps from 0 to 2.
        values.append(int(input("What is the Second number? ")))
        print(values[i])
        i = i + 1
        print(i) 
    else:
        print(values)
"""

##With Dictionary
print("""
1. add
2. sub
3. multi
4. div
""")
#Modify code to allow for either an integer or a string input.
#Add in error handling for invalid inputs. 

inputs = input("What function are you needing to perform? ")
inputs = inputs.lower


f_num = int(input("First number: "))
s_num = int(input("Second number: "))

def add(f_num, s_num):
    __doc__ = "Add two numbers"
    return f_num + s_num
def sub(f_num, s_num):
    __doc__ = "Subtract two numbers"
    return f_num - s_num
def multi(f_num, s_num):
    __doc__ = "Multiply two numbers"
    return f_num * s_num
def div(f_num, s_num):
    __doc__ = "Divide two numbers showing only a whole number"
    return f_num // s_num

mathChoices = {
    "add": add(f_num, s_num),
    "sub": sub(f_num, s_num),
    "multi": multi(f_num, s_num),
    "div": div(f_num, s_num)
}
print(mathChoices[inputs])
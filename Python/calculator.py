import math
from os import waitstatus_to_exitcode as wait

##With Dictionary
print("""
1. add
2. sub
3. multi
4. div
""")

inputs = input("What function are you needing to perform? ")
inputs = inputs.lower()

### Defining, unneccessary, functions
def add(f_num, s_num):
    __doc__ = "Sum two numbers"
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

if inputs == "1" or inputs == "2" or inputs == "3" or inputs == "4":
    wait(2)
    inputs = int(inputs)
    f_num = int(input("First number: "))
    s_num = int(input("Second number: "))

    mathChoices = {
        1: add(f_num, s_num),
        2: sub(f_num, s_num),
        3: multi(f_num, s_num),
        4: div(f_num, s_num)
    }

    print(mathChoices[inputs])
elif inputs == "add" or inputs == "sub" or inputs == "multi" or inputs == "div":
    wait(2)
    f_num = int(input("First number: "))
    s_num = int(input("Second number: "))

    mathChoices = {
        "add": add(f_num, s_num),
        "sub": sub(f_num, s_num),
        "multi": multi(f_num, s_num),
        "div": div(f_num, s_num)
    }
    print(mathChoices[inputs])
else:
    wait(5)
    print("\nYou have not provided a valid input, please run the program, again and enter the name of the function or its associated number.")
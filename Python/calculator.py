import math

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
inputs = inputs.lower()

### Defining functions
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

if inputs == "add" or "sub" or "multi" or "div":
    
    f_num = int(input("First number: "))
    s_num = int(input("Second number: "))

    mathChoices = {
        "add": add(f_num, s_num),
        "sub": sub(f_num, s_num),
        "multi": multi(f_num, s_num),
        "div": div(f_num, s_num)
    }
    print(mathChoices[inputs])

elif inputs ==  1 or 2 or 3 or 4:
    inputs = int(inputs)
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
    print("You have not provided a valid input, please run the program, again.")
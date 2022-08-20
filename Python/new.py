"""
#Print
print("Hello World")

#Variables
age = 24
print("My age is", str(age))
price = 20.01
first_name = "Richard"

#Exercise
fName = "John"
lName = "Smith"
age =   "20"
prevPatient = False

#Receiving input
name = input("What is your name? ")
print("Hello " + name)
"""
"""
#Type Conversion
ccNumber = input("Enter your credit card number: ")
ccNumberdif = 1000000000000000 - int(ccNumber)
print("Your Credit Card number is", ccNumberdif, "away from one quadrillion.")

first = input("First number: ")
second = input("Second number: ")
sum = float(first) + float(second)
print("Sum: " + str(sum))
"""
"""
#Strings
course = "Python for Beginners"

#Arithmetic Operators
x = int(0)
while x < 1001:
    x += 1
    print(x)
    
print("end")
y = 10 + 3 * 2
print(y)

#Logical Operators
price = 5
print(price > 10)

and (both)
or (at leath one)
not (opposite)
"""
"""
#If Statements
temperature = int(input("What's the temperature? "))

if temperature > 80:
    print("It's hot.")
    print("Drink water, bitch.")
elif temperature > 72: # (72, 80]
    print("It's nice.")
elif temperature > 64: # (64, 72]
    print("It's chilly.")
else:
    print("It's too cold. Stay inside.")
print("end")

#Exercise_Weight Conversion

weight = float(input("What is your weight? "))
unit = str(input("In what unit of weight are you using? "))
conversion = str(input("What unit of weight are you needing this converted to? (Kg, lb): "))
convweight = ()

if unit == "Kg" and conversion == "lb":
    convweight = weight * 2.2046226218
    print("The converted weight equals: " + str(convweight))
elif unit == "lb" and conversion == "Kg":
    convweight = weight / 2.2046226218
    print("The converted weight equals: " + str(convweight))
else:
    print("\nYou don't need this calculator.\nGoodbye")
"""
"""
#While Loops
#i = 0
#while i < 10:
#    i += 1
#    print(i * "/\\")

#Lists
names = ["Richie", "Madison", "Charlie", "Luna", "Aurora"]
namesNum = len(names)
i = 0
#print(names[i])
while i < namesNum:
    print(names[i-1])
    i += 1
"""
"""
##Methods
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers.insert(9, 777)
print(numbers)
numbers.remove(3)
print(numbers)
numbers.clear
print(numbers)
"""
"""
#For Loops
numbers = [1, 2, 3, 4, 5, 6, 7, 8] ##Easier
for items in numbers:
    print(items)

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
"""

#Range()
for number in range(5):
    print(number)

#Tuples
"Like lists, but cannot be changed"
numbers = (1, 2, 3)
numbers.index(2)
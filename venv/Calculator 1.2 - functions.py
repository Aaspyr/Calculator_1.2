import sys
" This is a calculator using functions to make an math operations"

"I define the basic functions of the program"

def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def wrongNumber():
    print("You made the wrong choice")
    sys.exit()

" Creating calculator's options "
a = int(input("Write first number: "))
b = int(input("Write second number: "))
c = int(input("Choose the type of activity: 1- add, 2-subtract, 3-multiply, 4-divide: "))

" Creating a function dependency"
if (c==1):
    score = addition(a,b)
elif (c==2):
    score = subtraction(a,b)
elif (c==3):
    score = multiply(a,b)
elif (c==4):
    score = divide(a,b)
else:
    score = wrongNumber()

" Printing score"
print("Score is: ", score)
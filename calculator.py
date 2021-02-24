<<<<<<< HEAD
from os import system
=======
>>>>>>> 66b0b378c0b9b549de7fbc95f0bcf794b7a15843
def add(x,y):
    print("Sum: ", x + y)

def sub(x,y):
    print("Subtraction: ", x - y)

def mult(x,y):
    print("Multiply: ", x * y)

def div(x,y):
    print("Divide: ", x / y)

def pow(x,y):
    print("Power: ", x^y)


<<<<<<< HEAD

check=True
while check:
    system('cls')
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Exit")

    choice = input("Enter a choice: ")

    num1, num2 = input("Enter two numbers seperated by a comma:").split(",")
    num1, num2 = int(num1), int(num2)
    
    if choice == 1:
        print(add(num1,num2))
    elif choice == 2:
        print(sub(num1,num2))
    elif choice == 3:
        print(mult(num1,num2))
    elif choice == 5:
        print(div(num1,num2))
    elif choice == 4:
        print(pow(num1,num2))
    elif choice == 6:
        check = True
    
        
=======
>>>>>>> 66b0b378c0b9b549de7fbc95f0bcf794b7a15843

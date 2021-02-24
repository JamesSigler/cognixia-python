
def weird_arithmetic(x, y, z): #function definition line
    output = ((x**x + y**z) // z ) #code block
    #print output
    return output

some_number = weird_arithmetic(5, 6, 7)

print("some_number:", some_number)


def greet(name, greet):
    print(greet, name + "!")

greet("Maria", "Hello")


x=int(input("Enter a number: "))
y=int(input("Enter a 2nd number: "))

def add(x,y):
    print("Sum: ", x + y)

def sub(x,y):
    print("Subtraction: ", x - y)

add(x, y)
sub(x, y)

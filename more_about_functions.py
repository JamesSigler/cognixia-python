PI = 3.14

def some_function(x, y, z):
    final = x + y + z
    return(final)

output = some_function(5, 6, 7)
#print(output)

def greet_friend(name, greeting, sentence):
    output = "{0}, {1}! {2}".format(greeting, name, sentence)
    print(output)

greeting = greet_friend("Maria", "Hello", "How are you doing today?")
#   print greeting

def greet_user(greeting):
    user = input("Please enter your name: ")
    print(type(user))
    print("{}, {}!".format(greeting, user))

    print(5 +int(input("Please enter a integer.")))
    
greet_user("Hello")
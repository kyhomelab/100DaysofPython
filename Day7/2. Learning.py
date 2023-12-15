# Create a program that can take in input of the users name
# save the name in a variable
# pass the variable through a function and print "Hello _____"


name = input("What is your name?\n")
def greeting(name):
    print("Hello " + name)

greeting(name)

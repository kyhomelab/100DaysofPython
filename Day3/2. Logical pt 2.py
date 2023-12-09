print("Hello, welcome to the Coffee Shop")

name = (input("What is your name?\n"))

if name != "Ben":
    print("You have been banned!")
    exit()
else:
    print("What can I get for you," + name + "?")
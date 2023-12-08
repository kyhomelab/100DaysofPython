print("Hello, welcome to the Coffee Shop")

name = (input("What is your name?\n"))

if name == "Ben":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes":
        print("You have been banned!")
        exit()
    else:
        print("Welcome in, what can I get you, " + name + "?")
else:
    print("What can I get for you," + name + "?")

menu = "Tea, Coffee, Latte"

print(menu)
order = input()

#if order == "Latte":
    #price = 10

#if order == "Coffee":
#    price = 6

if order == "Latte":
    price = 10
elif order == "Tea":
    price = 3
elif order == "Coffee":
    price = 6
else:
    print("Sorry we dont have that here")
    price = 0

print(price)
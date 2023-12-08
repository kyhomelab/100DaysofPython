#print("Hello, welcome to the Coffee Shop")

#name = (input("What is your name?\n"))

#if name == "Ben":
#    print("You have been banned!")
#else:
#    print("What can I get for you," + name + "?")

#if 2 > 3:
#    print("Its true")
#else:
#   print("false")

#Adding this to the previous Coffee Shop Code

print("Hello, welcome to the Coffee Shop")
name = (input("What is your name?\n"))

if name == "Ben":
    print("You have been banned!")
    exit()
else:
    print("What can I get for you," + name + "?")

print("What can I get for you," + name + "?")
menu = "Expresso?\nBlack Coffee?\nTea?\n"

print(menu)
order = input()
print("How many " + order + " would you like?")
amount = input()
price = 8
total = int(amount) * price

print("Thank you. Your total is: $" + str(total))
print("We will have all " + amount + " " + order + " ready for you in a moment.")
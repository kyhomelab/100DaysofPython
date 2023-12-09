print("Hello, welcome to the Coffee Shop")

name = (input("What is your name?\n"))

if name == "Ben" or name == "Patricia" or name == "Jack":
    evil_status = input("Are you evil?\n")
    deeds = int(input("How many goo deeds have you done today?\n"))
    if evil_status == "Yes" and deeds < 4:
        print("You have been banned " + name+"!")
        exit()
    else:
        print("Welcome in, what can I get you, " + name + "?")
else:
    print("What can I get for you," + name + "?")
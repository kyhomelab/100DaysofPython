choice = int(input("What number would you like to choose?\n"))

def function(choice):
    for num in range(0, choice):
        if num % 3 == 0 and num % 5 == 0:
            print(str(num) + " fizzbuzz")
        elif num % 3 == 0:
            print(str(num) + " fizz")
        elif num % 5 == 0:
            print(str(num) + " buzz")
        else:
            print(num)

function(choice)


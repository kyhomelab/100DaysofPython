# ask the user for the temperature input
# if its less than 20 degrees you need boots
# if its less than 30 you need a coat
# if its less than 70 you need a jacket
# if its over 70 it is nice outside

temp = int(input("What is the weather outside?\n"))

if temp < 20:
    print("You need gloves")
    if temp > 15:
        print("You need boots")
elif temp <= 30:
    print("You need a coat")
elif temp <= 70:
    print("you need a jacket")
elif temp > 70:
    print("It is nice outside")


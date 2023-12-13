# If you are under 5 you are a kid
# If you are 5-15 you are a big kid
# If you are 15-21 you are a bigger kid
# If you are over 21 you are old

var = int(input("What is your age?"))
if var <= 5:
    print("You are a kid")
elif var <= 15:
    print("You are a big kid")
elif var <= 21:
    print("You are a bigger kid")
else: print("You are old")
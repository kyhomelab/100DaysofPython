# 1. Create an input with a greeting

# 2. Ask what their favorite food

# 3. ASk what their favorite hobby is

# 4. print with an f string their favorite food and hobby

name = (input("Hey how are you doing? What is your name?\n"))
food = (input("What's your favorite food " + name + "?\n"))
hobby = (input("What kind of hobby are you into?\n"))

# print("Thats really cool that you like to eat " + food + ", and you love " + hobby + " " + name + ".")

print(f"Thats really cool that you like to eat {food} and that you love {hobby} {name}.")
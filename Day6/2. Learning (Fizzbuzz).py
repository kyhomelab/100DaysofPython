# Fizzbuzz
# If a number is divisible by 3, print fizz
# If a number is divisible by 5, print buzz
# If a number is divisible by both, print fizzbuzz

for num in range (0,100):
    if num % 3 == 0 and num % 5 == 0:
        print(str(num) + " fizzbuzz")
    elif num % 3 == 0:
        print(str(num) + " fizz")
    elif num % 5 == 0:
        print(str(num) + " buzz")
    else:
        print(num)
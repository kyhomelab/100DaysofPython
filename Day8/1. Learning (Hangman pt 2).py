import random

name = input('Hello, what is your name?\n')
print(f"Welcome to HangMan {name}")

words = ["hacker", "bounty", "random"]

# Create an empty list
# For each letter in the secret_word add a "_" that will be printed to the console
# Example if your word is Hacher "_","_","_","_","_","_"

secret_word = random.choice(words)

guess = input("Guess a letter ").lower()
# Loop through each of the letters in the chosen word
# If the letter is in the word replace the "_" with the letter
# It should look like this "_","a","c","_","_","r"

for letter in secret_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")





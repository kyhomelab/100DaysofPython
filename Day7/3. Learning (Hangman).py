import random

# create a greeting
name = input('Hello, what is your name?\n')
print(f"Welcome to HangMan {name}")

# create your word list
words = ["hacker", "bounty", "random"]

# randomly choose a word from the list you have created
secret_word = random.choice(words)

# Ask a user to guess a letter
# bonus make the program take the input from the user and make it lowercase
guess = input("Guess a letter ").lower()
print(guess)
# check if the letter is in the word
for letter in secret_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")





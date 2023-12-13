# Write a program that prompts the user to enter their score (out of 100) and displays
# their corresponding grade based on the following criteria

# Scores 90 and above: Grade A
# Scores 80 to 89: Grade B
# Scores 70 to 79: Grade C
# Scores 60 to 69: Grade D
# Scores below 60: Grade F

grade = int(input("What grade did you receive?\n"))

if grade >= 90:
    print("Grade = A")
elif grade >= 80:
    print("Grade = B")
elif grade >= 70:
    print("Grade = C")
elif grade >= 60:
    print("Grade = D")
else:
    grade < 60
    print("Grade = F")


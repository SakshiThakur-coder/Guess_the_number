# Game: Guessing Gamee
import random

lowest_num = 10
highest_num = 100


answer = random.randint(lowest_num, highest_num)

print(" Number Guessing Gamee ")
print(f"Select a number between {lowest_num} and {highest_num}")

while True:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)  # Convert input to an integer

        if guess < lowest_num or guess > highest_num:
            print(" This number is out of range!")

        elif guess < answer:
            print("Oops! Too low! Try again.")

        elif guess > answer:
            print(" Oops! Too high! Try again.")

        else: 
            print(" Yayyyy! You guessed it right!")
            break  

    else:
        print(" Invalid input. Please enter a number.")

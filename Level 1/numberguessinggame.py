#importing random module
import random


#picking a random number
secret_number = random.randint(1, 100)

#setting up maximum no.of attempts to guess
max_attempts = 7
attempts = 0


#guessing game
print("Welcome to the Number Guessing Game!!")
print("I have taken a number between 1 and 100.")
print(f"You have {max_attempts} no.of attempts to guess it.\n")

while attempts < max_attempts:
    number = int(input("Enter your guess:"))
    attempts += 1

    if number == secret_number:
        print(f"Congratulations!!! You have guessed the right number in {attempts} attempts.")
        break
    elif number < secret_number:
        print("Too Low!!")
    else:
        print("Too High!!")
    
if attempts == max_attempts :
    print(f"Game Over!! The correct number is {secret_number}.")

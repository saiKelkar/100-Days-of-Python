import random

def num_guessed(guess, answer):
    if guess > answer:
        print("Too high.\nGuess again.\n")
        return False
    elif guess < answer:
        print("Too low.\nGuess again.\n")
        return False
    else:
        print(f"You got it! The answer was {answer}.")
        return True


print("Welcome to the Number Guessing Game!\nI'm thiking of a number between 1 and 100.")
rand_num = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 10 if difficulty == 'easy' else 5


while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    num = int(input("Make a guess: "))
    correct = num_guessed(num, rand_num)
    if correct:
        break
    attempts -= 1

if attempts == 0 and num != rand_num:
    print(f"You've run out of guesses. The number was {rand_num}.")
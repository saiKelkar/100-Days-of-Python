import random

word_list = ["monkey", "donkey", "sandal"]

# Randomly choose a word from the word_list
random_word = random.choice(word_list)
print(random_word)

# Give the user 6 lives and display as many _ as there are letters in the chosen word
lives = 6
display = list('_' * len(random_word))
print(display)

while lives > 0 and '_' in display:
    guess = input("Guess a letter: ").lower()

    # if the user input is there in the chosen word, display the word instead of the _, lives remain the same
    if guess in random_word:
        for index, letter in enumerate(random_word):
            if letter == guess:
                display[index] = guess
                print(display)
        print("Good guess")

    # if the user input is not there in the chosen word, continue displaying _, lives reduce by 1
    else:
        lives = lives - 1
        print(f"Wrong guess! {lives} lives remaining")

# Display the results at the end
if '_' not in display:
    print("Congratulations! You won the game")
else:
    print("Sorry, try again!")

    
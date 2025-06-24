# Game rules:
# To add the cards to the largest number without going over 21
# If the cards in our hand add up to more than 21, then it's called a bust -- we lose

# All cards from 2 to 10 -- count as their face value
# Jack, Queen, and King -- count as 10
# Ace -- can either count as a 1 towards your total, or it can count as an 11
# (value of Ace depends on how close you are to 21)
# if the dealer ends up with a hand smaller than 17, so 16 or under, they must take another card

import random

def deal_cards():
    return random.randint(1, 10)

def total_scores(your_cards, computer_cards):
    return sum(your_cards), sum(computer_cards)

def compare_scores(current_score, computer_score):
    if current_score > computer_score or computer_score > 21:
        print("You Win!")
    elif current_score == computer_score and current_score < 21:
        print("It's a Draw!")
    elif current_score > 21:
        print("You went over. Your lose")
    else:
        print("You lose")


your_cards = []
computer_cards = []

ask = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if ask == 'y':
    for i in range(2):
        your_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    current_score, computer_score = total_scores(your_cards, computer_cards)
    
    print(f"Your cards: {your_cards}, current score: {current_score}")
    print(f"Computer's first cards: {computer_cards[0]}")

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == 'y':
        your_cards.append(deal_cards())
        
        if computer_score <= 16:
            computer_cards.append(deal_cards())
        
        current_score, computer_score = total_scores(your_cards, computer_cards)
        
        print(f"Your cards: {your_cards}, current score: {current_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

        compare_scores(current_score, computer_score)
    
    elif another_card == 'n':
        print(f"Your cards: {your_cards}, current score: {current_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

        compare_scores(current_score, computer_score)
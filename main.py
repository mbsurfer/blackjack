############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def deal_card():
    """Returns a random card from the deck"""
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def show_cards(user_cards, computer_cards):
    print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    
def show_final_cards(user_cards, computer_cards):
    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")

while input("Would you like to play a game of Blackjack? Type 'y' or 'n':") == 'y':
    cls()
    print(art.logo)
    
    #Deal cards to user and computer
    user_cards = []
    computer_cards = []
    
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    show_cards(user_cards, computer_cards)
    
    winner = ""
    while winner == "":
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
    
        if user_score == 21:
            if computer_score == 21:
                winner = "draw"
                break
            winner = "user"
            break
        elif computer_score == 21:
            winner = "computer"
            break
        else:
            
            # player turn
            while user_score < 21:
                user_choice = input("Would you like to hit or stand? Type 'h' or 's':")
                if user_choice == 'h':
                    user_cards.append(deal_card())
                    user_score = calculate_score(user_cards)
                    show_cards(user_cards, computer_cards)
                elif user_choice == 's':
                    break
            
            # did player bust?
            if user_score > 21:
                winner = "computer"
                break
            
            # computer turn
            while computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)
                
                # did dealer bust?
                if computer_score > 21:
                    winner = "user"
                    break
            
            # check for winner if no one busted
            if winner == "":  
                if user_score > computer_score:
                    winner = "user"
                elif user_score < computer_score:
                    winner = "computer"
                else:
                    winner = "draw"
                
    # show final cards
    show_final_cards(user_cards, computer_cards)
    
    if winner == "user":
        print("You win! :)")
    elif winner == "computer":
        print("You lose! :(")
    else:
        print("Draw!")
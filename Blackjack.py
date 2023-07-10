#Imports + lists
import random
from art import logo
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []
dealer_ai = ["y","n"]

#Functions    

def deal():
    player_score = 0
    dealer_score = 0
#dealer draw
    while dealer_score <= 21:
        if dealer_score >= 11:
            dealer_choice = random.choice(dealer_ai)
            if dealer_choice == "y":
                draw = random.choice(cards)
                if dealer_score >= 11 and draw == 11:
                    draw = 1
                dealer_hand.append(draw)
                dealer_score += draw
        else:
            draw = random.choice(cards)
            dealer_hand.append(draw)
            dealer_score += draw
#player draw
    for draw in range(0,2):
        draw = random.choice(cards)
        if player_score >= 11 and draw == 11:
            draw = 1
        player_hand.append(draw)
        player_score += draw  
    dealer_1st = dealer_hand[0]
    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Computer's first card: {dealer_1st}")
    if player_score == 21 and (dealer_hand[0] + dealer_hand[1]) < 21:
        print("Player Wins by blackjack!")
        end = True
#Hit or stick
    else:
        end = False
    while not end:
        hit_stick = input("Type 'y' to get anouther card, type 'n' to stick: ").lower()
            #Hit
        if hit_stick =="y":
            draw = random.choice(cards)
            if dealer_score >= 11 and draw == 11:
                draw = 1
            player_hand.append(draw)
            player_score += draw
            if player_score > 21:
                print("You've gone bust!!")
                print(f"Your final cards: {player_hand}, final score: {player_score}")
                print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}")
                if dealer_score <= 21:
                    print("Dealer Wins")
                    end = True
                else:
                    print("No winner!")
                end = True
            else:
                print(f"Your cards: {player_hand}, current score: {player_score}")
                print(f"Computer's first card: {dealer_1st}")
            #Stick
        elif hit_stick =="n":          
            print(f"Your final cards: {player_hand}, final score: {player_score}")
            print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}")
            if player_score > dealer_score or dealer_score > 21:
                print("Player Wins!")
                end = True
            elif player_score == dealer_score:
                print("It's a draw!")
                end = True

#Gameplay Loop
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if play == "y":
    print(logo)
    deal()
    play = input("Do you want to play again? Type 'y' or 'n'").lower()
    if play == "y":
        player_hand = []
        dealer_hand = []
        os.system('cls||clear')
        print(logo)
        deal()
    elif play == "n":
       print("Thank you for playing")
else:
    print("Thank you for coming")
    
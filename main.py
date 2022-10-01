# blackjack

import random

# 11 is ace
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand = []
dealer_hand = []


def add_cards(c1, c2):
    sum = c1 + c2
    return sum


def deal_new_card():
    """ Selects a random card value from the array 'cards' """
    card = random.choice(cards)
    return card


def start_round():
    player_hand = [deal_new_card(), deal_new_card()]
    print(player_hand)
    dealer_hand = [deal_new_card()]
    print(dealer_hand)
    print(f"Your cards: {player_hand}")
    print(f"Dealer draws the first card: {dealer_hand}")
    return player_hand, dealer_hand


start_round()

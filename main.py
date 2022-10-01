# blackjack

import random

# 11 is ace
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_over = False


def score(current_cards):
    if sum(current_cards) == 21 and len(current_cards) == 2:
        print("Blackjack!")
        return 0
    if sum(current_cards) > 21 and 11 in current_cards:
        current_cards.remove(11)
        current_cards.append(1)
    return sum(current_cards)


def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Draw!"
    elif dealer_score == 0:
        return "Dealer has Blackjack, you lose"
    elif user_score == 0:
        return "Blackjack! You win!"
    elif user_score > 21:
        return "Bust! You lose"
    elif dealer_score > 21:
        return "Dealer busts!"
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"


player_hand = []
dealer_hand = []


def deal_new_card():
    """Selects a random card from the deck"""
    card = random.choice(cards)
    return card


for draw in range(2):
    player_hand.append(deal_new_card())
    dealer_hand.append(deal_new_card())

while not game_over:
    user_score = score(player_hand)
    dealer_score = score(dealer_hand)

    print(f"Your cards: {player_hand}, current score: {user_score}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    if user_score == 0 or dealer_score == 0 or user_score > 21:
        game_over = True
    else:
        hit = input("Type 'y' to hit(another card) or type 'n' to pass: ")
        if hit == 'y':
            player_hand.append(deal_new_card())
        else:
            game_over = True

while dealer_score != 0 and dealer_score < 17:
    dealer_hand.append(deal_new_card())
    dealer_score = score(dealer_hand)

print(compare(user_score, dealer_score))

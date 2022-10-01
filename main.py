# blackjack

import random

# 11 is ace
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand = []
dealer_hand = []


def deal_new_card():
    """Selects a random card from the deck"""
    card = random.choice(cards)
    return card


for draw in range(2):
    player_hand.append(deal_new_card())
    dealer_hand.append(deal_new_card())


# def start_round():
#     player_hand = [deal_new_card(), deal_new_card()]
#     print(player_hand)
#     dealer_hand = [deal_new_card()]
#     print(dealer_hand)
#     return player_hand, dealer_hand
# start_round()

def score(current_cards):
    if sum(current_cards) == 21 and len(current_cards) == 2:
        print("Blackjack")
    if sum(current_cards) > 21 and 11 in current_cards:
        current_cards.remove(11)
        current_cards.append(1)
    return sum(current_cards)


user_score = score(player_hand)

print(f"Your cards: {player_hand}")
print(f"Your score is {user_score}")
print(f"Dealer cards: {dealer_hand}")

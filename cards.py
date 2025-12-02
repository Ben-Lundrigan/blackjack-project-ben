# Cards module
import random

def create_deck():
    deck = []
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = [
        ("Ace", 11), ("2", 2), ("3", 3), ("4", 4), ("5", 5),
+        ("6", 6), ("7", 7), ("8", 8), ("9", 9),
+        ("10", 10), ("Jack", 10), ("Queen", 10), ("King", 10)
    ]
    for suit in suits:
        for rank, value in ranks:
            deck.append([suit, rank, value])
    random.shuffle(deck)
    return deck

def deal_card(deck, hand):
    hand.append(deck.pop())

def show_cards(title, hand):
    if title != "":
        print(title)
    for c in hand:
        print(f"{c[1]} of {c[0]}")
    print()

def hand_total(hand):
    total = 0
    aces = 0
    for suit, rank, value in hand:
        total += value
        if rank == "Ace":
            aces += 1
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total
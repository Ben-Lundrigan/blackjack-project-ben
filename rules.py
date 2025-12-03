# Rules module
from cards import deal_card, hand_total

MIN_BET = 5
MAX_BET = 1000

def validate_bet(bet, money):
    if bet < MIN_BET:
        return False
    if bet > MAX_BET:
        return False
    if bet > money:
        return False
    return True

def dealer_hit_to_17(deck, dealer_hand):
    while hand_total(dealer_hand) < 17:
        deal_card(deck, dealer_hand)

def blackjack_payout(bet):
    return round(bet * 1.5, 2)
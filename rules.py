# Rules module: Validates bets, handles dealer actions, and blackjack payout.
from cards import deal_card, hand_total

# Betting limits
MIN_BET = 5
MAX_BET = 1000

# Return true if bet meets game rules
def validate_bet(bet, money):
    if bet < MIN_BET:
        return False
    if bet > MAX_BET:
        return False
    if bet > money:
        return False
    return True

# Dealer draws cards until reaching 17 or higher
def dealer_hit_to_17(deck, dealer_hand):
    while hand_total(dealer_hand) < 17:
        deal_card(deck, dealer_hand)

# Return the 3:2 payout
def blackjack_payout(bet):
    return round(bet * 1.5, 2)
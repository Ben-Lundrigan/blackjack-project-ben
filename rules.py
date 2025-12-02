# Rules module

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
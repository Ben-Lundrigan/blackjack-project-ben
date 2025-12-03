# Main module
from cards import create_Deck, deal_card, show_cards, hand_total
from rules import validate_bet
import db

def display_title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()

def main():
    money = db.read_money()

    while True:
        print(f"Money: {money}")
        bet = float(input("Bet amount: "))

        if not validate_bet(bet, money):
            print("Invalid bet.")
            print()
            continue

        deck = create_deck()
        player = []
        dealer = []

        deal_card(deck, player)
        deal_card(deck, dealer)
        deal_card(deck, player)
        deal_card(deck, dealer)

        show_cards(f"YOUR CARDS: {player}")

        # Hit/Stand 

if __name__ == "__main__":
    main()
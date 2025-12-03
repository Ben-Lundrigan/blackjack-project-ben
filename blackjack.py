# Main module
from cards import create_Deck, deal_card, show_cards, hand_total
from rules import validate_bet
from rules import dealer_hit_to_17
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
        while True:
            choice = input("Hit or stand? (hit/stand): ")
            if choice == "hit":
                deal_card(deck, player)
                show_cards(f"YOUR CARDS: {player}")
                if hand_total(player) > 21:
                    print("You bust!")
                    money -= bet
                    break
            elif choice == "stand":
                break

        # Dealer turn
        dealer_hit_to_17(deck, dealer)
        show_cards(f"DEALER CARDS: {dealer}")

if __name__ == "__main__":
    main()
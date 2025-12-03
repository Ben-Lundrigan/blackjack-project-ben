# Main module
from cards import create_deck, deal_card, show_cards, hand_total
from rules import validate_bet
from rules import dealer_hit_to_17
import db

def display_title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()

def main():
    money = db.read_money()
    display_title()

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

        print("DEALERS'S SHOW CARD:")
        print(f"{dealer[0][1]} of {dealer[0][0]}")
        show_cards("YOUR CARDS:", player)

        # Hit/Stand
        while True:
            choice = input("Hit or stand? (hit/stand): ")
            if choice == "hit":
                deal_card(deck, player)
                show_cards("YOUR CARDS:", player)
                if hand_total(player) > 21:
                    print("You bust!")
                    money -= bet
                    break
            elif choice == "stand":
                break

        # Dealer turn
        dealer_hit_to_17(deck, dealer)
        show_cards("DEALER CARDS:", dealer)

        player_total = hand_total(player)
        dealer_total = hand_total(dealer)

        print(f"YOUR POINTS: {player_total}")
        print(f"DEALER'S POINTS: {dealer_total}")
        print()

        if dealer_total > 21:
            print("Dealer busts. You win!")
            money += bet
        elif player_total > dealer_total:
            print("You win!")
            money += bet
        elif player_total < dealer_total:
            print("Sorry. You lose.")
            money -= bet

        db.write_money(money)
        
        again = input("Play again? (y/n): ")
        print()
        if again.lower() != "y":
            print("Come back soon!")
            print("Bye!")
            break

if __name__ == "__main__":
    main()
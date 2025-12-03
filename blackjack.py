# Main module
from cards import create_deck, deal_card, show_cards, hand_total
from rules import validate_bet
from rules import dealer_hit_to_17, blackjack_payout
import db

def display_title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()

def main():
    
    # Loads player's money amount from file
    money = db.read_money()
    display_title()

    # Game loop
    while True:
        
        # If player doesn't have enough to play, offer to buy chips
        if money < 5:
            print(f"Your balance is too low to play. (Balance: {money})")
            buy = input("Do you want to buy more chips? (Y/N): ").lower()
            
            if buy == "y":
                try:
                    add_amount = float(input("Enter amount to add (min $5): "))
                    
                    if add_amount >= 5:
                        money += add_amount
                        db.write_money(money)
                        print(f"Money: {money}")
                        print()
                    else:
                        print("Amount must be at least $5.")
                        print()
                        continue

                except ValueError:
                    print("Please enter a valid number.")
                    print()
                    continue
            else:
                print("Come back soon!")
                print("Bye!")
                break

        # Show current money
        print(f"Money: {money}")

        # Get bet amount
        try:
            bet = float(input("Bet amount: "))
            print()
        except ValueError:
            print("Invalid input. Enter a number.")
            print()
            continue

        # Validate the bet against rules
        if not validate_bet(bet, money):
            print("Invalid bet.")
            print()
            continue

        # Create deck and hands
        deck = create_deck()
        player = []
        dealer = []

        # Initial deal (two cards each)
        deal_card(deck, player)
        deal_card(deck, dealer)
        deal_card(deck, player)
        deal_card(deck, dealer)

        # Show dealers first card and player's hand
        print("DEALER'S SHOW CARD:")
        print(f"{dealer[0][1]} of {dealer[0][0]}")
        print()
        show_cards("YOUR CARDS:", player)

        # Check for blackjack before hit/stand
        player_total = hand_total(player)
        dealer_total = hand_total(dealer)

        if player_total == 21 or dealer_total == 21:
            print("DEALER'S CARDS:")
            show_cards("", dealer)

            print(f"YOUR POINTS: {player_total}")
            print(f"DEALER'S POINTS: {dealer_total}")
            print()

            # Player blackjack only
            if player_total == 21 and dealer_total != 21:
                print("Blackjack! You win.")
                win = blackjack_payout(bet)
                money += win

            # Dealer blackjack only
            elif dealer_total == 21 and player_total != 21:
                print("Dealer has blackjack. You lose.")
                money -= bet
            else:
                print("Push. No one wins.")

            # Save updated money
            print(f"Money: {money}")
            db.write_money(money)

            # Ask to play again
            print()
            again = input("Play again? (Y/N): ")
            print()
            if again.lower() != "y":
                print("Come back soon!")
                print("Bye!")
                break
            else:
                continue

        # Hit/stand loop
        busted = False
        while True:
            choice = input("Hit or stand? (Hit/Stand): ")
            
            if choice == "hit":
                print()
                deal_card(deck, player)
                show_cards("YOUR CARDS:", player)
                
                # Player busts
                if hand_total(player) > 21:
                    print("You bust!")
                    money -= bet
                    print(f"Money: {money}")
                    busted = True
                    break
            
            elif choice == "stand":
                break

        # Stop round early if bust
        if busted:
            db.write_money(money)
            print()
            again = input("Play again? (Y/N): ")
            print()
            
            if again.lower() != "y":
                print("Come back soon!")
                print("Bye!")
                break
            else:
                continue

        # Dealer turn (hits to 17)
        print()
        dealer_hit_to_17(deck, dealer)
        show_cards("DEALER CARDS:", dealer)

        # Final totals
        player_total = hand_total(player)
        dealer_total = hand_total(dealer)

        print(f"YOUR POINTS: {player_total}")
        print(f"DEALER'S POINTS: {dealer_total}")
        print()

        # Determine outcome
        if dealer_total > 21:
            print("Dealer busts. You win!")
            money += bet
            print(f"Money: {money}")
        
        elif player_total > dealer_total:
            print("You win!")
            money += bet
            print(f"Money: {money}")
        
        elif player_total < dealer_total:
            print("Sorry. You lose.")
            money -= bet
            print(f"Money: {money}")
        
        else:
            print("Push. No one wins.")
            print(f"Money: {money}")

        # Save updated money
        db.write_money(money)
        
        print()
        again = input("Play again? (Y/N): ")
        print()
        
        if again.lower() != "y":
            print("Come back soon!")
            print("Bye!")
            break

if __name__ == "__main__":
    main()
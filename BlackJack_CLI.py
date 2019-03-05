import random
import time
import copy


class Card():

    def __init__(self, value=1, rank='', suit=''):
        self.value = value
        self.suit = suit
        self.rank = rank


class Deck():
    suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    ranks = [('Ace', 11), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10),
             ('Jack', 10), ('Queen', 10), ('King', 10)]

    def __init__(self):

        self.cards = []
        for rank in self.ranks:
            for suit in self.suits:
                c = Card()
                c.suit = suit
                c.rank = rank[0]
                c.value = rank[1]
                self.cards.append(c)


class BlackJack:

    def __init__(self, player1):
        self.player1 = player1

        self.hands = []
        self.dealer = []
        self.stack = []

    def start_game(self):

        print(f"Hi {self.player1}, lets play some BlackJack")
        self.hands = []
        self.dealer = []
        self.stack = []
        time.sleep(1)
        global deck
        deck = Deck()
        random.shuffle(deck.cards)
        self.deal(deck.cards)

    def deal(self, deck):
        first_hand = []
        split_hand = []
        for i in range(2):
            card = deck.pop()
            card2 = deck.pop()
            first_hand.append(card)
            self.dealer.append(card2)
        print("Drawing everyones cards...")

        print(f"Dealer shows a card..{self.dealer[1].rank}")

        if first_hand[0].value == first_hand[1].value:
            print("You have drawn a same value pair")
            print([card.value for card in first_hand])
            answered = False
            while answered == False:
                answer = input("Would you like you split? Y/N: ")
                if answer.lower() == 'y' or answer.lower() == 'yes':

                    dup_card = first_hand.pop()
                    split_hand.append(dup_card)
                    card1, card2 = deck.pop(), deck.pop()
                    first_hand.append(card1)
                    split_hand.append(card2)
                    self.hands.append(first_hand)
                    self.hands.append(split_hand)
                    print("Your hands are:")
                    print(first_hand[0].rank, first_hand[1].rank)
                    time.sleep(1)
                    print(split_hand[0].rank, split_hand[1].rank)

                    time.sleep(2)

                    answered = True

                else:

                    self.hands.append(first_hand)
                    answered = True



        else:

            self.hands.append(first_hand)

            # we now have our initial hands or split hands
            #   now we want to play with each hand

        self.play_blackjack()

    def play_blackjack(self):

        # keep looping until bust or stick
        for hand in self.hands:

            result = self.total_of_hand(hand)

            while True:

                if result < 21 and len(hand) < 5:

                    answer = input("Would you like to draw a card? Y/N: ")
                    if answer.lower() == 'y' or answer.lower() == 'yes':
                        card = self.draw(hand)
                        hand.append(card)
                        result = self.total_of_hand(hand)

                    if answer.lower() == 'n' or answer.lower() == 'no':
                        # save results
                        self.stack.append(result)

                        break
                if result == 21:
                    print("You have a Black Jack!")
                    self.hands.remove(hand)
                    break
                if result > 21:
                    print("You are bust")
                    self.hands.remove(hand)
                    break
                if len(hand) == 5:
                    print("Your hand has won")
                    self.hands.remove(hand)
                    break
        if len(self.stack) > 0:
            self.dealer_turn(self.stack)

        if len(self.hands) == 0:
            self.play_again()

    def total_of_hand(self, hand):

        total = 0
        print("-" * 40)
        print("Your cards are:")
        print([card.rank for card in hand])

        for card in hand:

            if card.rank == 'Ace':
                while True:
                    answer = input("Would you like your ACE to be 1 or 11?\nEnter number: ")
                    if answer == '1':
                        total += 1
                        break
                    elif answer == '11':
                        total += 11
                        break
                    else:
                        print("Number not recognised, try again!")
                        time.sleep(1)

            else:
                total += card.value

        print("Your current total is:", total)
        return total

    def draw(self, hand):
        card = deck.cards.pop()
        return card

    def stick(self, hand):

        total = sum([card.value for card in hand])
        print("Your total is:", total)
        time.sleep(1)
        print("Now it's the dealers turn!")
        time.sleep(1)
        print("The dealer shows his hand: ")
        print([card.rank for card in self.dealer])
        time.sleep(3)

        self.dealer_draw()

    def dealer_turn(self, stack):
        dealer_total = 0
        game_over = False
        dealer_bust = False
        dealer_win_override = False
        highest_card = max(self.stack)
        time.sleep(1)
        test_total = sum([card.value for card in self.dealer])
        if test_total > 21:
            for card in self.dealer:
                if card.rank == 'Ace':
                    card.value = 1

        while dealer_bust == False:
            dealer_total = 0
            for card in self.dealer:
                dealer_total += card.value
            if dealer_total > 21:
                print(f"Dealers hand: {[card.rank for card in self.dealer]}")
                print("The dealer is bust!\nYou have won!")
                time.sleep(1)
                dealer_bust = True



            elif len(self.dealer) == 5 and dealer_total <= 21:

                print("The dealer has won with 5 cards!")
                print(f"Dealers hand: {[card.rank for card in self.dealer]}")
                dealer_win_override = True
                break

            elif dealer_total == 21:
                print("The dealer has won with a Black Jack!")
                print(f"Dealers hand: {[card.rank for card in self.dealer]}")
                game_over = True
                dealer_win_override = True
                break
            elif dealer_total < highest_card:
                self.dealer_draw()
            elif dealer_total == highest_card:
                print(f"Dealers hand: {[card.rank for card in self.dealer]}")
                print("You have a draw!")
                break
            elif dealer_total > highest_card:
                print("You have lost!")
                print(f"Dealers hand: {[card.rank for card in self.dealer]}")
                dealer_win_override = True
                break

        if len(self.stack) > 1 and dealer_bust == False and dealer_win_override == False:
            min_card = min(self.stack)
            if min_card == dealer_total:
                print("Your lowest card hand is a draw!")
            if min_card < dealer_total:
                print("Your lowest card hard lost!")
            elif min_card > dealer_total:
                print("Congrats you have won your second hand")
        elif len(self.stack) > 1 and dealer_bust == True:
            print("Your second hand has won!")
        game_over = True
        if game_over == True:
            self.play_again()

    def dealer_draw(self):
        print("The dealers draws a card...")
        time.sleep(3)

        card = deck.cards.pop()
        print("Dealer has drawn...", card.rank)

        time.sleep(2)
        self.dealer.append(card)
        self.dealer_turn(self.stack)

    def play_again(self):

        while True:
            answer = input("Would you like to play again? Y/N: ")
            if answer.lower() == 'y':

                print('-' * 40)
                print('-' * 40)
                print('-' * 40)
                self.start_game()

            elif answer.lower() == 'n':
                print("-" * 40)
                print("Thankyou for playing with Python Casino!")
                print("-" * 40)
                exit()


def game_intro():
    print("-" * 40)
    print(' ' * 5, "Welcome to the Python Casino!")
    print("-" * 40)
    print("""Rules of the game Black Jack are as followed:\n
    1. Both the dealer and the customer will draw two cards each from a shuffled pack of cards.
    2. The dealer will show his top card only
    3. Your goal is to draw cards one at a time to get as close to 21 or get the perfect 21 to win
    4. On the initial deal you have the option to split same value cards
    5. If you draw 5 cards and not bust you will win
    5. When you decide to stick (not draw anymore), and your turn is done,
     the dealer will show his cards and decide to draw or stick
    Good luck!\n""")
    print('-' * 40)

    while True:
        input_name = input("Enter your name to begin: ")
        if input_name.isalpha():
            person = BlackJack(input_name)

            person.start_game()
            break
        else:

            print("That's not a valid name!")
            answer = input("Type 'q' to quit or any key to continue: ")
            if answer.lower() == 'q': break
            print("-" * 40, "\n")


if __name__ == '__main__':
    game_intro()

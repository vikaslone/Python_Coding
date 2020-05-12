"""

Milestone Project 2 - Blackjack Game

In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:
You need to create a simple text-based BlackJack game
The game needs to have one player versus an automated dealer.
The player can stand or hit.
The player must be able to pick their betting amount.
You need to keep track of the player's total money.
You need to alert the player of wins, losses, or busts, etc...

And most importantly:
You must use OOP and classes in some portion of your game.
You can not just use functions in your game.
Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!
Feel free to expand this game. Try including multiple players.
Try adding in Double-Down and card splits! Remember to you are free to use any resources you want and as always:

Deck: Consists of 52 cards
      Ace can be counted as 1 or 11 as the player chooses
      King/Queen/Jack are each worth 10 points
      Rest are numbered cards from 2 to 9 and are worth the same points


Actions:
Hit: Receive a card from deck
Stay: Do not take any more cards from deck

"""

# Import Statements

import random

# Global variables

suits = ('Hearts', 'Clubs', 'Spades', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True

# Class Descriptions

# Each card object will have a suit and a corresponding rank


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # This will return a car d as "Two of Hearts" i.e., Rank of Suit
    def __str__(self):
        return self.rank + ' of ' + self.suit

# A deck object will have 52 card objects (4 suits times 13 ranks)


class Deck:
    # Create 52 card objects by looping through 4 suits and 13 ranks
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append((Card(suit, rank)))

    # This magic method will return list of all card in a deck.
    def __str__(self):
        deck_composition = ''
        for card in self.deck:
            deck_composition += card.__str__() + '\n'
        return deck_composition

    # This will shuffle cards in a deck to be in a random order
    def shuffle(self):
        random.shuffle(self.deck)

    # This will deal a single card form the deck to the player or the dealer
    def deal(self):
        single_card = self.deck.pop()
        return single_card


# This class is used to maintain balance details of a player
class Player:

    def __init__(self, player, balance):
        self.player = player
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f'{deposit_amount} has been deposited and the new balance is {self.balance}')

    def withdraw(self, bet_amount):
        if self.balance == 0:
            print('Funds Unavailable')
        elif self.balance < bet_amount:
            print('Bet amount greater than existing account balance')
        else:
            self.balance -= bet_amount
        print(f'{bet_amount} has been withdrawn to bet and the new balance is {self.balance}')

    # This is a dunder/magic method which will return a string
    # This is called by default when print or str of an object is called
    def __str__(self):
        return f'Player {self.player} has balance of {self.balance}'

    # This is a dunder/magic method which will delete an instance and perform actions mentioned
    def __del__(self):
        print('Player account has been deleted')

# This class is used to maintain balance details of a player's chips


class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def add_winning(self):
        self.total += self.bet
        print(f'{self.bet} has been added and the new total is {self.total}')

    def lose_bet(self):
        self.total -= self.bet
        print(f'{self.bet} has been deducted and the new total is {self.total}')


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_ace_value(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


'''
1. Ask player if he wants to start first
2. If not start with dealer
3. Deal 2 cards from the deck to the player and the dealer
4. Display both cards of the player and only one card of the dealer and keep the other card hidden
5. If so, start with adding a balance amount and the bet he will place
6. Keep asking if the player or dealer, who ever goes first, wants to hit or stay for every turn
7. If a stay is ordered and the value of all the cards in hand is less than 21, move to the opposite player/dealer
8. Keep checking if the value in hand for the player or the dealer is a bust
'''

# Functions


# Display the starting deck
def display_start(player, dealer):
    print('Player Hand: ', *player.cards, sep='\n')
    print('\nDealer Hand: ')
    print('<card hidden>')
    print(dealer.cards[1])


# Display all the cards
def display_end(player, dealer):
    print('Player Hand: ', *player.cards, sep='\n')
    print('Dealer Hand: ', *dealer.cards, sep='\n')


# Take bet from a player
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet: '))
        except ValueError:
            print('Bet has to be an integer')
        else:
            if chips.bet > chips.total:
                print('Bet cannot be more than the total number of chips')
            else:
                break


# If player selects hit, add a card to his hand and adjust value
def hit(hand, deck):
    hand.add_card(deck.deal())
    hand.adjust_ace_value()


# If player busts, he loses the bet
def player_busts(chips):
    print('Player busts')
    chips.lose_bet()


# If dealer busts, add the winnings to the player
def dealer_busts(chips):
    print('Dealer busts')
    chips.add_winning()


# If dealer wins, subtract the bet from the player's total
def dealer_wins(chips):
    print('Dealer wins')
    chips.lose_bet()


# If player wins, add the winnings to the player
def player_wins(chips):
    print('Player wins')
    chips.add_winning()


# If player and dealer tie
def tie_game():
    print('Dealer and Player tie. It is a push!')


# Actual Game starts here
player_ready = input('Do you want to play blackjack? Please enter Y or N: ')

if player_ready.upper() == 'Y':
    playing = True
else:
    playing = False

while playing:
    # Create a new Deck
    playing_deck = Deck()

    # Shuffle the deck
    playing_deck.shuffle()

    # Create empty dealer and player hand lists
    dealer_hand = Hand()
    player_hand = Hand()

    # Deal 2 cards to dealer
    dealer_hand.add_card(playing_deck.deal())
    dealer_hand.add_card(playing_deck.deal())

    # Deal 2 cards to player
    player_hand.add_card(playing_deck.deal())
    player_hand.add_card(playing_deck.deal())

    # Display cards dealt to both dealer and player
    display_start(player_hand, dealer_hand)

    # Assign chips to the player, defaulted to 100
    player_chips = Chips()

    # Ask the player to bet some chips
    take_bet(player_chips)

    # Ask player if he would like to hit(H) or stand(S)
    while True:
        hit_stand = input('Would you like to hit(H) or stand(S): ')

        if hit_stand.upper() == 'H':
            hit(player_hand, playing_deck)

            display_start(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_busts(player_chips)
                break
        elif hit_stand.upper() == 'S':
            break
        else:
            print('Select either H or S and nothing else')
            continue

    if player_hand.value <= 21:
        print('Dealer starts his turn')

        # Dealer will stand if his hand value is 17 or more
        while dealer_hand.value < 17:
            hit(dealer_hand, playing_deck)

        display_end(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_chips)

        elif dealer_hand.value < player_hand.value:
            dealer_wins(player_chips)

        elif player_hand < dealer_hand:
            player_wins(player_chips)
        else:
            tie_game(player_chips)

    print(f'Player winnings stand at: {player_chips.total}')

    new_game = input('Would you like to play a new game? Yes(Y) or No(N): ')

    if new_game.upper() == 'Y':
        playing = True
    else:
        playing = False
        print('Thanks for playing')
        break

# Test Code
'''
test_deck = Deck()
test_deck.shuffle()
new_hand = Hand()
new_hand.add_card(test_deck.deal())
new_hand.add_card(test_deck.deal())
print(new_hand.value)
for card in new_hand.cards:
    print(card)
'''


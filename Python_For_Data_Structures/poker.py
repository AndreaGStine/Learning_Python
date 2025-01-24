# In progress. Goal: Playable variable player poker
# To do: Reformat and complete the holdem function.
# Should have a sub-function for each part of the game (pre-flop, flop, turn, river)
#To do: Allow players to act simultaneously, be able to "whisper" to each player, and reformat most printed lines
#to be whispered to players
#Presumably this means have some kind of *actual* interface... so this project is on-hold for some time.

#Constructing acceptable ranks and suites of a deck of cards
Ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
Suites = ['S', 'C', 'D', 'H']

# Constructing a Card object. A Card has a suite and a rank.
class Card:
    def __init__(self, rank = '', suite = ''):
        self.suite = suite
        self.rank = rank


# Constructing a Deck object. A Deck is a set of cards.
class Deck:
    def __init__(self, cards = set([])):
        self._cards = cards
    for s in Suites:
        for r in Ranks:
            self._cards.append(Card(rank=r, suite=s))

    #You can move a card from a deck to a hand. This chooses a Card from the Deck at random, adds it to
    #the Hand, and removes it from the Deck.
    def draw(self, hand):
        drawn_card = random.choice(cards)
        hand.append(drawn_card)
        self._cards.remove(drawn_card)

    #You can move a card from a pile to a Deck. This chooses a specified Card from the pile,
    #removes it from the pile, and adds it to the Deck
    def shufflein(self, pile, card):
        if card in pile:
            self._cards.append(card)
            pile.remove(card)
        else:
            print('That card is not in that pile')

#Constructing a Player for the poker game. A player has:
#A Hand of two cards, a quantity of Chips, a state of being actively their turn or not, and a state of sitting at the table or not
class Player:
    def __init__(self, hand = set([]), chips = 0, active = False, sitting = True):
        self._hand = hand
        self._chips = chips
        self._active = active
        self._sitting = sitting

    #When it is a player's turn, they may bid
    def bid(self, quantity, min, pot):
        complete = False
        try:
            if quantity >= min and quantity < chips:
                chips = chips - quantity
                pot = pot + quantity
                min = quantity
                complete = True
                print(self + ' bids ' + quantity + ', pot is now: ' + pot)
            elif quantity == chips:
                chips = chips - quantity
                pot = pot + quantity
                min = quantity
                complete = True
                print('All in! Pot is now: ' + pot)
            else:
                print('Invalid bid.')
            return complete
        except:
            print('Invalid bid.')
            return complete

    #... Or raise (minus e because "raise" seems to be a keyword)
    def rais(self, quantity, min, pot):
        complete = False
        try:
            if quantity >= min and quantity < chips:
                chips = chips - quantity
                pot = pot + quantity
                min = quantity
                complete = True
                print(self + ' bids ' + quantity + ', pot is now: ' + pot)
            elif quantity == chips:
                chips = chips - quantity
                pot = pot + quantity
                min = quantity
                complete = True
                print('All in! Pot is now: ' + pot)
            else:
                print('Invalid bid.')
            return complete
        except:
            print('Invalid bid.')
            return complete


    #... Or call
    def call(self, quantity, pot):
        if quantity < chips:
            chips = chips - quantity
            pot = pot + quantity
            print(self + ' calls, pot is now: ' + pot)
        else:
            pot = pot + chips
            chips = 0
            print('All in! Pot is now: ' + pot)

    #... Or fold
    def fold(self):
        self._active = False
        print(self + ' folds')

    #... Or stand
    def stand(self):
        self._active = False
        self._sitting = False
        print(self + ' stands')

    #... Or sit
    def sit(self, newchips):
        complete = False
        if newchips > 0:
            chips = newchips
            self._active = False
            self._sitting = True
            print(self + 'sits with ' + chips + ' chips')
            complete = True
        else:
            print('Invalid chips.')
        return complete




#A player's move is a function of the player moving, the minimum, and the pot
#, and returns whether or not the player bidded or raised
#And if so, how that changed the minimum bid and the pot
def move(player, min, pot):
    print('Minimum bid is:' + min)
    # Player's turn ends when the turn is complete. Folding and calling automatically
    # completes the turn, while bidding and raising requires a correct quantity.
    # if an incomplete quantity is selected, the turn will stay incomplete until a correct
    # quantity is selected
    complete = False
    bidraise = False
    while complete == False:
        print('Player ' + player + ', choose a move:')
        # Splits player's choice into a word (bid, fold, call, raise) and a quantity (if bid or raise)
        choice = input().split()
        if choice[0] == 'bid' or 'Bid':
            complete = player.bid(choice[1], min, pot)
            bidraise = complete
        elif choice[0] == 'raise' or 'Raise':
            complete = player.rais(choice[1], min, pot)
            bidraise = complete
        elif choice[0] == 'fold' or 'Fold':
            player.fold
            complete = True
        elif choice[0] == 'call' or 'Call':
            player.call()
            complete = True
        elif choice[0] == 'stand' or 'Stand':
            player.stand
            complete = True
        else:
            print('Invalid choice.')
    return bidraise

#At the start of each round, every inactive player is given a choice to sit in.
#Players can stand at any point and immediately forfeit their hand, which is technically contrary to
#standard poker rules, but I'm not at the point of being able to accommodate multiple players acting simultaneously,
#So I'd rather give the option to fold and stand in one go rather than fold and then stand at the end of the round.
def start(players):
    activeplayers = []
    for p in players:
        if p._sitting == True:
            activeplayers.append(p)
        else:
            complete = False
            while complete == False:
                print('Player ' + p + ', would you like to sit?')
                choice = input()
                if choice == 'Yes' or 'yes' or 'Y' or 'y':
                    print('How many chips are you bringing to the table?')
                    p.sit(input())
                    activeplayers.append(p)
                    complete = true
                elif choice == 'No' or 'no' or 'N' or 'n':
                    print('Okay! Enjoy watching.')
                    complete = true
                else:
                    print('Invalid choice. Try again.')
    return activeplayers

def biddingphase(activeplayers, min, pot):
    i = 0
    j = 0
    while j < len(activeplayers):
        j += 1
        if move(activeplayers[i], min, pot) == True:
            j = 0

        if i < len(activeplayers):
            i += 1
        else:
            i = 0
    print('Bidding phase complete.')


def preflop(activeplayers, deck, min, pot, dealer):
    for p in activeplayers:
        deck.draw(p._hand)
        deck.draw(p._hand)
"""
def flop(activeplayers, deck, min, pot, dealer):

def turn(activeplayers, deck, min, pot, dealer):

def river(activeplayers, deck, min, pot, dealer):

def holdem(activeplayers):


    round = 0
    while len(activeplayers) > 1:
        round = round + 1
        move = 0
        min = 1
        pot = 0
"""


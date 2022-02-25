import random

deck = [
    ["hearts","A",2,3,4,5,6,7,8,9,10,"J","Q","K"],
    ["diamonds","A",2,3,4,5,6,7,8,9,10,"J","Q","K"],
    ["clubs","A",2,3,4,5,6,7,8,9,10,"J","Q","K"],
    ["spades","A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    ];

specialDeck = ["J","Q","K"];
aDeck = ["A"];
record = [];
conjunto = [];

class Card:

    def __init__(self, suit, index, value):
        self.suit = suit;
        self.index = index;
        self.value = value;
    
    def valueSpecial(card):
        if card.value in specialDeck:
            card.value = 10;
            return card;
        else:
            return card;
    
    def aValue(card):
        if card.value == "A":
            card.value = 11;
            return card;
        else:
            return card;

# machine send number especify ramdoly the index of suit and card.
def machine():
    suit = random.randint(0,3);
    index = random.randint(1,13);
    return suit,index;

# assiner, make a object named card with suit , index, value.
#  Inspect if the card have the value of J,Q,K change it to 10 and value A change it to 11
#  Return Object named card

def assiner():
    suit, index = machine();
    card = Card(suit, index, deck[suit][index]);
    card = card.valueSpecial();
    card = card.aValue();
    return card;

# Dealer receive the object card, compares it if gone out. 
# If true, request a new card to assiner, 
# If don't, insert the suit and index formated to the record and return the card to the table to be played. 

def dealer():
    card = assiner()
    index = f"{card.suit}:{card.index}"
    if index in record:
        # print(f"{index} Repetido")
        return dealer();
    else:
        record.append(index);
        return card;
        # print(record)
        

def decision(playerHand, playerCount, playerResponse, croupierHand, croupierCount, croupierResponse):
    if playerHand == 21 and playerCount == 0 and croupierHand == 21 and croupierCount == 0:
        x = "Draw Blackjack!!!"
        decisionResponse = "DRAW"
        return x, decisionResponse;
    elif croupierHand == 21 and croupierCount == 0:
        x = "Croupier's Blackjack"
        decisionResponse = "LOSE"
        return x, decisionResponse;
    elif playerHand == 21 and playerCount == 0:
        x = "Player's Blackjack"
        decisionResponse = "BLACKJACK"
        return x, decisionResponse;
    elif playerResponse == "PASSED" and croupierResponse == "STAND":
        x = f"Croupier's Win with: {croupierHand}"
        decisionResponse = "LOSE"
        return x, decisionResponse;
    elif playerResponse == "STAND" and croupierResponse == "PASSED":
        x = f"Player's Win with: {playerHand}"
        decisionResponse = "WIN"
        return x, decisionResponse;
    elif playerResponse == "STAND" and croupierResponse == "STAND":
        if playerHand < croupierHand:
            x = f"Croupier's win with: {croupierHand} vs {playerHand}"
            decisionResponse = "LOSE"
            return x, decisionResponse;
        elif playerHand == croupierHand:
            x = "Draw!!!"
            decisionResponse = "DRAW"
            return x, decisionResponse;
        else:
            x = f"Player's win with: {playerHand} vs {croupierHand}"
            decisionResponse = "WIN"
            return x, decisionResponse;
    elif playerResponse == "PASSED" and croupierResponse == "PASSED":
        x = "All are losers, go ahead study english"
        decisionResponse = "LOSE"
        return x, decisionResponse;
    else:
        x = f"Croupier's win with: {croupierHand} vs {playerHand}"
        decisionResponse = "LOSE"
        return x, decisionResponse;
        
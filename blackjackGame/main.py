import time
import table
import players
from tkinter import *
from tkinter import ttk

record = [];
coins = 1;
croupierCards = [];
playerCards = [];
croupierHand = 0;
playerHand = 0;
playerCount = 0;
croupierCount = 0;
playerResponse = ""
endTurn = ["21","STAND","PASSED"]

def dispenser():
    global record
    global coins
    global croupierCards
    global playerCards
    global croupierHand    
    global playerHand
    global playerCount
    global croupierCount
    option = int(input("""Do you want continue? press 1.
If you want take out your coins press 2: """));
    if option == 1:
        record = [];
        croupierCards = [];
        playerCards = [];
        croupierHand = 0;
        playerHand = 0;
        playerCount = 0;
        croupierCount = 0;
    elif option == 2:
        print(f"Total of coins winned!!! {coins}");
        coins = 0;
        return coins;
    else:
        print("Invalid option.")
        dispenser();



def coinControler(coins, decisionResponse):
    if decisionResponse == "WIN":
        coins += 2;
        return coins;
    elif decisionResponse == "DRAW":
        coins += 1;
        return coins;
    elif decisionResponse == "BLACKJACK":
        coins += 3;
        return coins;
    else:
        coins += 0;
        return coins;
    

 # Croupier's Turn 
def croupierTurn(croupierCount, croupierHand, croupierResponse):   
        global endTurn;
        while croupierResponse not in endTurn:
            croupierCount += 1;
            # print(f' el turno actual de croupier es: {croupierCount}');
            # print(f'hand croupier while: {croupierHand}')
            # print(croupierResponse)
            croupierHand = croupierAddCard(croupierCount, croupierHand);
            croupierResponse = croupier.croupierGame(croupierHand);
        return croupierCount, croupierHand, croupierResponse;
        print(croupierResponse) 

# Player's Turn
def playerTurn(playerCount, playerHand, playerResponse):
        global endTurn;
        while playerResponse not in endTurn:
            playerCount += 1;
            playerHand = playerAddCard(playerCount, playerHand);
            print(f"\n---->Total value in hand: {playerHand}\n")
            playerResponse = player.playerGame(playerHand);     
        return playerCount, playerHand, playerResponse
        # print(playerResponse)   


def croupierAddCard(i, croupierHand):
    croupierCards.append(table.dealer());
    croupierHand += croupierCards[i].value;
    # print(f' cartero croupier : {croupierHand}')
    return croupierHand;
    
    
def playerAddCard(i, playerHand):
    x = ""
    playerCards.append(table.dealer());
    playerHand += playerCards[i].value;
    x += str(playerCards[i].value)
    print(f' Card: {x} for Player')
    return playerHand;
    
    
def start(croupierHand, playerHand):
    for i in range(2):
        playerCount = i;
        croupierCount = i;
        croupierHand = croupierAddCard(i,croupierHand);
        playerHand = playerAddCard(i, playerHand);
    return croupierHand, playerHand;


if __name__ == "__main__":
    
    while coins > 0:
        print("""*********************************************************
*********************************************************\n""")
        coins -= 1;
        # Creating objects of Player and Croupier.
        croupier = players.Player(croupierCount, croupierCards, croupierHand);
        player = players.Player(playerCount, playerCards, playerHand);
            
        # Start the Game, verifies if have coins availables and give 2 card for each player.
        croupierHand, playerHand = start(croupierHand, playerHand)
        print(f"\n---->Total value in hand: {playerHand}")
        print("*********************************************************")
        
        # Listeners to response of players for the first round.
        croupierResponse = croupier.croupierGame(croupierHand);
        playerResponse = player.playerGame(playerHand);
        print(f"Player {playerResponse}")
        print("*********************************************************")
        #Interactive turn for player.
        playerCount, playerHand, playerResponse = playerTurn(playerCount, playerHand, playerResponse);
        if playerCount > 0:
            print(f"Player {playerResponse}")
        print("""*********************************************************
*********************************************************\n""")
        time.sleep(2);
        # Turn for croupier.
        print("Corupier's Turn")
        print(f'Actual Hand of Croupier : {croupierHand}')
        print("*********************************************************")
        time.sleep(2);
        croupierCount, croupierHand, croupierResponse = croupierTurn(croupierCount, croupierHand, croupierResponse);
        if croupierResponse == "ADD":
            print(f"Croupier {croupierResponse}")
            print(f'New Hand of Croupier : {croupierHand}')
        else:
            # print(f'New Hand of Croupier : {croupierHand}')
            print(f"Croupier {croupierResponse}")
        time.sleep(2);
        print("*********************************************************\n")
    # Definer
        x, decisionResponse = table.decision(playerHand, playerCount, playerResponse, croupierHand, croupierCount, croupierResponse);
        print(x)
        print("*********************************************************\n")
        time.sleep(1);
    # Adds coins to your pocket
        coins = coinControler(coins, decisionResponse);
        print("No coins for you this time, play again")
        if coins > 0:
            dispenser()
    print("*********************************************************")   
    print("Insert a Coin")    
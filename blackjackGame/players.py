class Player:

    def __init__(self, turn, cards, hand):
        self.turn = turn;
        self.cards = cards;
        self.hand = hand;
    
    def croupierGame(self, hand):
        if hand < 17:
            return Player.addCardToHand();
        elif hand > 21:
           return Player.passed();
        elif hand == 21:
            return Player.blackjack();
        else:
            return Player.stand();
        
    def playerGame(self, hand):
        if hand > 21:
            return Player.passed();
        elif hand == 21:
            return Player.blackjack();
        elif hand < 21:
            choise = int(input("""Enter 1 if want a new card. 
Enter 2 if want to stand:  
"""))
            if choise == 1:
                return Player.addCardToHand();
            elif choise == 2:
                return Player.stand();
            else:
                print("Choise a valid option")
                Player.playerGame(self, hand);
        else:
            return;
    
    def ensure():
        pass
    
    def divide():
        pass
    
    def addCardToHand():
        add = "ADD";
        return add;
       
    def stand():
        stand = "STAND"
        return stand;
    
    
    def double():
        pass
    
    def passed():
        passed = "PASSED"
        return passed;
    
    def blackjack():
        blackjack = "21"
        return blackjack;
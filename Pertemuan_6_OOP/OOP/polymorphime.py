import random

class Kartu(): 
    __SUIT = ["♣️","❤️","♠️","♦️"] 
    __RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    _total_kartu = 52
    __total_deck = 1
    __deck=[]

    def __init__(self,total_deck = 1): 
        self._total_kartu = total_deck
        for i in range(self.__total_deck):
            self.make_deck()
    
    def make_deck(self):
        for s in self.__SUIT:
            for r in self.__RANKS:
                card = (s,r)
                self.__deck.append(card)
        self._total_kartu = len(self.__deck)
        random.shuffle(self.__deck)
    
    def informasion(self):
        print(f"Jumlah Deck : {self.__total_deck}")
        print(f"Jumlah Kartu : {self._total_kartu}")
    
    def getCard(self):
        text = ""
        card = []
        card.append(self.__deck.pop())
        for s,r in card:
            text += "[" + r + s + " ]"
        return text
    
    def setDeck(self,total_deck):
        self.__deck = []
        self.__total_deck = total_deck
        for i in range(self.__total_deck):
            self.make_deck()

class BlackJack(Kartu):
    def informasion(self):
        print("=======BlackJack=======")
    
class Poker(Kartu):
    def informasion(self):
        print("=======Poker=======")
        


card = Kartu()
game1 = BlackJack()
game2 = Poker()

def informasion(Kartu): #polymorphisme
    Kartu.informasion()

informasion(card)
informasion(game1)
informasion(game2)



















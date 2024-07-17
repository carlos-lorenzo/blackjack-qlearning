from typing import List

from .deck import Deck
from .players import Dealer, Player

class Table:
    def __init__(self, ) -> None:
        self.players: List[Player] = []
        self.dealer = Dealer()
        self.deck = Deck()
        self.deck.shuffle()
        
    def add_player(self, player: Player) -> None:
        self.players.append(player)
    
    def add_players(self, players: List[Player]) -> None:
        self.players.extend(players)
   
    def start_turn(self) -> None:
        for player in self.players:
            player.clear_hand()
            
        self.dealer.clear_hand()
        
        self.dealer.hit(self.deck)
        self.dealer.hit(self.deck)
        
        
        if len([total for total in self.dealer.hand.possible_totals if total == 21]) > 0:
            pass # TODO
            # return
        
        for player in self.players:
            player.hit(self.deck)
            player.hit(self.deck)
        
    
    def play_turn(self) -> None:
        for player in self.players:
            while player.playing:  
                action = str(input("Enter 'h' to hit, 's' to stand: "))
                player.play(action, self.deck)
                
                
        
        self.dealer.play(self.deck)
            
        
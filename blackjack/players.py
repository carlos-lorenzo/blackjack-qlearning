from .hand import Hand
from .deck import Deck

class BasePlayer:
    def __init__(self) -> None:
        self.hand = Hand()
        self.playing: bool = True
    
    
    def __hash__(self) -> int:
        return id(self)
    
    def hit(self, deck: Deck) -> None:
        self.hand.add_card(deck.draw())
        
        self.playing = self.hand.total < 21
            
        
    def stand(self) -> None:
        self.playing = False
        
    def clear_hand(self) -> None:
        self.hand = Hand()
    
    def display_hand(self) -> None:
        print(f"{self.hand} - Total: {self.hand.total}")
        
        
class Dealer(BasePlayer):
    def __init__(self) -> None:
        super().__init__()
    
    @property
    def partial_total(self) -> int:
        return self.hand.cards[0].value.value[0]
    
        
    def play(self, deck: Deck) -> None:
        while self.hand.total < 17:
            self.hit(deck)
        self.stand()
    
    def display_hand_partial(self) -> None:
        print(f"{self.hand.cards[0]} - Total: +{self.partial_total}")
        

class Player(BasePlayer):
    def __init__(self) -> None:
        super().__init__()
        self.actions_taken = []
    
    def hit(self, deck: Deck, save_action: bool = True) -> None:
        initial_total = self.hand.total
        usable_ace = self.hand.usable_ace
        self.hand.add_card(deck.draw())
        
        self.playing = self.hand.total < 21
        
        if save_action:
            self.actions_taken.append({
                "action": 1,
                "total": initial_total,
                "usable_ace": usable_ace,
                "new_total": self.hand.total,
                "reward": 0
            })
        
    def stand(self) -> None:
        self.playing = False
        
        self.actions_taken.append({
            "action": 0,
            "total": self.hand.total,
            "usable_ace": self.hand.usable_ace,
            "new_total": self.hand.total,
            "reward": 0
        })
        
    def play(self, deck: Deck, action: int) -> None:
        if action == 1:
            self.hit(deck)
        elif action == 0:
            self.stand()
        else:
            raise ValueError("Invalid action")
        
    
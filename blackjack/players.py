from typing import List, Dict
from enum import Enum
from dataclasses import dataclass

from .hand import Hand
from .deck import Deck
from .card import Card

class Action(Enum):
    HIT = 0
    STAND = 1

class BasePlayer:
    def __init__(self) -> None:
        self.hand = Hand()
        self.playing: bool = True
        
    def hit(self, deck: Deck) -> None:
        self.hand.add_card(deck.draw())
        
        self.playing = min([total for total in self.hand.possible_totals]) < 21
            
        
    def stand(self) -> None:
        self.playing = False
        
    def clear_hand(self) -> None:
        self.hand = Hand()
    
    def display_hand(self) -> None:
        for total in self.hand.possible_totals:
            print(f"{self.hand} - Total: {total}")

class Dealer(BasePlayer):
    def __init__(self) -> None:
        super().__init__()

    
    def play(self, deck: Deck) -> None:
        while max(self.hand.possible_totals) < 17:
            self.hit(deck)
        self.stand()
        
        
    
    def display_hand_partial(self) -> None:
        print(f"{self.hand.cards[0]} - Total: ???")
        
    @property
    def partial_total(self) -> int:
        return self.hand.cards[0].value.value[0]
    
    @property
    def total(self) -> int:
        return max(self.hand.possible_totals)
        
    

class Player(BasePlayer):
    def __init__(self) -> None:
        super().__init__()
        # self.bet = 0
        
    def play(self, action: str, deck: Deck) -> None:
        if action.lower()[0] == "h":
            self.hit(deck)
            
        elif action.lower()[0] == "s":
            self.stand()
            
        else:
            raise ValueError("Invalid action")

class RecursivePlayer(BasePlayer):
    def __init__(self, chosen_total: int, hand: Hand, actions_taken: List[Dict[str, Action | int]] = [], playing: bool = True) -> None:
        #super().__init__()
        self.chosen_total = chosen_total
        self.hand = hand
        self.actions_taken = actions_taken
        self.playing = playing
        
    @property
    def total(self) -> int:
        return self.chosen_total
    
    @property
    def possible_totals(self) -> List[int]:
        return self.hand.possible_totals
    
    
    def hit(self, new_card: Card) -> None:
        self.hand.add_card(new_card)
        self.actions_taken.append({
            "action": Action.HIT,
            "total": self.chosen_total,
            "reward": 0 # TBD
        })
        
        self.playing = min(self.hand.possible_totals) < 21
            
        
    def stand(self) -> None:
        self.playing = False
        
        self.actions_taken.append({
            "action": Action.STAND,
            "total": self.chosen_total,
            "reward": 0 # TBD
        })
        
        
    
        
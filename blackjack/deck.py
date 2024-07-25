from dataclasses import dataclass, field
from typing import List

from .card import Card, Suit, Value, values

@dataclass
class Deck:
    n_full_decks: int = field(default=6)
    cards: List[Card] = field(default_factory=list)
    
    def __post_init__(self) -> None:
        for suit in Suit:
            for value in values.values():
                
                self.cards.append(Card(suit, value))
        self.shuffle()
        
    def __len__(self) -> int:
        return len(self.cards)
    
    def reset(self):
        self.cards = []
        self.__post_init__()
    
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    
    def draw(self) -> Card:
        return self.cards.pop()
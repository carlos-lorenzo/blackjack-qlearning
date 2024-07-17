from dataclasses import dataclass, field
from typing import List

from .card import Card, Suit, Value, values

@dataclass
class Deck:
    n_full_decks: int = field(default=6)
    cards: List[Card] = field(default_factory=list)
    
    def __post_init__(self) -> None:
        for suit in Suit:
            for name, value in values.items():
                self.cards.append(Card(suit, Value(name, value)))
        self.shuffle()
        
    def __len__(self) -> int:
        return len(self.cards)
    
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    
    def draw(self) -> Card:
        return self.cards.pop()
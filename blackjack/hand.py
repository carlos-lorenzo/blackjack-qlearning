from dataclasses import dataclass, field
from typing import List

from .card import Card, Suit, Value


@dataclass
class Hand:
    cards: List[Card] = field(default_factory=list)
    n_aces: int = field(init=False, default=0)

    def __str__(self) -> str:
        return ", ".join([str(card) for card in self.cards])
    
    @property
    def usable_ace(self) -> bool:
        return self.n_aces > 0 and self.total_without_ace <= 10
    
    @property
    def total_without_ace(self) -> int:
        return sum([card.value.value[0] for card in self.cards if card.value.name != "ACE"])
    
    @property
    def total(self) -> int:
        ace_sum = (self.n_aces - 1) * 1
        ace_sum += 11 if self.usable_ace else 1
        return self.total_without_ace + ace_sum
    
    def add_card(self, card: Card):
        self.cards.append(card)
        
        if card.value.name == "ACE":
            self.n_aces += 1
        
        return card
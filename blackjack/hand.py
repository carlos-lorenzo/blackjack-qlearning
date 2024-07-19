from dataclasses import dataclass, field
from typing import List

from .card import Card, Suit, Value, values


@dataclass
class Hand:
    cards: List[Card] = field(default_factory=list)


    def __str__(self) -> str:
        return ", ".join([str(card) for card in self.cards])
    
    @property
    def possible_totals(self) -> List[int]:
        n_aces = len([card for card in self.cards if card.value.name == "ACE"])
        n_possible_totals = n_aces + 1 # Pascalls triangle
        non_ace_total = sum([card.value.value[0] for card in self.cards if card.value.name != "ACE"])
        totals = [non_ace_total for _ in range(n_possible_totals)]
    
        for k in range(1, n_possible_totals + 1):
            totals[k - 1] += (k - 1) * 1 + (n_possible_totals - k) * 11
        return totals   
    
    def add_card(self, card: Card):
        self.cards.append(card)
        return card
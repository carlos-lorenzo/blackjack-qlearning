from dataclasses import dataclass
from typing import List
from enum import Enum
from collections import OrderedDict

class Suit(Enum):
    SPADES = 1
    DIAMONDS = 2
    CLUBS = 3
    HEARTS = 4

@dataclass
class Value:
    name: str
    value: List[int]

@dataclass
class Card:
    suit: Suit
    value: Value
    
    def __str__(self) -> None:
        return f"{self.value.name} of {self.suit.name}"
    
    

values = OrderedDict()
values["ACE"] = [1, 11]
values["TWO"] = [2]
values["THREE"] = [3]
values["FOUR"] = [4]
values["FIVE"] = [5]
values["SIX"] = [6]
values["SEVEN"] = [7]
values["EIGHT"] = [8]
values["NINE"] = [9]
values["TEN"] = [10]
values["JACK"] = [10]
values["QUEEN"] = [10]
values["KING"] = [10]

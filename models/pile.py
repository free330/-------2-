# models/pile.py
from models.card import Card


class Pile:
    """牌堆基类"""
    def __init__(self, cards=None):
        self.cards = cards if cards else []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def top_card(self):
        return self.cards[-1] if self.cards else None

    def is_empty(self):
        return len(self.cards) == 0

    def size(self):
        return len(self.cards)

    def to_dict(self):
        return [c.to_dict() for c in self.cards]

    @classmethod
    def from_dict(cls, data):
        cards = [Card.from_dict(c) for c in data]
        return cls(cards)
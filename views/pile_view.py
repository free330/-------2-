# views/pile_view.py
import pygame
from .card_view import CardView
from configs.setting import CARD_WIDTH, CARD_HEIGHT

class PileView:
    def __init__(self, pile, x, y, offset_y=20):
        self.pile = pile
        self.x = x
        self.y = y
        self.offset_y = offset_y
        self.card_views = []
        self._update_card_views()

    def _update_card_views(self):
        self.card_views = []
        for i, card in enumerate(self.pile.cards):
            cv = CardView(card, self.x, self.y + i * self.offset_y)
            self.card_views.append(cv)

    def draw(self, surface):
        for cv in self.card_views:
            cv.draw(surface)

    def get_card_view_at(self, pos):
        for cv in reversed(self.card_views):
            if cv.is_clicked(pos):
                return cv
        return None

    def update_positions(self):
        self._update_card_views()
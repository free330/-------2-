# models/tableau_pile.py
from .pile import Pile

class TableauPile(Pile):
    """桌面列，只有最底部牌翻开"""
    def __init__(self, cards=None):
        super().__init__(cards)
        if cards:
            for card in cards[:-1]:
                card.face_up = False
            cards[-1].face_up = True

    def add_card(self, card):
        super().add_card(card)
        card.face_up = True   # 添加到顶部的牌总是翻开

    def remove_card(self, card):
        # 只能移除顶部牌，所以移除后新的顶部牌翻开
        idx = self.cards.index(card)
        super().remove_card(card)
        if idx == len(self.cards):  # 原来就是顶部
            if self.cards:
                self.cards[-1].face_up = True
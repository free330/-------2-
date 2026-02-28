# models/stock_pile.py
from .pile import Pile

class StockPile(Pile):
    """备用牌堆，牌面朝下"""
    def draw_card(self):
        """抽一张牌（从顶部）"""
        if self.cards:
            return self.cards.pop()
        return None
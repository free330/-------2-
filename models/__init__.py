# models/__init__.py
from .tableau_pile import TableauPile
from .hand_pile import HandPile
from .stock_pile import StockPile

class GameModel:
    def __init__(self, tableau, hand, stock):
        self.tableau = tableau
        self.hand = hand
        self.stock = stock
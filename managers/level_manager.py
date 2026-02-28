# managers/level_manager.py
from models.card import Card
from models.tableau_pile import TableauPile
from models.hand_pile import HandPile
from models.stock_pile import StockPile

class LevelManager:
    @staticmethod
    def load_level(level_id):
        """根据关卡ID生成GameModel"""
        # 示例关卡1：简单布局
        tableau = [
            TableauPile([Card(0, 5, False), Card(1, 6, False)]),
            TableauPile([Card(2, 4, False)]),
            TableauPile([Card(3, 7, False)]),
        ]
        hand = HandPile([Card(0, 5, True)])  # 底牌
        stock = StockPile([
            Card(1, 2), Card(2, 3), Card(3, 8)
        ])
        # 所有牌初始坐标由视图设置，此处不处理
        return {'tableau': tableau, 'hand': hand, 'stock': stock}
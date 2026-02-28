# services/move_service.py
from .match_service import MatchService

class MoveService:
    def __init__(self, model):
        self.model = model

    def move_from_tableau_to_hand(self, tableau_idx, card, from_pos, to_pos):
        """将桌面牌移至手牌区，返回移动记录（含坐标）"""
        hand_top = self.model.hand.top_card()
        if not hand_top or not MatchService.can_match(hand_top, card):
            return None

        # 执行移动
        self.model.tableau[tableau_idx].remove_card(card)
        self.model.hand.add_card(card)

        move_record = {
            'type': 'tableau_to_hand',
            'tableau_idx': tableau_idx,
            'card': card,
            'from_pos': from_pos,
            'to_pos': to_pos
        }
        return move_record

    def draw_from_stock(self, from_pos, to_pos):
        """从备用牌堆抽一张牌到手牌区，返回移动记录"""
        if self.model.stock.is_empty():
            return None
        card = self.model.stock.draw_card()
        card.face_up = True
        self.model.hand.add_card(card)

        move_record = {
            'type': 'stock_to_hand',
            'card': card,
            'from_pos': from_pos,
            'to_pos': to_pos
        }
        return move_record
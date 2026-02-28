# controllers/game_controller.py
import pygame
from services.move_service import MoveService
from services.history_service import HistoryService
from controllers.animation_controller import AnimationController
from controllers.turn_controller import TurnController

class GameController:
    def __init__(self, model, view, event_dispatcher):
        self.model = model
        self.view = view
        self.event_dispatcher = event_dispatcher
        self.move_service = MoveService(model)
        self.history = HistoryService()
        self.turn_ctrl = TurnController(model, self.move_service, self.history)
        self.anim_ctrl = AnimationController()

        self.event_dispatcher.register('CARD_CLICKED', self.on_card_clicked)

    def on_card_clicked(self, data):
        if self.anim_ctrl.is_animating():
            return
        self.process_click(data)

    def process_click(self, clicked):
        if clicked is None:
            return
        obj_type, idx, card = clicked
        record = None

        if obj_type == 'tableau':
            from_pos = self.view.get_card_position(card)
            to_pos = self.view.get_hand_top_position()
            record = self.turn_ctrl.handle_tableau_click(idx, card, from_pos, to_pos)
        elif obj_type == 'hand':
            # 点击手牌区：从备用牌堆抽牌
            from_pos = self.view.get_stock_top_position()
            to_pos = self.view.get_hand_top_position()
            record = self.turn_ctrl.handle_hand_click(from_pos, to_pos)
        # stock 点击暂不处理

        if record:
            self._animate_move(record)
            self.view.update_views()

    def _animate_move(self, record):
        card = record['card']
        cv = self._find_card_view(card)
        if cv:
            self.anim_ctrl.add_move_animation(
                cv, record['from_pos'], record['to_pos'], 0.3
            )

    def _find_card_view(self, card):
        """查找与 card 关联的 CardView（用于动画）"""
        for tv in self.view.tableau_views:
            for cv in tv.card_views:
                if cv.card == card:
                    return cv
        for cv in self.view.hand_view.card_views:
            if cv.card == card:
                return cv
        for cv in self.view.stock_view.card_views:
            if cv.card == card:
                return cv
        return None

    def undo(self):
        if self.anim_ctrl.is_animating():
            return
        record = self.turn_ctrl.undo()
        if not record:
            return

        if record['type'] == 'tableau_to_hand':
            card = record['card']
            self.model.hand.remove_card(card)
            self.model.tableau[record['tableau_idx']].add_card(card)
            # 反向动画
            self._animate_move({
                'card': card,
                'from_pos': record['to_pos'],
                'to_pos': record['from_pos']
            })
        elif record['type'] == 'stock_to_hand':
            card = record['card']
            self.model.hand.remove_card(card)
            self.model.stock.add_card(card)
            card.face_up = False
            self._animate_move({
                'card': card,
                'from_pos': record['to_pos'],
                'to_pos': record['from_pos']
            })
        self.view.update_views()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.anim_ctrl.is_animating():
                return
            pos = pygame.mouse.get_pos()
            self.view.handle_click(pos)

    def update(self, dt):
        self.anim_ctrl.update(dt)
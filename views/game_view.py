# views/game_view.py
import pygame
from .pile_view import PileView
from configs.setting import SCREEN_WIDTH, SCREEN_HEIGHT

class GameView:
    def __init__(self, model, event_dispatcher):
        self.model = model
        self.event_dispatcher = event_dispatcher
        self.tableau_views = []
        self.hand_view = None
        self.stock_view = None
        self.init_views()

    def init_views(self):
        start_x = 100
        for i, pile in enumerate(self.model.tableau):
            pv = PileView(pile, start_x + i * 120, 200, offset_y=30)
            self.tableau_views.append(pv)

        self.hand_view = PileView(self.model.hand, SCREEN_WIDTH//2 - 40, 400, offset_y=0)
        self.stock_view = PileView(self.model.stock, 50, 50, offset_y=0)

    def draw(self, surface):
        surface.fill((0, 100, 0))
        for tv in self.tableau_views:
            tv.draw(surface)
        self.hand_view.draw(surface)
        self.stock_view.draw(surface)

    def handle_click(self, pos):
        clicked = self._detect_click(pos)
        if clicked:
            self.event_dispatcher.dispatch('CARD_CLICKED', clicked)

    def _detect_click(self, pos):
        for i, tv in enumerate(self.tableau_views):
            cv = tv.get_card_view_at(pos)
            if cv:
                return ('tableau', i, cv.card)
        cv = self.hand_view.get_card_view_at(pos)
        if cv:
            return ('hand', None, cv.card)
        cv = self.stock_view.get_card_view_at(pos)
        if cv:
            return ('stock', None, cv.card)
        return None

    def get_hand_top_position(self):
        """返回手牌区顶部卡牌的坐标（若无牌则返回牌堆起始位置）"""
        if self.hand_view.card_views:
            last_cv = self.hand_view.card_views[-1]
            return (last_cv.rect.x, last_cv.rect.y)
        else:
            return (self.hand_view.x, self.hand_view.y)

    def get_stock_top_position(self):
        """返回备用牌堆顶部卡牌的坐标"""
        if self.stock_view.card_views:
            last_cv = self.stock_view.card_views[-1]
            return (last_cv.rect.x, last_cv.rect.y)
        else:
            return (self.stock_view.x, self.stock_view.y)

    def get_card_position(self, card):
        """根据 card 查找对应的 CardView 并返回其坐标"""
        for tv in self.tableau_views:
            for cv in tv.card_views:
                if cv.card == card:
                    return (cv.rect.x, cv.rect.y)
        for cv in self.hand_view.card_views:
            if cv.card == card:
                return (cv.rect.x, cv.rect.y)
        for cv in self.stock_view.card_views:
            if cv.card == card:
                return (cv.rect.x, cv.rect.y)
        return None

    def update_views(self):
        for tv in self.tableau_views:
            tv.update_positions()
        self.hand_view.update_positions()
        self.stock_view.update_positions()
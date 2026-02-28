# controllers/animation_controller.py
import pygame
from utils.interpolator import Interpolator

class AnimationController:
    def __init__(self):
        self.animations = []

    def add_move_animation(self, card_view, from_pos, to_pos, duration, callback=None):
        anim = {
            'card_view': card_view,
            'interp': Interpolator(from_pos, to_pos, duration),
            'callback': callback
        }
        self.animations.append(anim)

    def update(self, dt):
        for anim in self.animations[:]:
            anim['interp'].update(dt)
            x, y = anim['interp'].value
            anim['card_view'].set_position(x, y)
            if anim['interp'].finished:
                if anim['callback']:
                    anim['callback']()
                self.animations.remove(anim)

    def is_animating(self):
        return len(self.animations) > 0
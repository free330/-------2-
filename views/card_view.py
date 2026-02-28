# views/card_view.py
import pygame
from configs.setting import CARD_WIDTH, CARD_HEIGHT, CARD_BACK_COLOR, CARD_FRONT_COLOR

class CardView:
    def __init__(self, card, x, y):
        self.card = card
        self.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)

    def draw(self, surface):
        if self.card.face_up:
            pygame.draw.rect(surface, CARD_FRONT_COLOR, self.rect)
            font = pygame.font.SysFont('Arial', 24)
            text = f"{self.card.rank}{'♠♥♣♦'[self.card.suit]}"
            img = font.render(text, True, (0,0,0))
            surface.blit(img, self.rect.topleft)
        else:
            pygame.draw.rect(surface, CARD_BACK_COLOR, self.rect)
        pygame.draw.rect(surface, (0,0,0), self.rect, 2)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
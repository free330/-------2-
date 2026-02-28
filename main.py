# main.py
import pygame
from configs.setting import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from managers.level_manager import LevelManager
from models import GameModel
from views.game_view import GameView
from controllers.game_controller import GameController
from utils.event_dispatcher import EventDispatcher

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    event_dispatcher = EventDispatcher()

    level_data = LevelManager.load_level(1)
    model = GameModel(**level_data)

    view = GameView(model, event_dispatcher)
    controller = GameController(model, view, event_dispatcher)

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    controller.undo()
            else:
                controller.handle_event(event)

        controller.update(dt)
        view.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
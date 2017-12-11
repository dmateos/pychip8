import pygame

class Video(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 320))

    def mainloop(self, callback):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            callback()
            pygame.display.flip()

    def draw(self, x, y, width):
        pass

from colors import Colors

import pygame
import ctypes


class Window(Colors):

    QUIT = pygame.QUIT

    def __init__(self, caption):

        pygame.font.init()
        pygame.mixer.init()

        """Get screen resolution"""
        user32 = ctypes.windll.user32
        self.width = user32.GetSystemMetrics(0)
        self.height = user32.GetSystemMetrics(1)
        self.Win = pygame.display.set_mode((self.width, self.height))
        self.leftBoundary = 0
        self.rightBoundary = self.width
        self.topBoundary = 0
        self.bottomBoundary = self.height

        """Assign caption"""
        pygame.display.set_caption(caption)

        """Game mechanics"""
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.run = True
        pygame.event.clear()


    def get_event(self):
        return pygame.event.get()

    def quit(self):
        pygame.quit()

    def check_quit(self):
        for event in self.get_event():
            if event.type == self.QUIT:
                self.run = False
                self.quit()

    def draw(self, surface=None):
        self.Win.fill(self.White)
        if surface != None:
            for item in surface:
                self.Win.blit(*item)
        pygame.display.update()


    def inputs(self):
        self.keysPressed = pygame.key.get_pressed()

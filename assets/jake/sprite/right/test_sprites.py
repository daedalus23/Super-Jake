import pygame
import os

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 600
screen_height = 800

background = pygame.transform.scale(
    pygame.image.load(r"C:\Users\Jamies-Main\PycharmProjects\Super-Jake\assets\jake\sprite\background\background.png"),
    (screen_width, screen_height))
background_rect = background.get_rect()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Testing Sprites")

bg = (50, 50, 50)

def draw_bg():
    screen.fill(bg)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        listDir = os.listdir(os.curdir)
        for img in listDir:
            if img[-2:] != "py":
                self.images.append(pygame.image.load(os.path.join(os.curdir, img)))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

        self.start = 0
        self.spriteFPS = 120


    def update(self):
        # explosion_speed = 20
        # self.counter += 1
        # if self.counter >= explosion_speed and self.index < len(self.images) - 1:
        #     self.counter = 0
        #     self.index += 1
        #     self.image = self.images[self.index]
        #
        # if self.index >= len(self.images) and self.counter >= explosion_speed:
        #     self.kill()

        ticks = pygame.time.get_ticks()
        if ticks - self.start > self.spriteFPS:
            self.index += 1
            self.start = ticks

        if self.index >= len(self.images):
           self.index = 0

        self.image = self.images[self.index]


def main():

    run = True

    explosion = Explosion(300, 510)
    explosion_group = pygame.sprite.Group(explosion)


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        clock.tick(fps)
        draw_bg()
        screen.blit(background, background_rect)
        screen.blit(background, background_rect.move(background_rect.width, 0))
        background_rect.move_ip(-2, 0)
        if background_rect.right == 0:
            background_rect.x = 0


        explosion_group.update()
        explosion_group.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()

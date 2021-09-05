from jake import PlayerOne
from window import Window

import pygame


def main():
    Win = Window("Buck Dunker")
    playerOne = PlayerOne()


    while Win.run:
        Win.clock.tick(Win.FPS)
        Win.check_quit()
        Win.inputs()
        Win.draw()
        playerOne.draw(Win)

if __name__ == "__main__":
    main()
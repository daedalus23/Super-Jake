import pygame
import time
import os


class PlayerOne:

    VEL = 15
    origin = {
        "x" : 500 ,
        "y" : 250
    }

    chestDest = origin["x"], origin["y"]
    headDest = origin["x"] + 35, origin["y"] - 70
    mouthDest = origin["x"] + 49, origin["y"] - 13
    leftThighDest = origin["x"] + 60, origin["y"] + 190
    leftArmDest = origin["x"] + 100, origin["y"] + 15
    rightArmDest = origin["x"] - 35, origin["y"] + 20
    rightThighDest = origin["x"] + 10, origin["y"] + 190
    leftLegDest = origin["x"] + 87, origin["y"] + 292
    rightLegDest = origin["x"] + 10, origin["y"] + 300


    def __init__(self):
        self.chestImg = pygame.image.load(os.path.join("assets/jake", "chest.png"))
        self.headImg = pygame.image.load(os.path.join("assets/jake", "head.png"))
        self.mouthImg = pygame.image.load(os.path.join("assets/jake", "mouth.png"))
        self.leftArmImg = pygame.image.load(os.path.join("assets/jake", "left_arm.png"))
        self.rightArmImg = pygame.image.load(os.path.join("assets/jake", "right_arm.png"))
        self.leftThighImg = pygame.transform.rotate(
            pygame.image.load(os.path.join("assets/jake", "left_thigh.png")),
            -10)  # Degrees rotated
        self.rightThighImg = pygame.image.load(os.path.join("assets/jake", "right_thigh.png"))
        self.leftLegImg = pygame.image.load(os.path.join("assets/jake", "left_leg.png"))
        self.rightLegImg = pygame.image.load(os.path.join("assets/jake", "right_leg.png"))

        self.chest = pygame.Rect(self.chestDest[0], self.chestDest[1], self.chestImg.get_width(), self.chestImg.get_height())
        self.head = pygame.Rect(self.headDest[0], self.headDest[1], self.headImg.get_width(), self.headImg.get_height())
        self.mouth = pygame.Rect(self.mouthDest[0], self.mouthDest[1], self.mouthImg.get_width(), self.mouthImg.get_height())
        self.leftArm = pygame.Rect(self.leftArmDest[0], self.leftArmDest[1], self.leftLegImg.get_width(), self.leftArmImg.get_height())
        self.rightArm = pygame.Rect(self.rightArmDest[0], self.rightArmDest[1], self.rightArmImg.get_width(), self.rightArmImg.get_height())
        self.leftThigh = pygame.Rect(self.leftThighDest[0], self.leftThighDest[1], self.leftThighImg.get_width(), self.leftThighImg.get_height())
        self.rightThigh = pygame.Rect(self.rightThighDest[0], self.rightThighDest[1], self.rightThighImg.get_width(), self.rightThighImg.get_height())
        self.leftLeg = pygame.Rect(self.leftLegDest[0], self.leftLegDest[1], self.leftLegImg.get_width(), self.leftLegImg.get_height())
        self.rightLeg = pygame.Rect(self.rightLegDest[0], self.rightLegDest[1], self.rightLegImg.get_width(), self.rightLegImg.get_height())

        self.build_body()


    def build_body(self) -> list:
        """Joins body image with rectangle"""
        self.playersBody = [
            [self.leftThighImg, self.leftThigh],
            [self.rightThighImg, self.rightThigh],
            [self.leftLegImg, self.leftLeg],
            [self.rightLegImg, self.rightLeg],
            [self.leftArmImg, self.leftArm],
            [self.rightArmImg, self.rightArm],
            [self.chestImg, self.chest],
            [self.headImg, self.head],
            [self.mouthImg, self.mouth]
        ]


    def player_controls(self, Window):
        self._move_left(Window)
        self._move_right(Window)
        self._move_up(Window)
        self._move_down(Window)
        self._yell(Window)


    def _move_left(self, Window):
        if Window.keysPressed[pygame.K_a] and self.rightArm.x > Window.leftBoundary:
            self.chest.x -= self.VEL
            self.head.x -= self.VEL
            self.mouth.x -= self.VEL
            self.leftArm.x -= self.VEL
            self.rightArm.x -= self.VEL
            self.leftThigh.x -= self.VEL
            self.rightThigh.x -= self.VEL
            self.leftLeg.x -= self.VEL
            self.rightLeg.x -= self.VEL


    def _move_right(self, Window):
        if Window.keysPressed[pygame.K_d] and (self.leftArm.x + self.leftArm.width) < Window.rightBoundary:
            self.chest.x += self.VEL
            self.head.x += self.VEL
            self.mouth.x += self.VEL
            self.leftArm.x += self.VEL
            self.rightArm.x += self.VEL
            self.leftThigh.x += self.VEL
            self.rightThigh.x += self.VEL
            self.leftLeg.x += self.VEL
            self.rightLeg.x += self.VEL


    def _move_up(self, Window):
        if Window.keysPressed[pygame.K_w] and self.head.y > Window.topBoundary:
            self.chest.y -= self.VEL
            self.head.y -= self.VEL
            self.mouth.y -= self.VEL
            self.leftArm.y -= self.VEL
            self.rightArm.y -= self.VEL
            self.leftThigh.y -= self.VEL
            self.rightThigh.y -= self.VEL
            self.leftLeg.y -= self.VEL
            self.rightLeg.y -= self.VEL


    def _move_down(self, Window):
        if Window.keysPressed[pygame.K_s] and (self.rightLeg.y + self.rightLeg.height) < Window.bottomBoundary:
            self.chest.y += self.VEL
            self.head.y += self.VEL
            self.mouth.y += self.VEL
            self.leftArm.y += self.VEL
            self.rightArm.y += self.VEL
            self.leftThigh.y += self.VEL
            self.rightThigh.y += self.VEL
            self.leftLeg.y += self.VEL
            self.rightLeg.y += self.VEL


    def _yell(self, Window):
        if Window.keysPressed[pygame.K_e]:  # yell
            self.mouth.y += 50
            time.sleep(1)
            self.mouth.y -= 50
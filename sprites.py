from pygame_functions import *
import random

class Player(newSprite):
    def __init__(self):
        newSprite.__init__(self, "LinkSimple.png", 14)
        self.rect.x = 500
        self.rect.y = 350
        self.speed = 4
    
    def move(self, frame):
        if self.orientation == 0:
            self.rect.y = self.rect.y + self.speed
            self.changeImage(0*2 + frame)
        elif self.orientation ==1:
            self.rect.y = self.rect.y - self.speed
            self.changeImage(1*2 + frame)
        elif self.orientation ==2:
            self.rect.x = self.rect.x + self.speed
            self.changeImage(2*2 + frame)
        else:
            self.rect.x = self.rect.x - self.speed
            self.changeImage(3*2 + frame)
            
    def sword(self):
        pass

class Enemy(newSprite):
    def __init__(self, filename, framesX=1, framesY=1):
        newSprite.__init__(self, filename, framesX, framesY)
        self.speed = 3
        self.rect.x = 200
        self.rect.y = 200
    def move(self, frame):
        if self.orientation == 0:
            self.rect.y = self.rect.y + self.speed
            self.changeImage(0 + frame *4)
        elif self.orientation ==1:
            self.rect.y = self.rect.y - self.speed
            self.changeImage(2 + frame*4)
        elif self.orientation ==2:
            self.rect.x = self.rect.x + self.speed
            self.changeImage(3 + frame*4)
        else:
            self.rect.x = self.rect.x - self.speed
            self.changeImage(1 + frame*4)
            
class Octorok(Enemy):
    def __init__(self):
        Enemy.__init__(self,"Octorok.png", 4, 2)
        self.orientation = random.randint(0,3)
        self.step = 0
    def move(self, frame):
        if self.step == 25:
            self.speed = 0
            
        if self.step == 40:
            self.orientation = random.randint(0,3)
            self.speed = 3
            self.step = 0
        if self.orientation == 0:
            self.rect.y = self.rect.y + self.speed
            self.changeImage(0 + frame *4)
        elif self.orientation ==1:
            self.rect.y = self.rect.y - self.speed
            self.changeImage(2 + frame*4)
        elif self.orientation ==2:
            self.rect.x = self.rect.x + self.speed
            self.changeImage(3 + frame*4)
        else:
            self.rect.x = self.rect.x - self.speed
            self.changeImage(1 + frame*4)
        self.step += 1
        
class Tektite(Enemy):
    def __init__(self):
        Enemy.__init__(self, "Tektite.png", 1, 2)
        self.time = 0
        self.speedx = 0
        self.speedy = 0
        self.jump = False
        
    def move(self, frame):
        if self.speedy <= 6 and self.jump == True:
            self.speedy += 1
        self.time += 1
        jumpFrame = 50
        
        if self.time == jumpFrame:
            self.jump = True
            self.speedy = random.randint(-14, -7)
            print(self.speedy)
            self.speedx = random.randint(-6, 6)
        
        if self.time == jumpFrame + 25:
            self.jump = False
            self.time = 0
            self.speedy = 0
            self.speedx = 0
            
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
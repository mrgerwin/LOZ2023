from pygame_functions import *
import random

def clock():
    current_time = pygame.time.get_ticks()
    return current_time

#class Rock(newSprite):
    #def __init__(self):
        #newSprite.__init__(self, "ROCKh.png", 10)
        

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
class WaterMonster(Enemy):
    def __init__(self):
        Enemy.__init__(self,"WaterMonster.png", 5, 1)
        self.orientation = 1
        self.frame = 0
        
    def move(self, frame):
        
        
        if self.frame <= 3:
            self.rect.x = random.randint(0,1024)
            self.rect.y = random.randint(0,768)
            self.changeImage(0)
            self.frame = self.frame +1
        elif self.frame <= 10:
            #self.frame = 0
            #elf.speed = 0
            #self.step = 0
            #self.frame = -1
            self.frame = self.frame +1
            self.changeImage(1)
        elif self.frame <= 15:
            self.frame = self.frame +1
            self.changeImage(2)
        elif self.frame <= 20:
            self.frame = self.frame +1
            self.changeImage(1)
        elif self.frame <= 35:
            self.frame = self.frame +1
            self.changeImage(3)
        elif self.frame <= 50:
            self.frame = self.frame +1
            self.changeImage(2)
        elif self.frame <= 60:
            self.frame = self.frame +1
            self.changeImage(1)
        elif self.frame <= 62:
            self.frame = self.frame +1
            self.changeImage(0)#gone:)
            self.frame =0
        #if self.frame == 3:
            #self.Originalimg = pygame.image.load("ROCKh.png")
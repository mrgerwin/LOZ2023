from pygame_functions import *
import random
import math

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
    def moveTo(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Enemy(newSprite):
    def __init__(self, filename, framesX=1, framesY=1):
        newSprite.__init__(self, filename, framesX, framesY)
        self.speed = 3
        self.rect.x = 200
        self.rect.y = 200
    def move(self, frame, link=None):
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
    
    def moveTo(self, x, y):
        self.rect.x = x
        self.rect.y = y
            
class Octorok(Enemy):
    def __init__(self):
        Enemy.__init__(self,"Octorok.png", 4, 2)
        self.orientation = random.randint(0,3)
        self.step = 0
    def move(self, frame, link):
        rock = None
        if self.step == 25:
            self.speed = 0
            
        #Shooting
        if self.step == 30:
            rock = TargetRock(link)
            rock.moveTo(self.rect.x, self.rect.y)
            
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
        return rock

class Leever(Enemy):
    def __init__(self):
        Enemy.__init__(self,"Leever.png", 6, 1)
        self.orientation = random.randint(0,3)
        self.step = 0
        self.changeImage(0)
    def move(self, frame, link=None):
        if self.step == 25:
            pass
            
        if self.step == 40:
            self.orientation = random.randint(0,3)
            self.speed = 3
            self.step = 0
        elif self.rect.x>=998:
            self.rect.x =995
            self.rect.x = self.rect.x - self.speed
            self.changeImage(4+frame)
        elif self.rect.x<=24:
            self.rect.x = 27
            self.rect.x = self.rect.x + self.speed
            self.changeImage(4+frame)
        elif self.orientation ==1:
            self.rect.x = self.rect.x + self.speed
            self.changeImage(4+frame)
        elif self.orientation ==2:
            self.rect.x = self.rect.x + self.speed
            self.changeImage(4+frame)
        else:
            self.rect.x = self.rect.x - self.speed
            self.changeImage(4+frame)
        self.step += 1 
    def spawn(self,leever,frame):
        self.changeImage(0)
        pause(125)
        self.changeImage(1)
        pause(125)
        self.changeImage(2)
        pause(125)
        self.changeImage(3)
        pause(125)
        self.changeImage(4)
        pause(125)


class wizzrobe(Enemy):
    def __init__(self):
        Enemy.__init__(self, "blueghost2.png", 3, 2)
        self.orientation = random.randint(0, 3)
        self.step = 0
        self.ShootReady = False
        
    
    def move(self, frame, link=None):
        if frame % 2 == 0:
            self.step += 1
            if self.ShootReady:
                self.Shoot(frame)
                self.ShootReady = False
        if self.step == 25:
            self.rect.x = random.randint(50, 950)
            self.rect.y = random.randint(75, 600)
            self.step = 0
            
        if self.step < 4:
            self.changeImage(3 + self.step % 3)
            
        elif self.step == 5:
            self.ShootReady = True
        else:
            self.changeImage(0)
        
        
        
            
            
        
    def Shoot(self, frame):
        if self.ShootReady == True:
            return
            print("I'm going to shoot now")
            """
            Spellball = newSprite("Spellball.png")
            Spellball.rect.x = self.rect.x
            Spellball.rect.y = self.rect.y
            ShootReady = False
            showSprite(Spellball)
            return Spellball
            """
        
        return None
    """
    def Spellballmove(frame, playerx, playery):
        global Spellball
        if playerx < Spellball.x:
            Spellball.x += 1
        if playerx > Spellball.x:
            Spellball.x -= 1
        if playery < Spellball.y:
            Spellball.y -= 1
        if playery > Spellball.y:
            Spellball.y += 1
    """            
                    
class Tektite(Enemy):
    def __init__(self):
        Enemy.__init__(self, "Tektite.png", 1, 2)
        self.time = 0
        self.speedx = 0
        self.speedy = 0
        self.jump = False
        
    def move(self, frame, link=None):
        if self.speedy <= 6 and self.jump == True:
            self.speedy += 1
        self.time += 1
        jumpFrame = 50
        
        if self.time == jumpFrame:
            self.jump = True
            self.speedy = random.randint(-14, -7)
            self.speedx = random.randint(-6, 6)
        
        if self.time == jumpFrame + 25:
            self.jump = False
            self.time = 0
            self.speedy = 0
            self.speedx = 0
            
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
class Sword(newSprite):
    def __init__(self, filename, framesX=1, framesY=1):
        newSprite.__init__(self, filename, framesX, framesY)
        self.orientation = 0
        self.rect.x = 0
        self.rect.y = 0
    
    def facing(self):
        self.changeImage(self.orientation)
        
    def moveTo(self, x, y):
        self.rect.x = x
        self.rect.y = y
    
    def stab(self, x, y, orientation):
        z = 0
        w = 0
        
        if orientation - 2 < 0:
            z = 32
        else:
            w = 32
        
        if orientation%2 == 1:
            z *= -1
            w *= -1
            
        self.orientation = orientation
        self.rect.x = x + w
        self.rect.y = y + z
        
class BlueOctorok(Enemy):
    def __init__(self):
        Enemy.__init__(self,"BlueOctorok.png",8,1)
        self.orientation = random.randint(0,3)
        self.step = 0
    def move(self, frame, link=None):
        if self.step == 15:
            self.speed = 0
            
        if self.step == 40:
            self.orientation = random.randint(0,4)
            self.speed = 6
            self.step = 0
        if self.orientation == 0:
            self.rect.y = self.rect.y + self.speed
            self.changeImage(0 + frame )
        elif self.orientation ==1:
            self.rect.y = self.rect.y - self.speed
            self.changeImage(2 + frame )
        elif self.orientation ==2:
            self.rect.x = self.rect.x + self.speed
            self.changeImage(4 + frame )
        else:
            self.rect.x = self.rect.x - self.speed
            self.changeImage(6 + frame )
        self.step += 1
        
class WaterMonster(Enemy):
    def __init__(self):
        Enemy.__init__(self,"WaterMonster.png", 5, 1)
        self.orientation = 1
        self.frame = 0
        
    def move(self, frame, link=None):
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

        
class Projectile(newSprite):
    def __init__(self, filename, framesX=1, framesY=1):
        newSprite.__init__(self,filename, framesX, framesY)
        self.speed = 3
        
    def move(self, frame):
        if self.orientation == 0:
            self.rect.y = self.rect.y + self.speed
        elif self.orientation ==1:
            self.rect.y = self.rect.y - self.speed
        elif self.orientation ==2:
            self.rect.x = self.rect.x + self.speed
        else:
            self.rect.x = self.rect.x - self.speed
            
        self.changeImage(frame)
    
    def moveTo(self, x, y):
        self.rect.x = x
        self.rect.y = y
        
class Rock(Projectile):
    def __init__(self):
        Projectile.__init__(self,"Rocks.png", 2, 1)

class TargetRock(Projectile):
    def __init__(self, link):
        Projectile.__init__(self, "Rocks.png", 2, 1)
        self.speed = 4
        self.quad = 0
        self.angle = 0
        self.link = link
        
        if (self.rect.x - link.rect.x) > 0:
            #link is to the left
            if (self.rect.y - link.rect.y)>0:
                #link is above
                print("Link is left and above")
                self.quad = 2
            else:
                #link is below
                print("Link is left and below")
                self.quad = 3
        else:
            #link is to the right
            if (self.rect.y - link.rect.y)>0:
                #link is above
                print("Link is right and above")
                self.quad = 1
            else:
                #link is below
                print("Link is right and below")
                self.quad = 4 
        
        self.angle = math.atan((self.rect.y-link.rect.y)/(self.rect.x-link.rect.x))
        
        
        #print(self.angle)
    def move(self, frame):
        deltaX = self.speed * math.cos(self.angle)
        deltaY = self.speed * math.sin(self.angle)
        
        if self.quad == 3 or self.quad == 2:
            deltaY = -deltaY
            deltaX = -deltaX
            
        self.rect.x += deltaX
        self.rect.y += deltaY
    
    def moveTo(self, x, y):
        
        self.rect.x = x
        self.rect.y = y
        
        if (self.rect.x - self.link.rect.x) > 0:
            #link is to the left
            if (self.rect.y - self.link.rect.y)>0:
                #link is above
                print("Link is left and above")
                self.quad = 2
            else:
                #link is below
                print("Link is left and below")
                self.quad = 3
        else:
            #link is to the right
            if (self.rect.y - self.link.rect.y)>0:
                #link is above
                print("Link is right and above")
                self.quad = 1
            else:
                #link is below
                print("Link is right and below")
                self.quad = 4 
        
        self.angle = math.atan((self.rect.y-self.link.rect.y)/(self.rect.x-self.link.rect.x))
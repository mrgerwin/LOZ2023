import pygame.display
from pygame_functions import *
import random
from os import path
import base64
import math


def ItemDrop(enemy):
    #0 yellow Rupee
    #1 heart
    #2 Blue Rupee
    #3 Fairy
    #4 Bomb
    #5 Clock
    if enemy == None:
        return None
    
    A= [0, 1, 0, 3, 0, 1, 1, 0, 0, 1]
    B= [4, 0, 5, 0, 1, 4, 0, 4, 1, 1]
    C = [0, 1, 0, 2, 1, 5, 0, 0, 0, 2]
    D = [1, 3, 0, 1, 3, 1, 1, 1, 0, 1]
    
    if enemy.type == "A":
        itemNum = A[enemy.link.kills]
    elif enemy.type == "B":
        itemNum = B[enemy.link.kills]
    elif enemy.type == "C":
        itemNum = C[enemy.link.kills]
    elif enemy.type == "D":
        itemNum = D[enemy.link.kills]
    
    if itemNum == 0:
        return Rupee(enemy.link)
    elif itemNum == 1:
        return Heart(enemy.link)
    elif itemNum == 2:
        return BlueRupee(enemy.link)
    elif itemNum == 3:
        return Fairy(enemy.link)
    elif itemNum == 4:
        return Bomb(enemy.link)
    elif itemNum == 5:
        return Clock(enemy.link)
            
class Player(newSprite):
    def __init__(self):
        newSprite.__init__(self, "LinkSimple.png", 14)
        self.rect.x = 500
        self.rect.y = 350
        self.speed = 0
        self.money = 0
        self.Bomb = 3
        self.health=3
        self.orientation = 0
        self.kills = 0
        
    def hit(self,enemy, ded):
        #print (llorientation)
        if self.health <= 0:
            #Die Animation
            changeSpriteImage(self, 0)
            pause(125)
            changeSpriteImage(self, 5)
            pause(125)
            changeSpriteImage(self, 2)
            pause(125)
            changeSpriteImage(self, 6)
            pause(125)
            changeSpriteImage(self, 0)
            pause(125)
            changeSpriteImage(self, 5)
            pause(125)
            changeSpriteImage(self, 2)
            pause(125)
            changeSpriteImage(self, 6)
            pause(125)
            changeSpriteImage(self, 0)
            pause(125)
            changeSpriteImage(self, 5)
            pause(125)
            changeSpriteImage(self, 2)
            pause(125)
            changeSpriteImage(self, 6)
            pause(125)
            changeSpriteImage(self, 0)
            pause(125)
            changeSpriteImage(self, 5)
            pause(125)
            changeSpriteImage(self, 2)
            pause(125)
            changeSpriteImage(self, 6)
            pause(125)
        elif self.orientation ==0:
            self.rect.y -=32
            self.health= self.health - 0.5
        elif self.orientation ==1:
            self.rect.y +=32
            self.health= self.health - 0.5
        elif self.orientation ==2:
            self.rect.x -=32
            self.health= self.health - 0.5
        elif self.orientation ==3:
            self.rect.x +=32
            self.health= self.health - 0.5

    def move(self, frame):
        if self.speed == 0:
            pass
        else:
        
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
        self.link = None
        self.type = "A"
    def move(self, frame, link):
        self.link = link
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
    

    def hit(self, lorientation):
        self.health -=1
        if self.health <= 0:
            killSprite(self)
        elif lorientation ==0:
            self.rect.y +=32
        elif lorientation ==1:
            self.rect.y -=32
        elif lorientation ==2:
            self.rect.x +=32
        elif lorientation ==3:
            self.rect.x -=32
        if self.health <= 0:
            item = ItemDrop(self)
            moveSprite(item, self.rect.x, self.rect.y)
            return item

class DarkMoblin(Enemy):
    def __init__(self):
        Enemy.__init__(self,"DarkMoblin.png", 8, 1)
        self.orientation = random.randint(0,3)
        self.step = 0
        self.health = 3
        self.type = "B"
    def move(self, frame, link=None):
        self.link = link
        a_arrow = None
        if self.step == 25:
            self.speed = 0
            a_arrow = AArrow()
            a_arrow.rect.x = self.rect.x
            a_arrow.rect.y = self.rect.y
            a_arrow.orientation = self.orientation
            showSprite(a_arrow)
            #backgroundMusic=makeSound("harderBetterFasterWhopper.mp3")
            
            
        if self.step == 40:
            self.orientation = random.randint(0,4)
            self.speed = 6
            self.step = 0
        if self.orientation == 0:
            self.rect.y = self.rect.y + self.speed
            self.changeImage(0 + frame )
        elif self.rect.x>=998:
            self.rect.x =995
            self.orientation=3
        elif self.rect.x<=24:
            self.rect.x = 27
            self.orientation=2
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
    
        return a_arrow


class Moblin(Enemy):
    def __init__(self):
        Enemy.__init__(self,"Moblin.png", 8, 1)
        self.orientation = random.randint(0,3)
        self.step = 0
        self.health = 2
    def move(self, frame, link=None):
        self.link = link
        a_arrow = None
        if self.step == 25:
            self.speed = 0
            a_arrow = AArrow()
            a_arrow.rect.x = self.rect.x
            a_arrow.rect.y = self.rect.y
            a_arrow.orientation = self.orientation
            showSprite(a_arrow)
            #backgroundMusic=makeSound("harderBetterFasterWhopper.mp3")
            
            
        if self.step == 40:
            self.orientation = random.randint(0,4)
            self.speed = 3
            self.step = 0
        if self.orientation == 0:
            self.rect.y = self.rect.y + self.speed
            self.changeImage(0 + frame )
        elif self.rect.x>=998:
            self.rect.x =995
            self.orientation=3
        elif self.rect.x<=24:
            self.rect.x = 27
            self.orientation=2
        elif self.rect.y<=24:
            self.rect.y=27
            self.orientation=0
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
    
        return a_arrow
    

class Octorok(Enemy):
    def __init__(self):
        Enemy.__init__(self,"Octorok.png", 4, 2)
        self.orientation = random.randint(0,3)
        self.step = 0
        self.health = 2
    def move(self, frame, link=None):
        self.link = link
        a_rock = None
        if self.step == 25:
            self.speed = 0
            if random.randint(0,3) == 3:
                a_rock = Rock()
                a_rock.rect.x = self.rect.x
                a_rock.rect.y = self.rect.y
                a_rock.orientation = self.orientation
                showSprite(a_rock)
            #backgroundMusic=makeSound("harderBetterFasterWhopper.mp3")


            
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
        
        
        return a_rock
class Leever(Enemy):
    def __init__(self):
        Enemy.__init__(self,"Leever.png", 6, 1)
        self.orientation = random.randint(0,3)
        self.step = 0
        self.changeImage(0)
        self.health = 3
        self.type = "C"
    def move(self, frame, link=None):
        self.link = link
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
        self.health = 3
        self.link = None
    

    def move(self, frame, link=None):
        self.link = link
        W_rock=None
        if frame % 2 == 0:
            self.step += 1
            if self.ShootReady:
                W_rock = self.Shoot(frame)
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
        
        return W_rock
    def Shoot(self, frame):
        if self.ShootReady == True:
            if self.link == None:
                pass
            else:
                W_Rock = TargetFireball(self.link)
                W_Rock.rect.x = self.rect.x
                W_Rock.rect.y = self.rect.y
                W_Rock.moveTo(self.rect.x, self.rect.y)
                showSprite(W_Rock)
            #print(W_Rock.rect.x, W_Rock.rect.y)
        
            return W_Rock
        
        return None
    
   

class Tektite(Enemy):
    def __init__(self):
        Enemy.__init__(self, "Tektite.png", 1, 2)
        self.time = 0
        self.speedx = 0
        self.speedy = 0
        self.jump = False
        self.health = 4
        
    def move(self, frame, link):
        self.link = link
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
        self.type = "B"

        self.health = 3
    def move(self, frame, link=None):
        self.link = link
        a_rock = None
        if self.step == 25:

            self.speed = 0

            if random.randint(0,1) == 1:
                a_rock = Rock()
                a_rock.rect.x = self.rect.x
                a_rock.rect.y = self.rect.y
                a_rock.orientation = self.orientation
                showSprite(a_rock)
       
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
        return a_rock
        
class WaterMonster(Enemy):
    def __init__(self, link):
        Enemy.__init__(self,"WaterMonster.png", 5, 1)
        self.orientation = 1
        self.frame = 0
        self.type = "D"
        self.health = 4
        self.link = link
        
    def move(self, frame, link):
        self.link = link
        a_target = None

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

        elif self.frame ==40:
            a_target= HotWater(link)
            a_target.moveTo(self.rect.x, self.rect.y)
            showSprite(a_target)
            self.frame += 1
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

        return(a_target)
            
        

class Projectile(newSprite):
    def __init__(self, filename, framesX=1, framesY=1):
        newSprite.__init__(self, filename, framesX, framesY)

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
    def moveTo(self, x,y):
        self.rect.x = x
        self.rect.y = y
        
class Rock( Projectile):
    def __init__(self):
         Projectile.__init__(self,"Rocks.png", 2, 1)

         
class Arrow(newSprite):
    def __init__(self, filename, framesX=1, framesY=1):
        newSprite.__init__(self, filename, framesX, framesY)
        self.speed = 3

        
    def move(self, frame):
        if self.orientation == 0:
            self.rect.y = self.rect.y + self.speed
            self.changeImage(0)
        elif self.orientation ==1:
            self.rect.y = self.rect.y - self.speed
            self.changeImage(1)
        elif self.orientation ==2:
            self.rect.x = self.rect.x + self.speed
            self.changeImage(2)
        else:
            self.rect.x = self.rect.x - self.speed
            self.changeImage(3)
            
class AArrow(Arrow):
    def __init__(self):
         Arrow.__init__(self,"arrow.png", 4, 1)
         
class TargetRock(Projectile):
    def __init__(self, link):
         Projectile.__init__(self,"Rocks.png", 2, 1)
         self.speed = 4
         self.quad = 0
         self.angle = 45
         self.link = link
    
    def move(self, frame):
        deltaX = self.speed * math.cos(self.angle)
        deltaY = self.speed * math.sin(self.angle)
        

        if self.quad == 1 or self.quad == 4:
            self.rect.x += deltaX
            self.rect.y += deltaY
        else:
            self.rect.x -= deltaX
            self.rect.y -= deltaY
            
        
    def moveTo(self, x,y):
        self.rect.x = x
        self.rect.y = y
        
        if (self.rect.x-self.link.rect.x) > 0:
            if (self.rect.y - self.link.rect.y)>0:
                #print("left and Above")
                self.quad = 2
            if (self.rect.y -self.link.rect.y)<0:
                #print("left and below")
                self.quad = 3
        else:
            if (self.rect.y - self.link.rect.y)>0:
                #print("right and Above")
                self.quad = 1
            if (self.rect.y -self.link.rect.y)<0:
                #print("right and below")
                self.quad = 4
            
        self.angle = math.atan((self.rect.y -self.link.rect.y)/(self.rect.x-self.link.rect.x))
        
        
class TargetFireball(Projectile):
    def __init__(self, link):
         Projectile.__init__(self,"fireball1.png", 3, 1)
         self.speed = 4
         self.quad = 0
         self.angle = 45
         self.link = link
    
    def move(self, frame):
        deltaX = self.speed * math.cos(self.angle)
        deltaY = self.speed * math.sin(self.angle)
        
        if self.quad == 1 or self.quad == 4:
            self.rect.x += deltaX
            self.rect.y += deltaY
        else:
            self.rect.x -= deltaX
            self.rect.y -= deltaY
            
        
    def moveTo(self, x,y):
        self.rect.x = x
        self.rect.y = y
        
        if (self.rect.x-self.link.rect.x) > 0:
            if (self.rect.y - self.link.rect.y)>0:
                #print("left and Above")
                self.quad = 2
            if (self.rect.y -self.link.rect.y)<0:
                #print("left and below")
                self.quad = 3
        else:
            if (self.rect.y - self.link.rect.y)>0:
                #print("right and Above")
                self.quad = 1
            if (self.rect.y -self.link.rect.y)<0:
                #("right and below")
                self.quad = 4
        if (self.rect.x-self.link.rect.x) != 0:    
            self.angle = math.atan((self.rect.y -self.link.rect.y)/(self.rect.x-self.link.rect.x))
        
class Rock( Projectile):
    def __init__(self):

        Projectile.__init__(self,"Rocks.png", 2, 1)
    
class HotWater(Projectile):
    def __init__(self, link):
        Projectile.__init__(self,"HotWater.png", 3, 1)
        self.speed = 2
        self.quad = 0
        self.angle = 0
        self.link = link
    def move(self, frame):
        deltaX = self.speed * math.cos(self.angle)
        deltaY = self.speed * math.sin(self.angle)
        
        if self.quad == 1 or self.quad == 4:
            self.rect.x += deltaX
            self.rect.y += deltaY
        else:
            self.rect.x -= deltaX
            self.rect.y -= deltaY
        
    def moveTo(self, x,y):
        self.rect.x = x
        self.rect.y = y
        
        if (self.rect.x-self.link.rect.x) > 0:
            if (self.rect.y - self.link.rect.y)>0:
                #print("left and Above")
                self.quad = 2
            if (self.rect.y -self.link.rect.y)<0:
                #print("left and below")
                self.quad = 3
        else:
            if (self.rect.y - self.link.rect.y)>0:
                #print("right and Above")
                self.quad = 1
            if (self.rect.y -self.link.rect.y)<0:
                #print("right and below")
                self.quad = 4
            
        self.angle = math.atan((self.rect.y -self.link.rect.y)/(self.rect.x-self.link.rect.x))
         
class TargetRock(Projectile):
    def __init__(self, link):
         Projectile.__init__(self,"Rocks.png", 2, 1)
         self.speed = 4
         self.quad = 0
         self.angle = 45
         self.link = link
    
    def move(self, frame):
        deltaX = self.speed * math.cos(self.angle)
        deltaY = self.speed * math.sin(self.angle)
        
        if self.quad == 1 or self.quad == 4:
            self.rect.x += deltaX
            self.rect.y += deltaY
        else:
            self.rect.x -= deltaX
            self.rect.y -= deltaY
        
    def moveTo(self, x,y):
        self.rect.x = x
        self.rect.y = y
        
        if (self.rect.x-self.link.rect.x) > 0:
            if (self.rect.y - self.link.rect.y)>0:
                #print("left and Above")
                self.quad = 2
            if (self.rect.y -self.link.rect.y)<0:
                #print("left and below")
                self.quad = 3
        else:
            if (self.rect.y - self.link.rect.y)>0:
                #print("right and Above")
                self.quad = 1
            if (self.rect.y -self.link.rect.y)<0:
                #print("right and below")
                self.quad = 4
            
        self.angle = math.atan((self.rect.y -self.link.rect.y)/(self.rect.x-self.link.rect.x))

        
class Item(newSprite):
    def __init__(self, img, x, link):
        newSprite.__init__(self, img, x)
        self.value = 0
        self.health = 0
        self.bomb = 0
        self.time = 0
        self.maxHealth = 0
        self.link = link
          
    def animate(self):
        nextSpriteImage(self)
        
    def collision(self):
        if touching(self, self.link):
            killSprite(self)
            return True
        else:
            return False
    def animate(self, frame = 0):
        nextSpriteImage(self)
          
class BombItem(Item):
    def __init__(self,link):
        self.link = link
        Item.__init__(self, "Bomb.png", 1, self.link)           
        self.value = 1
    def animate (self, frame=0):
        pass

class PlacableBomb(newSprite):
    def __init__(self, x, y):
        newSprite.__init__(self, "Bomb.png", 1)
        self.rect.x = x
        self.rect.y = y
        self.step = 0
    def animate (self, step=0):
        self.frames += 1
        if self.step == 10:
            hideSprite(self)
            self.step = 0
    
class Rupee(Item):
    def __init__(self,link):
        self.link = link
        Item.__init__(self, "Coins.png", 2, self.link)
        self.value = 1
    def animate (self, frame=0):
        pass
  
class BlueRupee(Item):
    def __init__(self,link):
        self.link = link
        Item.__init__(self, "Coins.png", 2, self.link)
        self.value = 5
        self.changeImage(1)
    def hit(self):
        killSprite(self)
    def animate(self, frame=0):
        pass 

class Heart(Item):
    def __init__(self, link):
        self.link = link
        Item.__init__(self,"Hearts.png", 3, self.link)
        self.health = 1
        
    def animate(self, frame=0):
        self.changeImage(frame)
    
    
class Fairy(Item):
    def __init__(self, x, y, link):
        self.link = link
        Item.__init__(self, "Fairy.png", 2, self.link)
        self.radian = 0
        self.radius = 250
        self.x = x
        self.y = y
        self.xPos = x
        self.yPos = y
        self.speed = .1
        self.rotations = 3
        
        
    def Move(self):
         
        if self.rotations*(math.pi*2) <= self.radian:
            self.xPos -= 20
            self.yPos -= 10
             
        else:
            self.yPos = (math.sin(self.radian)*self.radius) + self.y
            self.xPos = (math.cos(self.radian)*self.radius) + self.x
            self.radian += self.speed
            self.speed += .001
            self.radius -= 1
        
        self.move(self.xPos, self.yPos)
        
class Clock(Item):
    def __init__(self, link):
        Item.__init__(self, "Clock.png", 1, link)
            
    def animate(self,frame=0):
        pass         
class Tile(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.images = []
        self.images.append(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 9
        self.scale = 1
        self.x = self.rect.x
        self.y = self.rect.y
        self.passThrough = False

    def addImage(self, aImage):
        self.images.append(aImage)

    def changeImage(self, index=0):
        self.image = self.images[index]

    def move(self, xpos, ypos, centre=False):
        if centre:
            self.rect.center = [xpos, ypos]
        else:
            self.rect.topleft = [xpos, ypos]


# Note that Wall inherits from pygame sprite not newSprite
class Wall(Tile):
    """
    Walls are Scene Objects that most sprites cannot pass through
    """

    def __init__(self, image):
        Tile.__init__(self, image)
        self.passThrough = False
        self.choppable = False

    def move(self, xpos, ypos, centre=False):
        if centre:
            self.rect.center = [xpos, ypos]
        else:
            self.rect.topleft = [xpos, ypos]


class Scene:
    """
    A Scene is a background that does interact with the sprites.  For instance
    there are walls that the sprites cannot pass through
    """
    passTiles = ["C", "W", "b", "c", "d", "h", "i", "j", "n", "o", "p", "d", "q", "r", "s", "t", "k", "v"]

    def __init__(self, screen, player, spriteSheetFileName, mapFileName, framesX=1, framesY=1):
        global background

        self.player = player
        print("Loading: "+str(spriteSheetFileName))
        spriteSheet = loadImage(spriteSheetFileName)
        self.originalWidth = spriteSheet.get_width() // framesX
        self.originalHeight = spriteSheet.get_height() // framesY
        frameSurf = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)
        x = 0
        y = 0
        self.images = []
        for column in range(framesY):
            for frameNo in range(framesX):
                frameSurf = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)
                frameSurf.blit(spriteSheet, (x, y))
                self.images.append(frameSurf.copy())
                x -= self.originalWidth
            y -= self.originalHeight
            x = 0
        # Other initialized parameters
        self.Wall_Tiles = []
        self.Ground_Tiles = []
        self.Water_Tiles = []
        self.Enemies = []
        self.Projectiles = []
        self.Items = []
        # Populate the lists
        game_folder = os.getcwd()
        map_data = []
        with open(path.join(game_folder, mapFileName), 'rt') as f:
            for line in f:
                map_data.append(line)

        i = 0
        for row, tiles in enumerate(map_data):
            for col, tile in enumerate(tiles):
                if tile in base64dict:
                    if tile in Scene.passTiles:
                        passTile = Tile(self.images[base64dict[tile]])
                        passTile.move(col * 32, row * 32)
                        self.Ground_Tiles.append(passTile)
                    else:
                        thisWall = Wall(self.images[base64dict[tile]])
                        thisWall.move(col * 32, row * 32)
                        if tile == 'Y' or tile == 'Z' or tile == 'a' or tile == 'e' or tile == 'f' or tile == 'g' or tile == 'k' or tile == 'l' or tile == 'm':
                            self.Water_Tiles.append(thisWall)
                        else:
                            self.Wall_Tiles.append(thisWall)
                            if tile == 'H':
                                thisWall.choppable = True
                                thisWall.addImage(self.images[base64dict['i']])
                            
                elif tile == "@":
                    enemy = Octorok()
                    enemy.rect.x = col * 32
                    enemy.rect.y = row * 32
                    self.Enemies.append(enemy)
                elif tile == "^":
                    enemy = Leever()
                    enemy.rect.x = col * 32
                    enemy.rect.y = row * 32
                    self.Enemies.append(enemy)
                elif tile == "#":
                    enemy = BlueOctorok()
                    enemy.rect.x = col * 32
                    enemy.rect.y = row * 32
                    self.Enemies.append(enemy)
                elif tile == "$":
                    enemy = Moblin()
                    enemy.rect.x = col * 32
                    enemy.rect.y = row * 32
                    self.Enemies.append(enemy)
                elif tile == "&":
                    enemy = DarkMoblin()
                    enemy.rect.x = col * 32
                    enemy.rect.y = row * 32
                    self.Enemies.append(enemy)
                elif tile == "*":
                    enemy = WaterMonster()
                    enemy.rect.x = col * 32
                    enemy.rect.y = row * 32
                    self.Enemies.append(enemy)
                elif tile == "!":
                    enemy = wizzrobe()
                    enemy.rect.x = col * 32
                    enemy.rect.y = row * 32
                    self.Enemies.append(enemy)
                elif tile == "~":
                    enemy = Tektite()
                    enemy.rect.x = col * 32
                    enemy.rect.y = row * 32
                    self.Enemies.append(enemy)
                if tile not in base64dict:
                    thisGround = Tile(self.images[2])
                    thisGround.move(col * 32, row * 32)
                    self.Ground_Tiles.append(thisGround)
        self.surface = screen.copy()
        background = self.surface
        # Methods for Scrolling the Scene

    def scroll(self, x, y):
        for enemy in self.Enemies:
            enemy.speed = 0
            hideSprite(enemy)
        for projectile in self.Projectiles:
            killSprite(projectile)
        self.Projectiles = []
        for item in self.Items:
            killSprite(item)
        self.Items = []
        for tile in self.all_wall_panels:
            tile.move(tile.rect.x + x, tile.rect.y + y)
        for tile in self.all_ground_tiles:
            tile.move(tile.rect.x + x, tile.rect.y + y)
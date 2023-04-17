from pygame_functions import *
import random
import math

class Player(newSprite):
    def __init__(self):
        newSprite.__init__(self, "LinkSimple.png", 14)
        self.rect.x = 500
        self.rect.y = 350

        self.speed = 4
        self.health=3
        print("Link created")
    def hit(self,enemies, ded,llorientation):
        #print (llorientation)
        if self.health <= 0:
            if ded == False:
                dieAvailable=False
                theReaper=True
                if theReaper==True:
                    dieAvailable=True
                    if dieAvailable==True:
                        dieAvailable=False
                        theReaper=False
                        dieOn=True
                        ded=True
                        if llorientation ==0:
                            self.rect.y -=32
                            self.health= self.health - 0.5
                        elif llorientation ==1:
                            self.rect.y +=32
                            self.health= self.health - 0.5
                        elif llorientation ==2:
                            self.rect.x -=32
                            self.health= self.health - 0.5
                        elif llorientation ==3:
                            self.rect.x +=32
                            self.health= self.health - 0.5
                        hideSprite(enemies)
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
        elif llorientation ==0:
            self.rect.y -=32
            self.health= self.health - 0.5
        elif llorientation ==1:
            self.rect.y +=32
            self.health= self.health - 0.5
        elif llorientation ==2:
            self.rect.x -=32
            self.health= self.health - 0.5
        elif llorientation ==3:
            self.rect.x +=32
            self.health= self.health - 0.5

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
    """
    def hit(self):
        self.health -=1
        self.rect.y +=32
        if self.health == 0:
            killSprite(self)
    """       
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
    

    def hit(self, lorientation):
        self.health -=1
        if self.health == 0:
            killSprite(self)
        elif lorientation ==0:
            self.rect.y +=32
        elif lorientation ==1:
            self.rect.x +=32
        elif lorientation ==2:
            self.rect.y -=32
        elif lorientation ==3:
            self.rect.x -=32

        self.health -=1



class DarkMoblin(Enemy):
    def __init__(self):
        Enemy.__init__(self,"DarkMoblin.png", 8, 1)
        self.orientation = random.randint(0,3)
        self.step = 0
        self.health = 3
    def move(self, frame):
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
            self.rect.x = self.rect.x - self.speed
            self.changeImage(4+frame)
        elif self.rect.x<=24:
            self.rect.x = 27
            self.rect.x = self.rect.x - self.speed
            self.changeImage(4+frame)
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
    def move(self, frame):
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
            self.rect.x = self.rect.x - self.speed
            self.changeImage(4+frame)
        elif self.rect.x<=24:
            self.rect.x = 27
            self.rect.x = self.rect.x + self.speed
            self.changeImage(4+frame)
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
    def move(self, frame):
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
    def move(self, frame):
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
        
    
    def move(self, frame):
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
            #print("I'm going to shoot now")
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
        self.health = 4
        
    def move(self, frame):
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
        self.health = 3
    def move(self, frame):
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
        self.health = 4
        self.link = link
        
    def move(self, frame):
        T_Rock = None
        

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
        elif self.frame == 40:
            T_Rock = TargetRock(self.link)
            T_Rock.moveTo(self.rect.x, self.rect.y)
            showSprite(T_Rock)
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
        #if self.frame == 3:
            #self.Originalimg = pygame.image.load("ROCKh.png")

        return T_Rock
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
        
class Item(newSprite):
    def __init__(self, img, x):
        newSprite.__init__(self, img, x)
        self.value = 0
        self.health = 0
        self.bomb = 0
        self.time = 0
        self.maxHealth = 0
        
    def animate(self):
        nextSpriteImage(self)

class Rupee(Item):
    def __init__(self):
        Item.__init__(self, "Coins.png", 2)
        self.value = 1
        
    def animate(self, frame=0):
        pass

class BlueRupee(Item):
    def __init__(self):
        Item.__init__(self, "Coins.png", 2)
        self.value = 5
        self.changeImage(1)
        
    def animate(self, frame=0):
        pass

class Heart(Item):
    def __init__(self):
        Item.__init__(self,"Hearts.png", 3)
        self.health = 1
        
    def animate(self, frame=0):
        self.changeImage(frame)

    
class Rock( Projectile):
    def __init__(self):
         Projectile.__init__(self,"Rocks.png", 2, 1)
         
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
    def __init__(self, img, x):
        newSprite.__init__(self, img, x)
        self.value = 0
        self.health = 0
        self.bomb = 0
        self.time = 0
        self.maxHealth = 0
          
    def animate(self):
        nextSpriteImage(self)
          
           
    
class Rupee(Item):
    def __init__(self):
        Item.__init__(self, "coins.png", 2)
        self.value = 1
    def animate (self, frame=0):
        pass
  
  
class BlueRupee(Item):
    def __init__(self):
        Item.__init__(self, "coins.png", 2)
        self.value = 5
        self.changeImage(1)
    def animate(self, frame=0):
        pass
        
            
class HeartContainer(Item):
    def __init__(self):
        item.__init__(self, "Hearts.png", 3)
        self.maxHealth = 1
        self.changeImage(2)
            
    def animate(self):
        pass
    




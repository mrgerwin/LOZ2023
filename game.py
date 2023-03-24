from pygame_functions import *
from sprites import Player, Octorok, WaterMonster, Projectile, BlueOctorok, Tektite, Sword, wizzrobe, Leever, Rock, TargetRock

screenSize(1024,768)
setBackgroundColour('grey')

setAutoUpdate(False)

#Making all sprites
link = Player()
Blueoctorok = BlueOctorok()
octorok = Octorok()
octorok.moveTo(500,500)
leever=Leever()
leeverspawned=True
showSprite(leever)
wizzrobe = wizzrobe()
watermonster = WaterMonster()
tektite = Tektite()
sword = Sword("Sworb.png", 4, 1)

enemies = [octorok, Blueoctorok, watermonster, tektite, wizzrobe, leever]
projectiles = []
showSprite(link)
for enemy in enemies:
    showSprite(enemy)

#Experimenting with Rocks
a_rock = TargetRock(link)
a_rock.orientation = 0
showSprite(a_rock)
a_rock.rect.x = 500
a_rock.rect.y = 350

nextFrame = clock()
frame = 0

dieOn=False
def Die():
    global dieOn
    dieOn=True
    changeSpriteImage(link, 0)
    pause(125)
    changeSpriteImage(link, 5)
    pause(125)
    changeSpriteImage(link, 2)
    pause(125)
    changeSpriteImage(link, 6)
    pause(125)
    changeSpriteImage(link, 0)
    pause(125)
    changeSpriteImage(link, 5)
    pause(125)
    changeSpriteImage(link, 2)
    pause(125)
    changeSpriteImage(link, 6)
    pause(125)
    changeSpriteImage(link, 0)
    pause(125)
    changeSpriteImage(link, 5)
    pause(125)
    changeSpriteImage(link, 2)
    pause(125)
    changeSpriteImage(link, 6)
    pause(125)
    changeSpriteImage(link, 0)
    pause(125)
    changeSpriteImage(link, 5)
    pause(125)
    changeSpriteImage(link, 2)
    pause(125)
    changeSpriteImage(link, 6)
    pause(125)
    changeSpriteImage(link, 0)
    

while True:
    if clock() >nextFrame:
        frame= (frame + 1)%2
        nextFrame += 80
        pause(10)
        
        if dieOn == False:
          if keyPressed("down"):
              link.orientation =0
              link.move(frame)
              hideSprite(sword)

          if keyPressed("up"):
              link.orientation =1
              link.move(frame)
              hideSprite(sword)

          if keyPressed("right"):
              link.orientation =2
              link.move(frame)
              hideSprite(sword)

          if keyPressed("left"):
              link.orientation =3
              link.move(frame)
              hideSprite(sword)

          if keyPressed("space"):
              changeSpriteImage(link, link.orientation + 8)
              sword.stab(link.rect.x, link.rect.y, link.orientation)
              showSprite(sword)

          if keyPressed("h"):
              changeSpriteImage(link, frame+12)
          if keyPressed("s"):
              link.move(frame)
          if keyPressed("d"):
              Die()
        """
          if keyPressed("l"):
              leever.spawn(leever,frame)
              leeverspawned=True
          if leeverspawned==True:
              leever.move(frame)
        """
        for enemy in enemies:
            projectile = enemy.move(frame, link)
          #wizzrobe.Spellballmove(link.rect.x, link.rect.y)
            if projectile != None:
                projectiles.append(projectile)
                showSprite(projectile)
            if touching(enemy, sword):
                hideSprite(enemy)

        for projectile in projectiles:
            projectile.move(frame)
        
        
        sword.facing()


        a_rock.move(frame)



        updateDisplay()

endWait()
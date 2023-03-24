from pygame_functions import *

from sprites import Player, Octorok, WaterMonster, Projectile, BlueOctorok, Tektite, Sword, wizzrobe, Leever

# You Can Do It Code!!! I Believe In You!!!
screenSize(1024,768)
setBackgroundColour('grey')
#timer = clock
setAutoUpdate(False)
link = Player()
Blueoctorok = BlueOctorok()
octorok = Octorok()
leever = Leever()
watermonster = WaterMonster()
leeverspawned=True
wizzrobe = wizzrobe()
showSprite(link)

tektite = Tektite()
sword = Sword("Sworb.png", 4, 1)

a_rock = Projectile()
a_rock.orientation = 0
showSprite(a_rock)
a_rock.rect.x = 500
a_rock.rect.y = 350

enemies = [octorok, Blueoctorok, watermonster, tektite, wizzrobe, leever]

for enemy in enemies:
    showSprite(enemy)

nextFrame = clock()
frame = 0
backgroundMusic=makeSound("betterCallSaulTheme.mp3")
playSound(backgroundMusic,10)
dieOn=False
def Die():
    global dieOn
    dieOn=True
    stopSound(backgroundMusic)
    link.die(frame)


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
            
        """
          if keyPressed("l"):
              leever.spawn(leever,frame)
              leeverspawned=True
          if leeverspawned==True:
              leever.move(frame)
        """
        for enemy in enemies:
            enemy.move(frame)
            if touching(enemy, link):
                link.hit()
            if touching(enemy, sword):
                enemy.hit()
                if enemy.health == 0:
                    enemies.remove(enemy)
                    killSprite(enemy)
                    
        if link.health == 0:
            Die()

        sword.facing()


        a_rock.move(frame)



        updateDisplay()

endWait()
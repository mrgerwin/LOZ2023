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
leever=Leever()
leeverspawned=True
showSprite(leever)
wizzrobe = wizzrobe()
showSprite(link)
showSprite(octorok)
showSprite(wizzrobe)

canMove = True
canStab = True
timer = 0

tektite = Tektite()
sword = Sword("Sworb.png", 4, 1)
showSprite(tektite)


watermonster = WaterMonster()
showSprite(link)
showSprite(octorok)
showSprite(Blueoctorok)
showSprite(watermonster)
'''
a_rock = Projectile()
a_rock.orientation = 0
showSprite(a_rock)
a_rock.rect.x = 500
a_rock.rect.y = 350
'''

enemies = [octorok, Blueoctorok, watermonster, tektite, wizzrobe, leever]

nextFrame = clock()
frame = 0
#backgroundMusic=makeSound("harderBetterFasterWhopper.mp3")
backgroundMusic=makeSound("betterCallSaulTheme.mp3")
playSound(backgroundMusic,10)
dieOn=False
def Die():
    global dieOn
    dieOn=True
    stopSound(backgroundMusic)
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
                if canMove == True:
                    link.move(frame)
                    hideSprite(sword)

            if keyPressed("up"):
                link.orientation =1
                if canMove == True:
                    link.move(frame)
                    hideSprite(sword)

            if keyPressed("right"):
                link.orientation =2
                if canMove == True:
                    link.move(frame)
                    hideSprite(sword)

            if keyPressed("left"):
                link.orientation =3
                if canMove == True:
                    link.move(frame)
                    hideSprite(sword)

            if keyPressed("space") and canStab:
                canMove = False
                canStab = False 
                timer = nextFrame
                changeSpriteImage(link, link.orientation + 8)
                sword.stab(link.orientation, link.rect.x, link.rect.y, frame)
                showSprite(sword)
                
            if timer+400 <= nextFrame and canStab == False:
                canMove = True
                hideSprite(sword)
                changeSpriteImage(link, link.orientation * 2)
                canStab = True

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
            enemy.move(frame)
          #wizzrobe.Spellballmove(link.rect.x, link.rect.y)
            if touching(enemy, sword):
<<<<<<< Updated upstream
                hideSprite(enemy)
=======
                pass
                #killSprite(enemy)
                #enemy.hit()
                
            if touching (enemy, link):
                pass
                #killSprite(link)
                #link.hit()
            for projectile in projectiles:
                projectile.move(frame)

>>>>>>> Stashed changes

        sword.facing()
        

        '''
        a_rock.move(frame)
        '''


        updateDisplay()

endWait()
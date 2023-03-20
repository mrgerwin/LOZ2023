from pygame_functions import *

from sprites import Player, Octorok, WaterMonster, Projectile, BlueOctorok, Tektite, Sword, wizzrobe


screenSize(1024,768)
setBackgroundColour('grey')
#timer = clock
setAutoUpdate(False)
link = Player()
Blueoctorok = BlueOctorok()
octorok = Octorok()

wizzrobe = wizzrobe()
showSprite(link)
showSprite(octorok)
showSprite(wizzrobe)



tektite = Tektite()
sword = Sword("Sworb.png", 4, 1)
showSprite(tektite)


watermonster = WaterMonster()
showSprite(link)
showSprite(octorok)
showSprite(Blueoctorok)
showSprite(watermonster)
a_rock = Projectile()
a_rock.orientation = 0
showSprite(a_rock)
a_rock.rect.x = 500
a_rock.rect.y = 350


nextFrame = clock()
frame = 0

while True:
    if clock() >nextFrame:
        frame= (frame + 1)%2
        nextFrame += 80
        pause(10)
        
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

        wizzrobe.move(frame)
        #wizzrobe.Spellballmove(link.rect.x, link.rect.y)

            
        if touching(octorok, sword):
            hideSprite(octorok)
        

        octorok.move(frame)

        tektite.move(frame)
        sword.facing()


        Blueoctorok.move(frame)

        watermonster.move(frame)

        a_rock.move(frame)



        updateDisplay()

endWait()
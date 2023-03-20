from pygame_functions import *
from sprites import Player, Octorok, WaterMonster, Projectile


screenSize(1024,768)
setBackgroundColour('grey')
#timer = clock
setAutoUpdate(False)
link = Player()
octorok = Octorok()
watermonster = WaterMonster()
showSprite(link)
showSprite(octorok)
showSprite(watermonster)
a_rock = Projectile()
a_rock.orientation = 0
showSprite(a_rock)
a_rock.rect.x = 500
a_rock.rect.y = 350

#moveSprite(octorok, 200, 200)

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
        if keyPressed("up"):
            link.orientation =1
            link.move(frame)
        if keyPressed("right"):
            link.orientation =2
            link.move(frame)
        if keyPressed("left"):
            link.orientation =3
            link.move(frame)
        if keyPressed("space"):
            changeSpriteImage(link, link.orientation + 8)
        if keyPressed("h"):
            changeSpriteImage(link, frame+12)
        octorok.move(frame)
        watermonster.move(frame)

        a_rock.move(frame)

        updateDisplay()

endWait()
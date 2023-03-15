from pygame_functions import *
from sprites import Player, Octorok, wizzrobe


screenSize(1024,768)
setBackgroundColour('grey')
setAutoUpdate(False)
link = Player()
octorok = Octorok()
wizzrobe = wizzrobe()
showSprite(link)
showSprite(octorok)
showSprite(wizzrobe)



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
        wizzrobe.move(frame)
        octorok.move(frame)
        updateDisplay()

endWait()
from pygame_functions import *
from sprites import Player, Octorok, Leever

# You Can Do It Code!!! I Believe In You!!!
screenSize(1024,768)
setBackgroundColour('grey')
setAutoUpdate(False)
link = Player()
octorok = Octorok()
leever=Leever()
showSprite(link)
showSprite(octorok)
showSprite(leever)
#moveSprite(octorok, 200, 200)

nextFrame = clock()
frame = 0
backgroundMusic=makeSound("harderBetterFasterWhopper.mp3")
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
            if keyPressed("s"):
                link.move(frame)
            elif keyPressed("space"):
                changeSpriteImage(link, link.orientation + 8)
            elif keyPressed("d"):
                Die()
            elif keyPressed("h"):
                changeSpriteImage(link, frame+12)
            octorok.move(frame)
            leever.move(frame)
            updateDisplay()
        else:
            pass

endWait()
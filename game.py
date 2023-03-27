from pygame_functions import *
from sprites import Player, Octorok, WaterMonster, Projectile, BlueOctorok, Tektite, Sword, wizzrobe, Leever, Rock

screenSize(1024,768)
setBackgroundColour('grey')

setAutoUpdate(False)

#Making all sprites
link = Player()
Blueoctorok = BlueOctorok()
octorok = Octorok()
leever=Leever()
leeverspawned=True
showSprite(leever)
wizzrobe = wizzrobe()
watermonster = WaterMonster()
tektite = Tektite()
sword = Sword("Sworb.png", 4, 1)

enemies = [octorok, Blueoctorok, watermonster, tektite, wizzrobe, leever]
showSprite(link)
for enemy in enemies:
    showSprite(enemy)

#Experimenting with Rocks
"""
a_rock = Rock()
a_rock.orientation = 0
showSprite(a_rock)
a_rock.rect.x = 500
a_rock.rect.y = 350
"""
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
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit = True
                pygame.quit()
                sys.exit(0)
        

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    changeSpriteImage(link, link.orientation + 8)
                    sword.stab(link.rect.x, link.rect.y, link.orientation)
                    showSprite(sword)
                if event.key == pygame.K_LEFT:
                    link.orientation =3
                    hideSprite(sword)
                    link.speed = 4
                if event.key == pygame.K_RIGHT:
                    link.orientation =2
                    link.speed = 4
                    hideSprite(sword)
                if event.key == pygame.K_UP:
                    link.orientation =1
                    link.speed = 4
                    hideSprite(sword)
                if event.key == pygame.K_DOWN:
                    link.orientation =0
                    link.speed = 4
                    hideSprite(sword)
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    print("Aiden do the sword thing")
                if event.key == pygame.K_LEFT:
                    link.speed = 0
                if event.key == pygame.K_RIGHT:
                    link.speed = 0
                if event.key == pygame.K_UP:
                    link.speed = 0
                if event.key == pygame.K_DOWN:
                    link.speed = 0
        
              
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
                hideSprite(enemy)


        link.move(frame)
        sword.facing()


        #a_rock.move(frame)



        updateDisplay()

endWait()
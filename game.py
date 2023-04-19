from pygame_functions import *

from sprites import Player, Octorok, WaterMonster, Projectile, BlueOctorok, Tektite, Sword, wizzrobe, Leever, TargetRock, DarkMoblin, Moblin, Heart, Rupee, BlueRupee, BombItem,Clock

screenSize(1024,768)
setBackgroundColour('grey')

setAutoUpdate(False)

#Making all sprites
link = Player()
ClockAquired=False
ClockNumber=0
Blueoctorok = BlueOctorok()
octorok = Octorok()
leever=Leever()
leeverspawned=True
showSprite(leever)
wizzrobe = wizzrobe(link)
tektite = Tektite()
moblin = Moblin()
dmoblin = DarkMoblin()
sword = Sword("Sworb.png", 4, 1)




Bomb = BombItem()

#a_rock.orientation = 0

items = [Bomb]

heart1 = Heart()
clock1= Clock()
rupee1 = Rupee()
bluerupee1 = BlueRupee()
heart1.move(64,64)
rupee1.move(128, 64)
bluerupee1.move(96,64)
clock1.move(160,64)
showSprite(heart1)
showSprite(rupee1)
showSprite(clock1)
showSprite(bluerupee1)

watermonster = WaterMonster(link)
projectiles = []

nextFrame = clock()
frame = 0
backgroundMusic=makeSound("linkMusic.mp3")
playSound(backgroundMusic,10)

enemies = [octorok, Blueoctorok, watermonster, tektite, wizzrobe, leever, moblin, dmoblin]
showSprite(link)

for enemy in enemies:
    showSprite(enemy)
dieOn=False
ded=False

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
        
            if dieOn == False:
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
                  if event.key == pygame.K_a:
                      ClockAquired=True
                      print("A key pressed")


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
       
        for enemy in enemies:
            if ClockAquired==False:
                projectile = enemy.move(frame)
                if projectile != None:
                    projectiles.append(projectile)
            else:
                if ClockNumber==500:
                    ClockAquired=False
                    ClockNumber=0
                else:
                    ClockNumber+=1
                    print(ClockNumber)

            if touching(enemy, sword):
                #killSprite(enemy)
                if enemy.health ==1:
                    enemies.remove(enemy)
                enemy.hit(link.orientation)
                
            if touching (enemy, link):
                #killSprite(link)
                if link.health == 0.5:
                    print("you died")
                link.hit(enemy,ded,link.orientation)
            for projectile in projectiles:
                projectile.move(frame)

        

        sword.facing()
        link.move(frame)

        #a_rock.move(frame)

        heart1.animate(frame)
        updateDisplay()

endWait()
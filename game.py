from pygame_functions import *

from sprites import Player, Octorok, WaterMonster, Projectile, BlueOctorok, Tektite, Sword, wizzrobe, Leever, TargetRock, DarkMoblin, Moblin, Heart, Rupee, BlueRupee, BombItem, PlacableBomb, HotWater,Clock, Fairy

screenX = 1024
screenY = 768

screenSize(screenX,screenY)
setBackgroundColour('grey')

setAutoUpdate(False)

#Making all sprites
link = Player()
ClockAquired=False
ClockNumber=0
music = makeMusic("linkMusic.mp3")
link_die = makeSound("LOZ_Link_DIE.wav")
link_hit = makeSound("LOZ_Link_Hurt.wav")
enemy_die = makeSound("LOZ_Enemy_DIE.wav")
enemy_hit = makeSound("LOZ_Enemy_Hit.wav")
sword_slash = makeSound("LOZ_Sword_Slash.wav")

Blueoctorok = BlueOctorok()
octorok = Octorok()
leever=Leever()
wizzrobe = wizzrobe(link)
watermonster = WaterMonster(link)
tektite = Tektite()
moblin = Moblin()
dmoblin = DarkMoblin()
fairy = Fairy(screenX//2, screenY//2, link)
leeverspawned=True
sword = Sword("Sworb.png", 4, 1)
showSprite(link)
heart1 = Heart(link)
Bomb = PlacableBomb(link, BombItem)
Bomb1 = BombItem(link)
Bomb2 = BombItem(link)
Bomb3 = BombItem(link)
rupee1 = Rupee(link)
bluerupee1 = BlueRupee(link)
bluerupee2 = BlueRupee(link)
bluerupee3 = BlueRupee(link)
clock1=Clock(link)
heart1.move(64,64)
rupee1.move(128, 64)
clock1.move(160,64)
Bomb1.rect.x = 600
Bomb1.rect.y = 64
Bomb2.rect.x = 650
Bomb2.rect.y = 64
Bomb3.rect.x = 700
Bomb3.rect.y = 64
bluerupee1.move(96,64)

fairy.move(200, 200)
bluerupee2.move(64, 96)
bluerupee3.move(46, 69)
Bomb = Bomb1, Bomb2, Bomb3

projectiles = []

nextFrame = clock()
frame = 0
green = (0,102,0)
backgroundMusic=makeSound("linkMusic.mp3")
playSound(backgroundMusic,10)

bombs = newLabel(str(link.Bomb), 20, 'Arial', 'green', 200, 60,"clear")
textboxGroup.add(bombs)
enemies = [octorok, Blueoctorok, watermonster, tektite, wizzrobe, leever, moblin, dmoblin]
Items = [heart1, rupee1, bluerupee1, bluerupee2, bluerupee3, Bomb1, Bomb2, Bomb3, clock1, fairy] 
showSprite(link)

HealthText = newLabel(str(link.health), 20, 'Arial', 'green', 200, 60,"clear")
MoneyText = newLabel(str(link.money), 20, 'Arial', 'green', 300, 60, "clear")

showLabel(HealthText)
showLabel(MoneyText)

for enemy in enemies:
    showSprite(enemy)
    
for item in Items:
    showSprite(item)

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
    killSprite(link)
    
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
                      
                  if event.key == pygame.K_b:
                      #Placebomb 
                      pass

              if event.type == pygame.KEYUP:
                  if event.key == pygame.K_SPACE:
                      hideSprite(sword)
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
                projectile = enemy.move(frame,link)
                if projectile != None:
                    projectiles.append(projectile)
            else:
                if ClockNumber==500:
                    ClockAquired=False
                    ClockNumber=0
                else:
                    ClockNumber+=1
                    #print(ClockNumber)


            if touching(enemy, sword):
                #killSprite(enemy)
                if enemy.health ==1:
                    enemies.remove(enemy)
                enemy.hit(link.orientation)
                
            if touching (enemy, link):
                #killSprite(link)
                link.hit(enemy,ded)
                changeLabel(HealthText,str(link.health), green)
        for projectile in projectiles:
            projectile.move(frame)
            if touching(link, projectile):
                link.hit(projectile, ded)
                
        for Item in Items:
            Item.animate(frame)
            if touching (link, Item):
                if type(Item) == BlueRupee:
                    link.money +=5
                    changeLabel(MoneyText,str(link.money), green)
                    
                
                
                elif type(Item) == BombItem:
                    link.Bomb +=1
                    link.hit(enemy, ded)
                    changeLabel(bombs,str(link.Bomb), 'green')
                    print(link.Bomb)

                elif type(Item)==Clock:
                    ClockAquired=True

                Items.remove(Item)
                killSprite(Item)
                print(link.money)
        if link.health == 0:
            print("you died")
            ded = True
            Die()
        fairy.Move()
        sword.facing()
        link.move(frame)
        updateDisplay()

endWait()
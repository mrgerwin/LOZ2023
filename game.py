from pygame_functions import *
from sprites import *

#from sprites import Player, Octorok, WaterMonster, Projectile, BlueOctorok, Tektite, Sword, wizzrobe, Leever, TargetRock, DarkMoblin, Moblin, Heart, Rupee, BlueRupee, BombItem, PlacableBomb, HotWater,Clock, Fairy

screenX = 1024
screenY = 768


window = screenSize(screenX,screenY)
setBackgroundColour('grey')

setAutoUpdate(False)

#Making all sprites
link = Player()
scene1 = Scene(window, link, "ZeldaMapTilesBrown.png", "map2.txt", 6,8)
showBackground(scene1)
ClockAquired=False
ClockNumber=0
music = makeMusic("linkMusic.mp3")
link_die = makeSound("LOZ_Link_DIE.wav")
link_hit = makeSound("LOZ_Link_Hurt.wav")
enemy_die = makeSound("LOZ_Enemy_DIE.wav")
enemy_hit = makeSound("LOZ_Enemy_Hit.wav")
sword_slash = makeSound("LOZ_Sword_Slash.wav")

sword = Sword("Sworb.png", 4, 1)
showSprite(link)

projectiles = []

nextFrame = clock()
frame = 0
green = (0,102,0)
backgroundMusic=makeSound("linkMusic.mp3")
playSound(backgroundMusic,10)

bombs = newLabel(str(link.Bomb), 20, 'Arial', 'green', 200, 60,"clear")
#textboxGroup.add(bombs)
Items = [] 
showSprite(link)

HealthText = newLabel(str(link.health), 20, 'Arial', 'green', 200, 60,"clear")
MoneyText = newLabel(str(link.money), 20, 'Arial', 'green', 300, 60, "clear")

showLabel(HealthText)
showLabel(MoneyText)

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
                      #PlacableBomb.Placebomb
                      pass

              if event.type == pygame.KEYUP:
                  if event.key == pygame.K_SPACE:
                      hideSprite(sword)
                  if event.key == pygame.K_b:
                      if link.money >= 1:
                          link.shoot(linksProjectiles,frame)
                          link.money-=1
                      else:
                           pass
                  if event.key == pygame.K_LEFT:
                      link.speed = 0
                  if event.key == pygame.K_RIGHT:
                      link.speed = 0
                  if event.key == pygame.K_UP:
                      link.speed = 0
                  if event.key == pygame.K_DOWN:
                      link.speed = 0
       
        for enemy in scene1.Enemies:
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
                    scene1.Enemies.remove(enemy)
                    link.kills +=1
                item=enemy.hit(link.orientation)
                if item != None:
                    print(item)
                    showSprite(item)
                    Items.append(item)
                
            if touching (enemy, link):
                #killSprite(link)
                link.hit(enemy,ded)
                changeLabel(HealthText,str(link.health), green)
        for projectile in projectiles:
            projectile.move(frame)
            print(projectiles)
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
        #fairy.Move()
        sword.facing()
        link.move(frame)
        updateDisplay()

endWait()
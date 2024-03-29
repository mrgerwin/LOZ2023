from pygame_functions import *
from sprites import *

def sceneChange(direction):
    global currentScene, indexX, indexY, Items, LinkProjectiles
    
    #currentIndex = maps.index(currentScene)
    hideBackground(currentScene)
    for projectile in LinkProjectiles:
        killSprite(projectile)
        
    for item in Items:
        killSprite(item)
    
    LinkProjectiles = []
    Items = []
    
    
    
    if direction == "right":
        if indexX + 1>= len(maps[indexY]):
            indexX = 0
        else:
            indexX += 1
        currentScene = maps[indexY][indexX]
    
    elif direction == "left":
        if indexX - 1< 0:
            indexX = len(maps[indexY])-1
        else:
            indexX -= 1
        currentScene = maps[indexY][indexX]
    elif direction == "up":
        indexY += 1
        
        currentScene = maps[indexY][indexX]
    elif direction == "down":
        indexY -= 1
        currentScene = maps[indexY][indexX]
    
    showBackground(currentScene)
    hideSprite(link)
    showSprite(link)

screenX = 1024
screenY = 768

window = screenSize(screenX,screenY)

setBackgroundColour('grey')

setAutoUpdate(False)

#Making all sprites
link = Player()

BoomerangMove = False
BoomerangThrow = True

LinkProjectiles = []
map1 = Scene(window, link, "ZeldaMapTilesBrown.png", "map1.txt", 6,8)
map2 = Scene(window, link, "ZeldaMapTilesBrown.png", "map2.txt", 6,8)
map3 = Scene(window, link, "ZeldaMapTilesBrown.png", "map3.txt", 6,8)
map4 = Scene(window, link, "ZeldaMapTilesBrown.png", "map4.txt", 6,8)
map5 = Scene(window, link, "ZeldaMapTilesBrown.png", "map5.txt", 6,8)
map6 = Scene(window, link, "ZeldaMapTilesBrown.png", "map6.txt", 6,8)
map7 = Scene(window, link, "ZeldaMapTilesBrown.png", "map7.txt", 6,8)
map8 = Scene(window, link, "ZeldaMapTilesBrown.png", "map8.txt", 6,8)
map9 = Scene(window, link, "ZeldaMapTilesBrown.png", "map9.txt", 6,8)
map8 = Scene(window, link, "ZeldaMapTilesBrown.png", "map8.txt", 6,8)



low = [map7, map8, map9]
middle = [map3, map1, map2]
high = [map4, map5, map6]

maps = [low, middle, high]

indexX=1
indexY=1

currentScene = map1

showBackground(currentScene)

ClockAquired=False
ClockNumber=0
music = makeMusic("linkMusic.mp3")
linkIsDie = False
link_die = makeSound("LOZ_Link_DIE.wav")
#link_die = makeSound("link'sPain.mp3")
#link_die = makeSound("LinkInMaximumPain.mp3")
#link_die = makeSound("LinkScreamsForALittleBit.mp3")
link_hit = makeSound("LOZ_Link_Hurt.wav")
link_hit1 = makeSound("LinkHit1.mp3")
link_hit2 = makeSound("LinkHit2.mp3")
link_hit3 = makeSound("LinkHit3.mp3")
enemy_die = makeSound("LOZ_Enemy_DIE.wav")
enemy_hit = makeSound("LOZ_Enemy_Hit.wav")
sword_slash = makeSound("LOZ_Sword_Slash.wav")
#sword_slash = makeSound("MrBeast.mp3")
get_rupee = makeSound("LOZ_Get_Rupee.wav")

sword = Sword("Sworb.png", 4, 1)

boomerang = Boomerang(link, "Boomerang.png", 3, 1)
showSprite(link)
linksProjectiles = []
#projectiles = []


nextFrame = clock()
frame = 0
green = (0,102,0)
black = (0, 0, 0)
backgroundMusic=makeSound("linkMusic.mp3")
#backgroundMusic=makeSound("betterCallSaulTheme.mp3")
playSound(backgroundMusic,10)


bombs = newLabel(str(link.Bomb), 20, 'Arial', 'green', 200, 60,"clear")

Items = [] 
HealthText = newLabel(str(link.health), 20, 'Arial', 'black', 50, 50,"clear")
HealthWords = newLabel("Health", 20, 'Arial', 'black', 50, 30, "clear")
MoneyText = newLabel(str(link.money), 20, 'Arial', 'black', 150, 50, "clear")
MoneyWords = newLabel("Money", 20, 'Arial', 'black', 150, 30, "clear")
BombText = newLabel(str(link.Bomb), 20, 'Arial', 'black', 250, 50,"clear")
BombWords = newLabel("Bombs", 20, 'Arial', 'black', 250, 30, "clear")
explosion = Explosion
textboxGroup.add(BombText)
showLabel(HealthWords)
showLabel(HealthText)
showLabel(MoneyWords)
showLabel(MoneyText)
showLabel(BombWords)
textboxGroup.add(BombText)

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
                      if len(LinkProjectiles) >= 1:
                          print("other projectile not cleared")
                      elif link.health < 3:
                          print("not enough health to throw sword")
                      else:
                          
                          tsword=ThrowSword()
                          tsword.rect.x = link.rect.x
                          tsword.rect.y = link.rect.y
                          tsword.orientation  = link.orientation
                          LinkProjectiles.append(tsword)
                      showSprite(sword)
                      pygame.mixer.Sound.play(sword_slash)
                      
                  if event.key == pygame.K_LEFT:
                      link.orientation =3
                      hideSprite(sword)
                      link.speed = 6
                      
                  if event.key == pygame.K_RIGHT:
                      link.orientation =2
                      link.speed = 6
                      hideSprite(sword)
                      
                  if event.key == pygame.K_UP:
                      link.orientation =1
                      link.speed = 4
                      hideSprite(sword)
                      
                  if event.key == pygame.K_DOWN:
                      link.orientation =0
                      link.speed = 4
                      hideSprite(sword)
                    
                  if event.key == pygame.K_v:
                      link.speed = 12
                      

                  if event.key == pygame.K_c and BoomerangThrow == True:
                      boomerang.reset()
                      showSprite(boomerang)
                      boomerang.orientate()
                      BoomerangMove = True
                      BoomerangThrow = False
                      

                  if event.key == pygame.K_b:
                      #PlacableBomb.Placebomb
                      if link.Bomb >= 1:
                          link.Bomb -= 1
                          bomb = PlacableBomb(link.rect.x, link.rect.y, Explosion)
                          LinkProjectiles.append(bomb)
                          changeLabel(BombText,str(link.Bomb), 'black')
                          showSprite(bomb)
                      else:
                          pass
                  if event.key == pygame.K_s:
                      if link.money >= 1:
                          LinkProjectiles.append(link.shoot(frame))
                          link.money-=1
                          changeLabel(MoneyText,str(link.money), black)
                      else:
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
                  if event.key == pygame.K_v:
                      link.speed = 4
       
        for enemy in currentScene.Enemies:
            if ClockAquired==False:
                enemy.speed = enemy.ospeed
            else:
                enemy.speed = 0
                if ClockNumber==500:
                    ClockAquired=False
                    ClockNumber=0
                else:
                    ClockNumber+=1
                    #print(ClockNumber)
            projectile = enemy.move(frame,link)
            if projectile != None:
                currentScene.Projectiles.append(projectile)


            if touching(enemy, sword) or touching(enemy, boomerang):
                if touching(enemy, boomerang):
                    BoomerangMove = False
                    BoomerangThrow = True
                    hideSprite(boomerang) 
                    boomerang.reset()
                #killSprite(enemy)
                item=enemy.hit(link.orientation)
                if item != None:
                  showSprite(item)
                  Items.append(item)
                if enemy.health ==0:
                    pygame.mixer.Sound.play(enemy_die)
                    currentScene.Enemies.remove(enemy)
                    killSprite(enemy)
                    link.kills +=1
                else:
                    pygame.mixer.Sound.play(enemy_hit)   
          
            if touching (enemy, link):
                #killSprite(link)
                link.hit(enemy,ded,link.orientation) 
                changeLabel(HealthText,str(link.health), black)
                if link.health <= 0.4:
                    print("you died")
                    pygame.mixer.Sound.stop(backgroundMusic)
                    if linkIsDie == False:
                        pygame.mixer.Sound.play(link_die)
                        linkIsDie=True
        for projectile in currentScene.Projectiles:
            projectile.move(frame)
            if touching(link, projectile):
                link.hit(projectile, ded, link.orientation)
                changeLabel(HealthText,str(link.health), black)
                killSprite(projectile)
                currentScene.Projectiles.remove(projectile)

                if link.health <= 0.4:
                    killSprite(projectile)
                    currentScene.Projectiles.remove(projectile)
                    print("you died")
                    pygame.mixer.Sound.stop(backgroundMusic)
                    if linkIsDie == False:
                        pygame.mixer.Sound.play(link_die)
                        linkIsDie=True
        
        for projectile in LinkProjectiles:
            theExplosion = projectile.move(frame)
            
            if theExplosion == True:
                LinkProjectiles.remove(projectile)
                #LinkProjectiles.clear()
                killSprite(projectile)
            elif theExplosion == False:
                pass
            elif theExplosion != None:
                for projectile in theExplosion.explosionList:
                    LinkProjectiles.append(projectile)
            if projectile.rect.x >= 1028:
                killSprite(projectile)
                LinkProjectiles.remove(projectile)
            if projectile.rect.y >= 768:
                killSprite(projectile)
                LinkProjectiles.remove(projectile)
            if projectile.rect.y <= 0:
                killSprite(projectile)
                LinkProjectiles.remove(projectile)
            if projectile.rect.x <= 0:
                killSprite(projectile)
                LinkProjectiles.remove(projectile)
            for enemy in currentScene.Enemies:
                if touching(enemy, projectile):
                    try:
                        LinkProjectiles.remove(projectile)
                        killSprite(projectile)
                    except:
                        pass
                    print("Enemy hit by projectile")
                    item=enemy.hit(link.orientation)
                    if item != None:
                          print(item)
                          showSprite(item)
                          Items.append(item)
                    if enemy.health <= 0:
                        pygame.mixer.Sound.play(enemy_die)
                        currentScene.Enemies.remove(enemy)
                        link.kills +=1
                        
                    else:
                        pygame.mixer.Sound.play(enemy_hit)
                    
        for Item in Items:
            Item.animate(frame)
            if Item.rect.x > screenX or Item.rect.x<0 or Item.rect.y>screenY or Item.rect.y<0:
                Items.remove(Item)
                killSprite(Item)
            if touching (link, Item):
                if type(Item) == BlueRupee:
                    link.money +=5
                    pygame.mixer.Sound.play(get_rupee)
                    changeLabel(MoneyText,str(link.money), black)   
                elif type(Item) == BombItem:
                    link.Bomb +=1

                    changeLabel(BombText,str(link.Bomb), black)

                    print(link.Bomb)
                elif type(Item) == Rupee:
                    link.money += 1
                    pygame.mixer.Sound.play(get_rupee)
                    changeLabel(MoneyText,str(link.money), black)   
                elif type(item) == Heart:
                    if link.health <= 3:
                        link.health += 1
                    if link.health > 3:
                        link.health = 3
                    print("You commited a crime by stealing that heart, the FBI have been sent to your location "+ str(link.health) + " Heart")
                    changeLabel(HealthText,str(link.health), black)
                elif type(Item)==Clock:
                    ClockAquired=True
                elif type(Item)==Fairy:
                       link.health=3
                       changeLabel(HealthText,str(link.health), black)
                Items.remove(Item)
                killSprite(Item)
                print(link.money)
                    
            
        if link.health == 0:
            print("you died")
            ded = True
            Die()
        #fairy.Move()
        if BoomerangMove == True:
            boomerang.move()
            boomerang.animate()
            if boomerang.move() == True:
                BoomerangMove = False
                BoomerangThrow = True
        sword.facing()
        link.move(frame)
        for tile in currentScene.Wall_Tiles:
            if touching(link, tile):
                link.speed=0
                if link.orientation == 0:
                    link.rect.y -= link.speed
                    link.rect.y -=7
                elif link.orientation == 1:
                    link.rect.y += link.speed
                    link.rect.y +=7
                elif link.orientation == 2:
                    link.rect.x -= link.speed
                    link.rect.x -= 7
                elif link.orientation == 3:
                    link.rect.x += link.speed
                    link.rect.x +=7
            for enemy in currentScene.Enemies:
                if touching(tile, enemy):
                    enemy.turnAround()
        for tile in currentScene.Water_Tiles:
            for enemy in currentScene.Enemies:
                if touching(tile, enemy):
                    enemy.turnAround()
                
        if link.rect.x > screenX:
            sceneChange("right")
            link.rect.x = 1
        elif link.rect.x < 0:
            sceneChange("left")
            link.rect.x = screenX - 1
        elif link.rect.y <= 0:
            sceneChange("up")
            link.rect.y = screenY -1
        elif link.rect.y >= screenY:
            sceneChange("down")
            link.rect.y = 1
            
        updateDisplay()
endWait()
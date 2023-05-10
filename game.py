from pygame_functions import *

from sprites import Player, Octorok, WaterMonster, Projectile, BlueOctorok, Tektite, Sword, wizzrobe, Leever, Rock, TargetRock, HotWater, Item, Rubee, BlueRupee, drawScore, ThrowSword

screenSize(1024,768)
setBackgroundColour('grey')

setAutoUpdate(False)

#Making all sprites
link = Player()
#Scene1 = Scene(link, WaterMonster, "ZeldaMapTilesBrown", "map.txt", 6, 8)
music = makeMusic("linkMusic.mp3")
link_die = makeSound("LOZ_Link_DIE.wav")
link_hit = makeSound("LOZ_Link_Hurt.wav")
enemy_die = makeSound("LOZ_Enemy_DIE.wav")
enemy_hit = makeSound("LOZ_Enemy_Hit.wav")
sword_slash = makeSound("LOZ_Sword_Slash.wav")
sword_throw = makeSound("yeetsword.wav")


watermonster = WaterMonster(link)

tektite = Tektite()
#moblin = Moblin()
#dmoblin = DarkMoblin()
sword = Sword("Sworb.png", 4, 1)


enemies = [watermonster]
projectiles = []
showSprite(link)

#Bomb = BombItem()

#a_rock.orientation = 0


#heart1 = Heart()




for enemy in enemies:
    showSprite(enemy)
    
    
rubee = Rubee()

Items = [rubee]
for Item in Items:
    showSprite(Item)
    
LinkProjectiles = []   
    
#Experimenting with Rocks
a_rock = Rock()
a_rock.orientation = 0
showSprite(a_rock)
a_rock.rect.x = 500
a_rock.rect.y = 350

nextFrame = clock()
frame = 0
backgroundMusic=makeSound("linkMusic.mp3")
playSound(backgroundMusic,10)


#enemies = [octorok, Blueoctorok, watermonster, tektite, wizzrobe, leever, moblin, dmoblin]
#Items = [heart1, rupee1, bluerupee1, bluerupee2, bluerupee3, Bomb] 
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
                      if len(LinkProjectiles) >= 1:
                          print("other projectile not cleared")
                      else:
                          
                          tsword=ThrowSword()
                          tsword.rect.x = link.rect.x
                          tsword.rect.y = link.rect.y
                          tsword.orientation  = link.orientation
                          LinkProjectiles.append(tsword)
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
                    
       
        for enemy in enemies:
            projectile = enemy.move(frame, link)
            if projectile != None:
                projectiles.append(projectile)

            if touching(enemy, sword):
                #killSprite(enemy)
                print(enemy.health)
                if enemy.health <=1:
                    enemies.remove(enemy)
                    killSprite(enemy)
                    
                enemy.hit(link.orientation)
            if touching (enemy, link):
                #killSprite(link)
                if link.health == 0.5:
                    print("you died")
                link.hit(enemy,ded,link.orientation)
            for projectile in projectiles:
                projectile.move(frame)
                
            for Item in Items:
                if touching (link, Item):
                    if type(Item) == BlueRupee:
                        link.money +=5
                    Items.remove(Item)
                    killSprite(Item)
                    #Item.hit(bluerupee1)
                    print(link.money)
            
        for projectile in projectiles:
            projectile.move(frame)
            if touching(projectile, link):
                killSprite(link)
                link.hit(enemy, ded, link.orientation)
                playSound(link_hit)
            if projectile.rect.x>1028:
                killSprite(projectile)
                projectiles.remove(projectile)
                print("No Weapons?")
            if projectile.rect.y>768:
                killSprite(projectile)
                projectiles.remove(projectile)
                print("No Weapons?")
            
                
                
        for item in Items:
            if touching(link, item):
                Items.remove(item)
                killSprite(item)
        for projectile in LinkProjectiles:
            projectile.move(frame)
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
                
            if touching(enemy, projectile):
                enemy.hit(link.orientation)
                if enemy.health <=1:
                    print("Enemy hit by projectile")
                    #enemies.remove(enemy)
                    killSprite(enemy) 

        sword.facing()
        link.move(frame)
        #heart1.animate(frame)
        updateDisplay()

endWait()
from pygame_functions import *
from sprites import Player, Octorok, WaterMonster, Projectile, BlueOctorok, Tektite, Sword, wizzrobe, Leever, TargetRock, DarkMoblin, Moblin, Heart, Rupee, BlueRupee, BombItem, HotWater,Clock

screenSize(1024,768)
setBackgroundColour('grey')

setAutoUpdate(False)

#Making all sprites
link = Player()
ClockAquired=False
ClockNumber=0
music = makeMusic("linkMusic.mp3")
#link_die = makeSound("LOZ_Link_DIE.wav")
link_die = makeSound("link'sPain.mp3")
link_hit = makeSound("LOZ_Link_Hurt.wav")
enemy_die = makeSound("LOZ_Enemy_DIE.wav")
enemy_hit = makeSound("LOZ_Enemy_Hit.wav")
#sword_slash = makeSound("LOZ_Sword_Slash.wav")
sword_slash = makeSound("MrBeast.mp3")

Blueoctorok = BlueOctorok()
octorok = Octorok()
leever=Leever()
leeverspawned=True
showSprite(leever)

wizzrobe = wizzrobe(link)
watermonster = WaterMonster(link)

tektite = Tektite()
moblin = Moblin()
dmoblin = DarkMoblin()
sword = Sword("Sworb.png", 4, 1)


projectiles = []
showSprite(link)
Bomb = BombItem(link)
heart1 = Heart()
Bomb1 = BombItem(link)
rupee1 = Rupee()
bluerupee1 = BlueRupee()
bluerupee2 = BlueRupee()
bluerupee3 = BlueRupee()
clock1=Clock()
heart1.move(64,64)
rupee1.move(128, 64)
clock1.move(160,64)
Bomb1.rect.x = 156
Bomb1.rect.y = 64
bluerupee1.move(96,64)
bluerupee2.move(64, 96)
bluerupee3.move(46, 69)

watermonster = WaterMonster(link)
projectiles = []

nextFrame = clock()
frame = 0
backgroundMusic=makeSound("linkMusic.mp3")
playSound(backgroundMusic,10)


enemies = [octorok, Blueoctorok, watermonster, tektite, wizzrobe, leever, moblin, dmoblin]
Items = [heart1, rupee1, bluerupee1, bluerupee2, bluerupee3, Bomb1, clock1] 

showSprite(link)

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
                      pygame.mixer.Sound.play(sword_slash)
                      
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
                    print(ClockNumber)


            if touching(enemy, sword):
                #killSprite(enemy)
                if enemy.health ==1:
                    enemies.remove(enemy)
                    pygame.mixer.Sound.play(enemy_die)
                else:
                    pygame.mixer.Sound.play(enemy_hit)
                enemy.hit(link.orientation)
                
            if touching (enemy, link):
                #killSprite(link)
                if link.health>=0.5:
                    pygame.mixer.Sound.play(link_hit)
                elif link.health == 0:
                    print("you died")
                    pygame.mixer.Sound.stop(backgroundMusic)
                    pygame.mixer.Sound.play(link_die)
                link.hit(enemy,ded,link.orientation)
            for projectile in projectiles:
                projectile.move(frame)
                
        for Item in Items:
            Item.animate(frame)
            if touching (link, Item):
                if type(Item) == BlueRupee:
                    link.money +=5

                elif type(Item)==Clock:
                    ClockAquired=True

                elif type(Item) == Bomb:
                    link.bomb += 1

                Items.remove(Item)
                killSprite(Item)
                print(link.money)
            
        sword.facing()
        link.move(frame)
        updateDisplay()

endWait()
from sprites import Player, Octorok, WaterMonster, Projectile, BlueOctorok, Tektite, Sword, wizzrobe, Leever, TargetRock, DarkMoblin, Moblin

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
tektite = Tektite()
moblin = Moblin()
dmoblin = DarkMoblin()
sword = Sword("Sworb.png", 4, 1)



watermonster = WaterMonster(link)
projectiles = []
nextFrame = clock()
frame = 0
#backgroundMusic=makeSound("harderBetterFasterWhopper.mp3")
#backgroundMusic=makeSound("betterCallSaulTheme.mp3")
backgroundMusic=makeSound("linkMusic.mp3")
playSound(backgroundMusic,10)

enemies = [octorok, Blueoctorok, watermonster, tektite, wizzrobe, leever, moblin, dmoblin]
showSprite(link)
dieOn=False
ded=False
    

while True:
    if clock() >nextFrame:
        frame= (frame + 1)%2
        nextFrame += 80
        pause(10)
        
        if dieOn == False:
          if keyPressed("down"):
              link.orientation =0
              link.move(frame)
              hideSprite(sword)

          if keyPressed("up"):
              link.orientation =1
              link.move(frame)
              hideSprite(sword)

          if keyPressed("right"):
              link.orientation =2
              link.move(frame)
              hideSprite(sword)

          if keyPressed("left"):
              link.orientation =3
              link.move(frame)
              hideSprite(sword)

          if keyPressed("space"):
              changeSpriteImage(link, link.orientation + 8)
              sword.stab(link.rect.x, link.rect.y, link.orientation)
              showSprite(sword)

          if keyPressed("h"):
              changeSpriteImage(link, frame+12)
          if keyPressed("s"):
              link.move(frame)
        """
          if keyPressed("l"):
              leever.spawn(leever,frame)
              leeverspawned=True
          if leeverspawned==True:
              leever.move(frame)
        """
        for enemy in enemies:
            enemy.move(frame)
            if touching(enemy, link):
                link.hit(enemies,ded)
                print(link.health)
          #wizzrobe.Spellballmove(link.rect.x, link.rect.y)
            if touching(enemy, sword):
                enemy.health = enemy.health -1
                print(enemy.health)
                if enemy.health <=0:
                    hideSprite(enemy)



        sword.facing()


        rock.move(frame)



        updateDisplay()

endWait()
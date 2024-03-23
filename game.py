import pygame
import random
import math

pygame.init()   # initialize the pygame

# asserts
window_icon=pygame.image.load('./asserts/ufo.png')
main_background=pygame.image.load('./asserts/17520.jpg')
hero_spaceship=pygame.image.load('./asserts/spaceship2.png')
invader_img=pygame.image.load('./asserts/invader2.png')
bullet=pygame.image.load('./asserts/bullet2.png')

#Limits
heroXStartLimit=0
heroXEndLimit=738
heroYStartLimit=400
heroYEndLimit=500

#hero movements
heroSpaceshipX=380
heroSpaceshipY=500
changeX=0
changeY=0
heroSpeed=1

# invader movements
invaderImages=[]
invaderXs=[]
invaderYs=[]
invaderXSpeeds=[]
invaderYSpeeds=[]
numOfInvaders=6

for i in range(numOfInvaders):
    invaderImages.append(pygame.image.load('./asserts/invader.png'))
    invaderXs.append(random.randint(0,738))
    invaderYs.append(random.randint(30,150))
    invaderXSpeeds.append(.5)
    invaderYSpeeds.append(10)

#attack
shoot=False
bulletX=395
bulletY=465

# score
score=0
gameFont=pygame.font.Font('freesansbold.ttf',32)

screen = pygame.display.set_mode((800,600)) # passing display width and height
pygame.display.set_caption('Interstellar Investigator')
pygame.display.set_icon(window_icon)

endGame=False

def hero():
    screen.blit(hero_spaceship,(heroSpaceshipX,heroSpaceshipY))

def invader(invaderX,invaderY):
    screen.blit(invader_img,(invaderX,invaderY))

def attack():
    screen.blit(bullet,(bulletX,bulletY))

def collision(invaderX,invaderY):
    distance=math.sqrt((invaderX-bulletX)**2+(invaderY-bulletY)**2)
    if distance<27:
        return True

def showScore():
    scoreDisplay=gameFont.render('Score: '+str(score),True,(255,255,255))
    screen.blit(scoreDisplay,(10,10))

def gameOver():
    pygame.event.set_blocked(pygame.KEYDOWN)
    gameOverFont=pygame.font.Font('freesansbold.ttf',64)
    gameOverDisplay=gameOverFont.render('GAME OVER',True,(255,255,255))
    screen.blit(gameOverDisplay,(200,250))

while not endGame:
    screen.blit(main_background,(0,0)) # background image and its inital position
    
    for event in pygame.event.get(): # event monitoring
        if event.type==pygame.QUIT:
            endGame=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                changeX-=heroSpeed
            if event.key==pygame.K_RIGHT:
                changeX+=heroSpeed
            if event.key==pygame.K_UP:
                changeY-=heroSpeed
            if event.key==pygame.K_DOWN:
                changeY+=heroSpeed
            if event.key==pygame.K_SPACE:
                if not shoot: # check if bullet is not already shot
                    shoot=True
                    bulletX=heroSpaceshipX+15 # bullet postion as spaceship position
                    bulletY=heroSpaceshipY-30 # bullet postion as spaceship position
        if event.type==pygame.KEYUP:
            changeX=0
            changeY=0

    heroSpaceshipX+=changeX
    heroSpaceshipY+=changeY

    #movement limits for hero spaceship
    if heroSpaceshipX<=heroXStartLimit:
        heroSpaceshipX=heroXStartLimit
    if heroSpaceshipX>=heroXEndLimit:
        heroSpaceshipX=heroXEndLimit
    if heroSpaceshipY<=heroYStartLimit:
        heroSpaceshipY=heroYStartLimit
    if heroSpaceshipY>=heroYEndLimit:
        heroSpaceshipY=heroYEndLimit
    
    # for invaders to bouncing back and forth
    for i in range(numOfInvaders):
        if invaderYs[i] >= 350: # checking if invader has reached the spaceship
            invaderYs[i]=3000
            gameOver()
        invaderXs[i]+=invaderXSpeeds[i] # changing the speed
        if invaderXs[i]<=0:
            invaderXSpeeds[i]=+abs(invaderXSpeeds[i])
            invaderYs[i]+=invaderYSpeeds[i]
        if invaderXs[i]>=738:
            invaderXSpeeds[i]=-abs(invaderXSpeeds[i])
            invaderYs[i]+=invaderYSpeeds[i]
        
        if collision(invaderXs[i],invaderYs[i]): # checking for collision
            # reset the invader
            invaderXs[i]=random.randint(0,738)
            invaderYs[i]=random.randint(30,150)
        
            # reset the bullet
            bulletY=490
            shoot=False
        
            # increase the score
            score+=1
        invader(invaderXs[i],invaderYs[i]) 
       
    # shooting
        
    if bulletY<=0: # resetting the bullet
        bulletY=490
        shoot=False # to ensure only one bullet is fired
    
    if shoot: # moving the bullet
        attack()
        bulletY-=1  # bullet speed

    hero()
    #collision()
    showScore()
    
    pygame.display.update()
import pygame
import random
import math
from database import GameDatabase
from pygame import mixer

class Game:
    def __init__(self, name):
        pygame.init()   # initialize pygame
        mixer.init()

        # background music
        mixer.music.load('Rock_Metal_Valhalla_by_Alexander_Nakarada.mp3')
        pygame.mixer.music.set_volume(0.3)  # Set volume (0.0 to 1.0)
        mixer.music.play(-1)

        self.laser_sound = mixer.Sound('laser_shoot.mp3')
        self.laser_sound.set_volume(0.1)
        # when player loses
        self.death_sound = mixer.Sound('videogame-death-sound.mp3')

        # asserts
        window_icon = pygame.image.load('./asserts/ufo.png')
        self.main_background = pygame.image.load('./asserts/17520.jpg')
        self.hero_spaceship = pygame.image.load('./asserts/spaceship2.png')
        self.invader_img = pygame.image.load('./asserts/invader2.png')
        self.bullet = pygame.image.load('./asserts/bullet2.png')

        # Limits
        self.heroXStartLimit = 0
        self.heroXEndLimit = 738
        self.heroYStartLimit = 400
        self.heroYEndLimit = 500

        # hero movements
        self.heroSpaceshipX = 380
        self.heroSpaceshipY = 500
        self.changeX = 0
        self.changeY = 0
        self.heroSpeed = 1

        # invader movements
        self.invaderImages = []
        self.invaderXs = []
        self.invaderYs = []
        self.invaderXSpeeds = []
        self.invaderYSpeeds = []
        self.numOfInvaders = 6

        #DB
        self.db = GameDatabase()
        self.user_name = name

        for i in range(self.numOfInvaders):
            self.invaderImages.append(pygame.image.load('./asserts/invader.png'))
            self.invaderXs.append(random.randint(0, 738))
            self.invaderYs.append(random.randint(30, 150))
            self.invaderXSpeeds.append(.5)
            self.invaderYSpeeds.append(10)

        # attack
        self.shoot = False
        self.bulletX = 395
        self.bulletY = 465

        # score
        self.score = self.db.get_player_score(self.user_name)
        self.gameFont = pygame.font.Font('freesansbold.ttf', 32)

        self.screen = pygame.display.set_mode((800, 600))  # passing display width and height
        pygame.display.set_caption('Interstellar Investigator')
        pygame.display.set_icon(window_icon)

        self.endGame = False

    def hero(self):
        self.screen.blit(self.hero_spaceship, (self.heroSpaceshipX, self.heroSpaceshipY))

    def invader(self, invaderX, invaderY):
        self.screen.blit(self.invader_img, (invaderX, invaderY))

    def attack(self):
        self.screen.blit(self.bullet, (self.bulletX, self.bulletY))

    def collision(self, invaderX, invaderY):
        distance = math.sqrt((invaderX - self.bulletX) ** 2 + (invaderY - self.bulletY) ** 2)
        if distance < 27:
            return True

    def showScore(self):
        scoreDisplay = self.gameFont.render('Score: ' + str(self.score), True, (255, 255, 255))
        self.screen.blit(scoreDisplay, (10, 10))

    def gameOver(self):
        pygame.event.set_blocked(pygame.KEYDOWN)
        gameOverFont = pygame.font.Font('freesansbold.ttf', 64)
        gameOverDisplay = gameOverFont.render('GAME OVER', True, (255, 255, 255))
        self.screen.blit(gameOverDisplay, (200, 250))
        self.death_sound.play()
        self.db.update_player_score(self.user_name, self.score)

    def run(self):
        while not self.endGame:
            self.screen.blit(self.main_background, (0, 0))  # background image and its initial position

            for event in pygame.event.get():  # event monitoring
                if event.type == pygame.QUIT:
                    self.endGame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.changeX -= self.heroSpeed
                    if event.key == pygame.K_RIGHT:
                        self.changeX += self.heroSpeed
                    if event.key == pygame.K_UP:
                        self.changeY -= self.heroSpeed
                    if event.key == pygame.K_DOWN:
                        self.changeY += self.heroSpeed
                    if event.key == pygame.K_SPACE:
                        if not self.shoot:  # check if bullet is not already shot
                            self.shoot = True
                            self.bulletX = self.heroSpaceshipX + 15  # bullet position as spaceship position
                            self.bulletY = self.heroSpaceshipY - 30  # bullet position as spaceship position
                            # laser sound while shooting
                            self.laser_sound.play()
                if event.type == pygame.KEYUP:
                    self.changeX = 0
                    self.changeY = 0

            self.heroSpaceshipX += self.changeX
            self.heroSpaceshipY += self.changeY

            # movement limits for hero spaceship
            if self.heroSpaceshipX <= self.heroXStartLimit:
                self.heroSpaceshipX = self.heroXStartLimit
            if self.heroSpaceshipX >= self.heroXEndLimit:
                self.heroSpaceshipX = self.heroXEndLimit
            if self.heroSpaceshipY <= self.heroYStartLimit:
                self.heroSpaceshipY = self.heroYStartLimit
            if self.heroSpaceshipY >= self.heroYEndLimit:
                self.heroSpaceshipY = self.heroYEndLimit

            # for invaders to bouncing back and forth
            for i in range(self.numOfInvaders):
                if self.invaderYs[i] >= 350:  # checking if invader has reached the spaceship
                    self.invaderYs[i] = 3000
                    self.gameOver()
                self.invaderXs[i] += self.invaderXSpeeds[i]  # changing the speed
                if self.invaderXs[i] <= 0:
                    self.invaderXSpeeds[i] = +abs(self.invaderXSpeeds[i])
                    self.invaderYs[i] += self.invaderYSpeeds[i]
                if self.invaderXs[i] >= 738:
                    self.invaderXSpeeds[i] = -abs(self.invaderXSpeeds[i])
                    self.invaderYs[i] += self.invaderYSpeeds[i]

                if self.collision(self.invaderXs[i], self.invaderYs[i]):  # checking for collision
                    # reset the invader
                    self.invaderXs[i] = random.randint(0, 738)
                    self.invaderYs[i] = random.randint(30, 150)

                    # reset the bullet
                    self.bulletY = 490
                    self.shoot = False

                    # increase the score
                    self.score += 1
                self.invader(self.invaderXs[i], self.invaderYs[i])

            # shooting
            if self.bulletY <= 0:  # resetting the bullet
                self.bulletY = 490
                self.shoot = False  # to ensure only one bullet is fired

            if self.shoot:  # moving the bullet
                self.attack()
                self.bulletY -= 1  # bullet speed

            self.hero()
            self.showScore()

            pygame.display.update()
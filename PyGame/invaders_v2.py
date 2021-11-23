import pygame
from pygame.locals import*
import math
import random

# Define some colours
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)



class Game_screen():

    def __init__(self):
        self.size = (700,500)
        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.font.SysFont('Calibri',25,True, False)
        pygame.display.set_caption("MyGame")
    # end of constructor

    def update_screen(self,lives, score, bullet_count):
        text = self.font.render("Lives: " + str(lives),True,WHITE)
        self.screen.blit(text,[30,30])
        text = self.font.render("Score: " + str(score),True,WHITE)
        self.screen.blit(text,[30,60])
        text = self.font.render("Bullets: " + str(50 - bullet_count),True,WHITE)
        self.screen.blit(text,[30,90])

    # end procedure

#### end Game_screen class

class enemy(pygame.sprite.Sprite):
    # Define the constructor function

    def __init__(self, color, width, height, speed):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = speed
        self.rect.x = random.randrange(0,600)
        self.rect.y = 0

    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        if self.rect.y > 500:
             self.reset_pos()
             
    def reset_pos(self):
        self.rect.x = random.randrange(0,690)
        self.rect.y = 0

### end enemy class

class attacker(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x_speed = 0
        self.y_speed = 0
        self.rect.x = 200
        self.rect.y = 490

    def get_x(self):
        return self.rect.x

    def update(self):
  
        # Chekc position of player to avoid it going off the screen
        if self.rect.x < 0 or self.rect.x > 690:
            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > 690:
                self.rect.x = 690
        else:    
            self.rect.x = self.rect.x + self.x_speed

#### End attacker class

class bullet(pygame.sprite.Sprite):

    def __init__(self, color, width, height,x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.y_speed = -3
        self.rect.x = x_pos
        self.rect.y = y_pos

    def update(self):
         
        if self.rect.y < 0:
            self.rect.y = -50
        else:
            self.rect.y = self.rect.y + self.y_speed

### end bullet class

class Game(pygame.sprite.Sprite):

    def __init__(self):

        self.attacker_list = pygame.sprite.Group()
        self.block_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.x_speed = 0
        self. y_speed = 1
        self.score = 0
        self.no_of_blocks = 6
        self.lives = 3
        self.bullet_count = 0
        self.start_game_flag = True
        self.the_screen = Game_screen()

        # create player and add to all sprites list for the game
        self.player = attacker(RED,10,10)
        self.attacker_list.add(self.player)
        self.all_sprites_list.add(self.player)

        # Add all the enemies
        self.start_game()

    # end of initialisor

    def logic(self):

        # Check for a player enemy collision
        bullet_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, False)
        
        # take a life off for all enemies hitting and reset
        for foo in bullet_hit_list:
            self.lives -= 1
            self.score -= 30
            foo.reset_pos()

        bullet_hit_list = pygame.sprite.groupcollide(self.block_list, self.bullet_list, True, True)
        
        for me in bullet_hit_list:
            self.score +=20

        if self.lives == 0:
            return  "stop"

        if not self.block_list:
            return "newgame"

        self.all_sprites_list.update()
    # end of update procedure

    def start_game(self):
        for x in range(self.no_of_blocks):
            my_enemy = enemy(WHITE, 10, 10,self.y_speed)
            self.block_list.add(my_enemy)
            self.all_sprites_list.add(my_enemy)           
    
    def add_bullet(self):
        mybullet = bullet(RED,5,5, g.player.get_x(), 490)
        self.all_sprites_list.add(mybullet)
        self.bullet_list.add(mybullet)
        self.bullet_count = self.bullet_count + 1

    def update_screen(self):
        self.the_screen.update_screen(self.lives,self.score,self.bullet_count)

    def key_check(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "stop"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.x_speed = -3

                elif event.key == pygame.K_RIGHT:
                    self.player.x_speed = 3

                elif event.key == pygame.K_UP:
                    if self.bullet_count > 49:
                        pass
                    else:
                        self.add_bullet()
                        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.x_speed = 0

### end Game class


pygame.init()

# Loop until the user clicks the close button
done = False

# used to manage time .. how fast the screen updates
clock = pygame.time.Clock()



# Game object intantiated
g = Game()

#### Main game loop
while not done:

    ### Chekc the keys
    ret = g.key_check()
    if ret == "stop":
        done = True

    # Run the game logic function
    g.logic()

    # draw the screen
    g.the_screen.screen.fill(BLACK)

    #Update the screen text
    g.update_screen()
    

    # Draw all the sprites
    g.all_sprites_list.draw(g.the_screen.screen)

    
    # update the screen
    pygame.display.flip()

    # tick the clock on
    clock.tick(60)
    
pygame.quit()



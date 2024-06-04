import pygame, sys
from pygame.math import Vector2
import matplotlib.pyplot as plt

pygame.init()


#set no of blocks should be there in screen to form grid
cell_size = 20
cell_number = 50

screen_size = cell_number * cell_size

#define screen area for displaying game
screen = pygame.display.set_mode((screen_size,screen_size))
screen.fill((175,215,70)) # screen background color 

pygame.display.set_caption("train mode")


clock = pygame.time.Clock()


class BOT:
    def __init__(self):
        self.x = 25
        self.y = 700
        self.pos = Vector2(self.x,self.y)
        self.direction = Vector2(0,0)
        self.path = []
        self.new_pos = self.pos
    def draw_bot(self):
        bot_rect = pygame.Rect(int(self.pos.x),
                                 int(self.pos.y),
                                 cell_size * 5,
                                 cell_size * 5)
        pygame.draw.rect(screen,(255,255,255),bot_rect)
    
    def move_bot(self):
        self.new_pos = self.pos + self.direction

        bot_rect = pygame.Rect(self.new_pos.x,
                               self.new_pos.y,
                               cell_size * 5,
                               cell_size * 5)

        # Check for collision with blocks
        if not (bot_rect.colliderect(block.get_rect()) or
                bot_rect.colliderect(block2.get_rect()) or
                bot_rect.colliderect(block3.get_rect()) or
                bot_rect.colliderect(block4.get_rect())):
            self.pos = self.new_pos

        if len(self.path) == 0:
            self.path.append((self.pos.x, self.pos.y))

        if len(self.path) != 0:
            if (self.path[-1][0] != self.new_pos.x) or (self.path[-1][1] != self.new_pos.y):
                self.path.append((self.pos.x, self.pos.y))

    def save_path_to_file(self, filename="bot_path.txt"):
        with open(filename, 'w') as file:
            for position in self.path:
                file.write(f"{position[0]}, {position[1]}\n")

 

class BLOCK:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.pos = Vector2(self.x,self.y)
    def draw_block(self):
        block_rect = pygame.Rect(int(self.pos.x),
                                 int(self.pos.y),
                                 cell_size * 3,
                                 cell_size * 30)
        pygame.draw.rect(screen,(150,75,0),block_rect)
    
    def get_rect(self):
        return pygame.Rect(int(self.pos.x),
                           int(self.pos.y),
                           cell_size * 3,
                           cell_size * 30)

block = BLOCK(150,150)
block2 = BLOCK(360,150)
block3 = BLOCK(570,150)
block4 = BLOCK(780,150)
bot = BOT()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bot.direction = Vector2(0,-10)
                
            elif event.key == pygame.K_DOWN:
                bot.direction = Vector2(0,10)
                
            elif event.key == pygame.K_LEFT:
                bot.direction = Vector2(-10,0)
                
            elif event.key == pygame.K_RIGHT:
                bot.direction = Vector2(10,0)

            if event.key == pygame.K_s:
                bot.save_path_to_file("bot_path.txt")
            if event.key == pygame.K_p:
                print(bot.path[-1][0])
                print(bot.new_pos.x)

        if event.type == pygame.KEYUP:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    bot.direction = Vector2(0, 0)  
            

            
    
    screen.fill((175,215,70)) # screen background color         
    block.draw_block()
    block2.draw_block()
    block3.draw_block()
    block4.draw_block()
    bot.move_bot()
    bot.draw_bot()
    
    pygame.display.update()
    clock.tick(60)

    



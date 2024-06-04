import pygame
import sys
from pygame.math import Vector2

pygame.init()

cell_size = 20
cell_number = 50
screen_size = cell_number * cell_size

screen = pygame.display.set_mode((screen_size, screen_size))
screen.fill((175, 215, 70))
pygame.display.set_caption("path following")

SCREEN_UPDATE = pygame.USEREVENT

pygame.time.set_timer(SCREEN_UPDATE,150)

clock = pygame.time.Clock()


class BOT:
    def __init__(self, path):
        self.path = path
        self.path_index = 0
        self.pos = Vector2(self.path[self.path_index])

    def draw_bot(self):
        bot_rect = pygame.Rect(int(self.pos.x),
                               int(self.pos.y),
                               cell_size * 5,
                               cell_size * 5)
        pygame.draw.rect(screen, (255, 255, 255), bot_rect)

    def move_bot(self):
        if self.path_index < len(self.path) - 1:
            self.path_index += 1
            self.pos = Vector2(self.path[self.path_index])


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


def read_bot_path(filename="bot_path.txt"):
    path = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split(','))
            path.append((x, y))
    return path


bot_path = read_bot_path()
bot = BOT(bot_path)

trip = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            bot.move_bot()

    screen.fill((175, 215, 70))
    

    block.draw_block()
    block2.draw_block()
    block3.draw_block()
    block4.draw_block()
    bot.draw_bot()

    pygame.display.update()
    clock.tick(100)

    if bot.path_index == len(bot.path) -1:
        bot.path.reverse()
        bot.path_index = 0
        trip +=1
        if trip == 2:
            break

pygame.display.quit()
pygame.quit()
sys.exit()
import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 22
HEIGHT = 22
MARGIN = 3


class Grid:
    def __init__(self, width, height, margin):
        self.width = width
        self.height = height
        self.margin = margin
        self.grid = [[0 for y in range(height)] for x in range(width)]
        self.font = pygame.font.SysFont(None, 20)

    def draw(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                pygame.draw.rect(screen, WHITE, [(self.margin + WIDTH) * col + self.margin,
                                                 (self.margin + HEIGHT) * row + self.margin,
                                                 WIDTH, HEIGHT])
                if row == 0:
                    number = self.font.render(str(col+1), True, BLACK)
                    screen.blit(number, ((self.margin + WIDTH) * col + self.margin + 8, self.margin - 20))
                if col == 0:
                    number = self.font.render(str(row+1), True, BLACK)
                    screen.blit(number, (self.margin - 20, (self.margin + HEIGHT) * row + self.margin + 8))



class Field:
    def __init__(self, grid):
        self.grid = grid

    def fill(self, row, col, color):
        pygame.draw.rect(screen, color, [(self.grid.margin + WIDTH) * col + self.grid.margin,
                                         (self.grid.margin + HEIGHT) * row + self.grid.margin,
                                         WIDTH, HEIGHT])

pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

grid = Grid(20, 20, 3)
field = Field(grid)

done = False

clock = pygame.time.Clock()

while not done:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               done = True

          # ---
          # The code here ist called once per clock tick
          # Let your algorithm loop here
               # ---

          screen.fill(BLACK)

                    # ---
               # The screen is empty here
          # Put your 'drawing' code here
                    #
                    #   RECTANGEL EXAMPLE
                    #
          #   The third Parameter defines the rectangles positioning etc: [y-pos,x-pos,width,height]
          #pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * y + MARGIN, (MARGIN + HEIGHT) * x + MARGIN,WIDTH,HEIGHT])
          grid.draw(screen)

          # Fill some example cells
          for i in range(10,20):
               field.fill(i,9,BLACK)
          for i in range(4,10):
               field.fill(10, i, BLACK)
          for i in range(0,11):
               field.fill(i,16,BLACK)


          pygame.display.flip()

clock.tick(60)
pygame.quit()
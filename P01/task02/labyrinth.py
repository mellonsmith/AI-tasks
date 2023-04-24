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


# ---
# Initialize your classes etc.here
# ---

pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

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
          # pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * y + MARGIN,
                    #               (MARGIN + HEIGHT) * x + MARGIN,WIDTH,HEIGHT])
                    # ---


          pygame.display.flip()

clock.tick(60)
pygame.quit()
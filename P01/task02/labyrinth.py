import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 19
HEIGHT = 19
MARGIN = 3


class Grid:
    def __init__(self, width, height, margin):
        self.width = width
        self.height = height
        self.margin = margin
        self.grid = [[0 for y in range(height )] for x in range(width )]
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
          self.grid.grid[row][col] = 1
          
     def isfilled(self, row, col):
          return self.grid.grid[row][col] == 1 or row < 0 or row > 19 or col < 0 or col > 19
     
class Labyrinth:
     def __init__(self, field):
          self.field = field
          self.current = (0,0)
          self.start = (19,0)
          self.end = (0,19)
          self.path = []
          self.path.append(self.start)
     
     def setStart(self, row, col):
          self.start = (row, col)
     
     def setEnd(self, row, col):
          self.end = (row, col)
     
     def goLeft(self):
          self.path.append((self.path[-1][0], self.path[-1][1]-1))
          self.current = self.path[-1]
          self.field.fill(self.current[0], self.current[1], RED)
          
     def goRight(self):
          self.path.append((self.path[-1][0], self.path[-1][1]+1))
          self.current = self.path[-1]
          self.field.fill(self.current[0], self.current[1], RED)
          
     def goUp(self):
          self.path.append((self.path[-1][0]-1, self.path[-1][1]))
          self.current = self.path[-1]
          self.field.fill(self.current[0], self.current[1], RED)
          
     def goDown(self):
          self.path.append((self.path[-1][0]+1, self.path[-1][1]))
          self.current = self.path[-1]
          self.field.fill(self.current[0], self.current[1], RED)
     
     def heuristic(self, row, col):
          return math.sqrt((row - self.end[0])**2 + (col - self.end[1])**2)
     
     def pathfinding_astar(self):
        open_list = [self.start]
        closed_list = []
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(*self.start)}
        
        while open_list:
            current = min(open_list, key=f_score.get)
            if current == self.end:
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                path.reverse()
                for node in path:
                    self.field.fill(*node, RED)
                return path
            open_list.remove(current)
            closed_list.append(current)
            for neighbor in [(current[0]-1, current[1]), (current[0]+1, current[1]), (current[0], current[1]-1), (current[0], current[1]+1)]:
                if neighbor in closed_list or self.field.isfilled(*neighbor):
                    continue
                tentative_g_score = g_score[current] + 1
                if neighbor not in open_list:
                    open_list.append(neighbor)
                elif tentative_g_score >= g_score[neighbor]:
                    continue
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + self.heuristic(*neighbor)
          
          
          
     #def aStar(self):

pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

grid = Grid(20, 20, 3)
field = Field(grid)

done = False

clock = pygame.time.Clock()

while True:
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
          l = Labyrinth(field)
          field.fill(l.start[0], l.start[1], BLUE)
          field.fill(l.end[0], l.end[1], GREEN)
          l.pathfinding_astar()
               

          pygame.display.flip()

clock.tick(60)
pygame.quit()
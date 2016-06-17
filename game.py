import sys, pygame, time
pygame.init()

level_width = 25
level_height = 15
blocksize = 50
size = level_width*blocksize, level_height*blocksize
gold = 212, 175, 55
red = 255, 0, 0
blue = 0, 0, 255
GRAVITY = 2

screen = pygame.display.set_mode(size)

class Block():
    def __init__(self, colour):
        self.colour = colour
    
    def draw(self, x, y):
        pygame.draw.rect(screen, self.colour, (x, y, blocksize, blocksize))
        
red_block = Block(red)
blue_block = Block(blue)

class Man():
    position = [25, 25]
    velocity = [0, 0]
    height = 50

    def draw(self):
        pygame.draw.rect(screen, gold, (self.position[0], self.position[1], 20, self.height))

    def update_position(self):
        bottom = size[1] - self.height
        final_y = self.position[1] + self.velocity[1]
        if final_y > bottom:
            self.velocity = [0, 0]
            self.position[1] = bottom
        if self.position[0] < bottom:
            self.velocity[1] += GRAVITY
            self.position[1] += self.velocity[1]
        
        self.position[0] += self.velocity[0]
        
        
class Level():
    blocks = [[blue_block] * level_width] * (level_height - 1)
    blocks.append([red_block] * level_width)

    def draw(self):
        for j, row in enumerate(self.blocks):
            for i, block in enumerate(row):
                block.draw(i * blocksize, j * blocksize)

level1 = Level()
man = Man()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                man.velocity[0] = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                man.velocity[0] = 0

    level1.draw()
    man.update_position()
    man.draw()
    pygame.display.flip()
    time.sleep(0.001)

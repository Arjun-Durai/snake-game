import pygame
import random

pygame.init()

width = 1000
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame basics")

running = True

background_color = pygame.Color("black")
snake_color = pygame.Color('Green')

black = (0, 0, 0)
white = (255, 255, 255)

block_size = 10

snake = [(100, 100)]  # single block

# 0  1  2   3  4  5
# listx = [10,20,30,40,50,60]
#
# print(listx[3])

#            0  1    0   1    0   1
# listx = [(10,20), (30,40), (50,60)]
#             0        1       2

# listx[0][1]

# listx[2][0]

# list : 3 elements

# listx[0] -----> (10,20)


# list ----> one element ----> (100,100)     0
#
# (100,100) -------> 0 1

direction = (block_size, 0)  # moving along right side

clock = pygame.time.Clock()

# left side ------> (-block_size,0)
# down   --------> (0,block_size)
# up -------------> (0,-block_size)
#
# 1 to 20
# 0 to 19

food = (random.randint(0, width // block_size - 1) * block_size,
        random.randint(0, height // block_size - 1) * block_size)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = (-block_size, 0)

            elif event.key == pygame.K_RIGHT:
                direction = (block_size, 0)

            elif event.key == pygame.K_DOWN:
                direction = (0, block_size)

            elif event.key == pygame.K_UP:
                direction = (0, -block_size)

    screen.fill(background_color)  # to update the display screen
    new_pos = (snake[0][0] + direction[0], snake[0][1] + direction[1])# tuple
    # snake[0] = new_pos # tuple


    # pygame.draw.rect(screen, snake_color, (snake[0][0], snake[0][1], block_size, block_size))

    # Check for collisions
    if (new_pos in snake or
            new_pos[0] < 0 or new_pos[0] >= width or
            new_pos[1] < 0 or new_pos[1] >= height):
        running = False  # Game over

    snake.insert(0, new_pos)

    if new_pos == food:

        food = (random.randint(0, width // block_size- 1) *block_size,
                random.randint(0, height // block_size - 1) * block_size)
    else:
        snake.pop()  # Remove tail if no food eaten

    for block in snake:
        pygame.draw.rect(screen, 'green',(block[0],block[1],block_size,block_size))




    pygame.draw.rect(screen, 'red', (food[0], food[1], block_size, block_size))

    pygame.display.flip()
    clock.tick(10)

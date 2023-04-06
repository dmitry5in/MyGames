import pygame

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Games")
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("arial", 32)
follow = font.render("Какой-то текст", True, RED, GREEN)
like = font.render("Текст", True, BLUE, RED)
width, height = like.get_size()
x, y = (0, 300)
direct_x = 3
direct_y = 3
clock = pygame.time.Clock()
FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    clock.tick(FPS)
    screen.fill(BLACK)
    screen.blit(follow, (0, 0))
    screen.blit(like, (x, y))
    x += direct_x
    y += direct_y
    if x + width >= 800 or x == 0:
        direct_x = -direct_x
    if y + height >= 600 or y == 0:
        direct_y = -direct_y
    pygame.display.update()


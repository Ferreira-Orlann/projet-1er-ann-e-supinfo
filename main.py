import sys, pygame

if __name__ == "__main__":
    pygame.init()
    
screen = pygame.display.set_mode((500,500))
black = 0, 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    pygame.display.flip()
import pygame

# Initialize pgame

pygame.init()
# Create screen
screen = pygame.display.set_mode((800, 600))

running = True

#titel and icon
pygame.display.set_caption("gomu gomu no")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# adding player img
playerimg = pygame.image.load("spaceshipp.png")

playerx = 370
playery = 480

# defing function to draw player on screen
def player(x,y):
    screen.blit(playerimg,(x,y))


# game loop
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if key is pressed cheak wether key pressed is left or right

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left key pressed")

            if event.key == pygame.K_RIGHT:
                print("right key pressed")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("key is released")

    # backgroud colour

    player(playerx,playery)
    # we have to update screen every time loop run so
    pygame.display.update()




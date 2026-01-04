import pygame
pygame.init() #initialise pygame engine

#Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hallelujah")

done = False
clock = pygame.time.Clock()
 
#Main Program Loop 
while not done:
    # --- Main event loop - Code for mouse keyboard + mouse clicks go here
    for event in pygame.event.get(): #User did something
        if event.type == pygame.QUIT: #If user clicked close
            done = True #Exit this loop
 
    #Game logic
 #Code for objects etc.
  
    #Drawing code
    screen.fill(WHITE) #Background - drawing comes after

    pygame.display.flip() #"Update the full display Surface to the screen"
 
    clock.tick(60) #Frame rate limit

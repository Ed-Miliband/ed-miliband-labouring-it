import pygame
from MainMenu import LoginPage
from MainMenu import NewGame
from Saves import SaveLoad

A = True #Constant

def main_menu(): #Main menu screen
  pygame.display.set_caption("Menu")

 while A = True:
   screen.blit(BG, (0, 0)) #set background

   MENU_MOUSE_POS = pygame.mouse.get_pos() #mouse position
   
   MENU_TEXT = get_font (100).render("MAIN MENU", True, "#b68f40") 
   MENU_RECT = MENU_TEXT.get_rect (center=(640, 100))

   NEWGAME_BUTTON = Button (image=pygame.image.load("assets/Play Rect.png"), pos=(640, 50), text_input="NEW GAME", font=get_font (75), base_color="#d7fcd4", hovering_color="White")
   PLAY_BUTTON = Button (image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), text_input="PLAY", font=get_font (75), base_color="#d7fcd4", hovering_color="White")
   OPTIONS_BUTTON = Button (image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), text_input="OPTIONS", font=get_font (75), base_color="#d7fcd4", hovering_color="White")
   QUIT_BUTTON = Button (image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), text_input="QUIT", font=get_font (75), base_color="#d7fcd4", hovering color="White")

   SCREEN.blit (MENU_TEXT, MENU_RECT)

  for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]: 
    button.changeColor (MENU_MOUSE_POS)
    button.update(SCREEN)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if PLAY_BUTTON. check For Input (MENU_MOUSE_POS): 
        play()
    if OPTIONS_BUTTON.checkForInput (MENU_MOUSE_POS):
      options()
    if QUIT_BUTTON.checkForInput (MENU_MOUSE_POS):
      pygame.quit() 
      sys.exit()
      
  pygame.display.update()

main_menu()

def NewNewGame():
  NewGame()
  
def play():
  loadGame()
  loadLevel()

def options(): 
   pygame.display.set_caption("Options") #filler menu tbh

   while A = True:
    screen.blit(BG, (0, 0)) #set background
    asurf = pygame.image.load(ed_lees_band.jpg) #i luv speedy gonzalez

   MENU_MOUSE_POS = pygame.mouse.get_pos() #mouse position

   OPTIONS_OPTIONS = pos=(640, 250), text_input="feesh", font=get_font (75), base_color="#d7fcd4", hovering_color="White"     

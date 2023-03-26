import pygame

#DEFINE theme | DARK COLOR THEME
BLACK = (0,0,0)
DARK_GRAY= (50,50,50)
GRAY = (100,100,100)
LIGHT_GRAY = (150,150,150)

#DEFINE theme | LIGHT COLOR THEME
WHITE = (255,255,255)
LIGHT_BLUE = (100,149,237)
LIGHT_GREEN = (144,239,144)
YELLOW = (255,255,0)

#USE THESE NAMES ON THE LEFT FOR THE COLOR REFERENCED ON THE RIGHT
BACKGROUND_COLOR = BLACK
TEXT_COLOR = LIGHT_GRAY
BUTTON_COLOR = DARK_GRAY
BUTTON_TEXT_COLOR = WHITE


#SETUP THE GAME
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Best Game Ever!")

#button using the dark color theme
button_rect = pygame.Rect(300,250,200,50)
pygame.draw.rect(screen, DARK_GRAY, button_rect)
font = pygame.font.Font(None, 36)
button_text = font.render("Click me!", True, LIGHT_GRAY)
text_rect = button_text.get_rect(center=button_rect.center)
screen.blit(button_text, text_rect)

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()
    
    
pygame.quit()

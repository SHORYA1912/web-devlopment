import pygame,random
pygame.init()

win = pygame.display.set_mode((500,500))
font = pygame.font.sysfont.font("none",36)
choice = ["rock","paper","scissors"]
player_comp = result = ""
show_try_again = False
def text(t,x,y):win.blit(font.render(t,True,(0,0,0)),(x,y))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            run = False
        elif event.type == pygame.KEYDOWN:
        elif event.key == pygame.K_r:
            player = "rock"
        elif event.key == pygame.K_p:
            player = "paper"
        elif event.key == pygame.K_s:
            player = "scissors"
        if player:        
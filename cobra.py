import pygame
from pygame.locals import*
import random


yellow = (255, 255, 102)
window_size = (600,600)
pixel_size = 10
tamanho_cobra = 1


def colisoes(pos1, pos2):
    return pos1 == pos2

def limiteParede(pos):
    if 0 <= pos[0] < window_size[0] and 0 <= pos[1] < window_size[1]:
        return False
    else:
        return True
    
def random_maca():
    x = random.randint(0, window_size[0])
    y = random.randint(0, window_size[1])
    return x // pixel_size * pixel_size, y // pixel_size * pixel_size



pygame.init()
tela = pygame.display.set_mode((window_size))
pygame.display.set_caption("Snake")

cobra_pos = [(250,50),( 260, 50),(270, 50)]
cobra_surface = pygame.Surface((pixel_size, pixel_size))
cobra_surface.fill((255,255,255)) 
cobra_direcao = K_LEFT


maca_surface = pygame.Surface((pixel_size, pixel_size))
maca_surface.fill((255,0,0))
maca_pos = random_maca()


def reinicia():
    global cobra_pos
    global maca_pos
    global cobra_direcao
    cobra_pos = [(250, 50),(260,50),(270,50)]
    cobra_direcao = K_LEFT
    maca_pos = random_maca()
    
while True: 

    pygame.time.Clock().tick(15)
    tela.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit()
            quit()
        
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_LEFT, K_RIGHT, K_DOWN]:
                cobra_direcao = event.key
    
    tela.blit(maca_surface, maca_pos)
    
    
    if colisoes(maca_pos, cobra_pos[0]):
        cobra_pos.append((-10,-10))
        maca_pos = random_maca()
        
    
    for pos in cobra_pos:
        tela.blit(cobra_surface, pos)
        
    
    
    for i in range(len(cobra_pos) -1,0,-1):
        if colisoes(cobra_pos[0], cobra_pos[i]):
            reinicia()
        cobra_pos[i] = cobra_pos[i-1]
        
    if limiteParede(cobra_pos[0]):
        reinicia()
    
    if cobra_direcao == K_UP:
        cobra_pos[0] = (cobra_pos[0][0], cobra_pos[0][1] - pixel_size)
    
    if cobra_direcao == K_DOWN:
        cobra_pos[0] = (cobra_pos[0][0], cobra_pos[0][1] + pixel_size)
        
    if cobra_direcao == K_LEFT:
        cobra_pos[0] = (cobra_pos[0][0] - pixel_size, cobra_pos[0][1])
        
    if cobra_direcao == K_RIGHT:
        cobra_pos[0] = (cobra_pos[0][0] + pixel_size, cobra_pos[0][1] )
    pygame.display.update()
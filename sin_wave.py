import sys,pygame,math
from pygame.locals import *

window_size = (640,480)
amplitude = 100 #quantidade de pixels que a onda pode "subir" ou "descer"
window_center = [int(window_size[0]/2),int(window_size[1]/2)]

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Sine Wave")

font = pygame.font.Font('freesansbold.ttf',16) #fonte padrao do pygame

showSine = False
xPos = 0
step = 0 #entrada da função seno(x)
sinPos = [] #lista para dados da posição do seno

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                showSine=True
        
        
    #desenha linha do meio e linhas da amplitude maxima e minima
    pygame.draw.line(screen,(0,0,0),(0,window_center[1]),(window_size[0],window_center[1]))
    pygame.draw.line(screen,(0,0,0),(0,window_center[1]+amplitude),(window_size[0],window_center[1]+amplitude))#linha de baixo
    pygame.draw.line(screen,(0,0,0),(0,window_center[1]-amplitude),(window_size[0],window_center[1]-amplitude))

    #determinar a posição de y no grafico(-100,0,100)
    yPos = -1 * math.sin(step)*amplitude
    sinPos.append((int(xPos),int(yPos)+window_center[1])) #somamos o centro da janela em y para dizer ao grafico se manter no meio da tela
    if showSine:
        pygame.draw.circle(screen,(255,0,0),(int(xPos),int(yPos)+window_center[1]),10)
        for x,y in sinPos:
            pygame.draw.circle(screen,(255,0,0),(x,y),4)
        xPos+=0.5
        if xPos>window_size[0]:
            xPos=0
            sinPos = []
            step = 0
        else:
            step+=0.08
            step%=2*math.pi


    pygame.display.update()
    clock.tick(60)

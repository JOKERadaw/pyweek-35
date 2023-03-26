import pygame
screensize = [1200, 800]
pygame.init()
screen = pygame.display.set_mode(screensize,pygame.RESIZABLE)
pygame.display.set_caption('HIVE')
clock = pygame.time.Clock()
lastpressed=True
zoom=1
a, b = pygame.mouse.get_pos()
nowcor=[0,0]
jesus=[0,0]
point=[0,0]
reference=[0,0]
def drawmap(x,y):
    pygame.draw.polygon(screen, (255,0,0), [[x+(0-point[0])*zoom**2,y+(100-point[1])*zoom**2],[x+(200-point[0])*zoom**2,y+(200-point[1])*zoom**2],[x+(200-point[0])*zoom**2,y+(100-point[1])*zoom**2]])
    reference[0] = x - point[0] * zoom ** 2
    reference[1] = y - point[1] * zoom ** 2
while True:
    screen.fill([0,0,0])
    drawmap(a,b)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==4 or event.button==5:
                a, b = pygame.mouse.get_pos()
                god= pygame.mouse.get_pos()
                point[0] +=(god[0]-jesus[0])/zoom**2
                point[1] += (god[1]-jesus[1])/zoom**2
                if event.button == 4:
                    zoom *= 1.08
                if event.button == 5:
                    zoom /= 1.08
                jesus = god
        elif event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.VIDEORESIZE:
            screensize = event.size
    if pygame.mouse.get_pressed()[2] or pygame.mouse.get_pressed()[1] :
        if lastpressed:
            buffer= pygame.mouse.get_pos()
            point[0] -=(buffer[0]-totmove[0])/zoom**2
            point[1]-=(buffer[1]-totmove[1])/zoom**2
            totmove=buffer
        else:
            totmove = pygame.mouse.get_pos()
            lastpressed=True
    else:
        lastpressed=False
    pygame.display.update()
    clock.tick(30)
pygame.quit()

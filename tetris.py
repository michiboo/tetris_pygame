import sys, pygame, random

def collison(rect1,rect2):
    if rect1.colliderect(rect2):
        return True
    return False

#setup

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

pygame.init()
size = width, height = 320, 640
screen = pygame.display.set_mode(size)
background = pygame.Surface(screen.get_size())
background.fill( (0,0,0))
block_size = 30
color = (255, 0, 255)
for y in range(height):
    for x in range(width):
        rect = pygame.Rect(x*(block_size+1), y*(block_size+1), block_size, block_size)
        pygame.draw.rect(background, color, rect)
num_block = 1
block = [pygame.draw.rect(screen, (0, 0, 128), (0, 0, block_size, block_size)) for i in range(num_block)]
clock= pygame.time.Clock()
FPS =30
playtime = 0.0
curr = 0
score = 0
r1,r2 = 1,1
while 1:
    milliseconds = clock.tick(FPS)
    playtime += milliseconds/ 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pressed_keys = pygame.key.get_pressed()
    
    
    

    if pressed_keys[pygame.K_LEFT]:
        
        if block[curr].x > 0 and not any([collison(block[curr], block[i]) for i in range(num_block) if i != curr ]):
            block[curr].move_ip(-10,0)
    if pressed_keys[pygame.K_RIGHT]:
        if block[curr].x < width - block_size*r1 and not any([collison(block[curr], block[i]) for i in range(num_block) if i != curr ]):
            block[curr].move_ip(10,0)
    if int(milliseconds/1000)%1 ==0 and block[curr].y < 620:
        block[curr].move_ip(0,10)
        
    text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
    
    

    if block[curr].y >= height-block_size*r2 or any([collison(block[curr], block[i]) for i in range(num_block) if i != curr ]):
        num_block += 1
        r1,r2 = random.randint(1,5), random.randint(1,5)
        block.append(pygame.draw.rect(screen, (0, 0, 128), (0, 0, block_size * r1, block_size* r2)))
        curr += 1
        score = score + r1 + r2
        
    
    
    pygame.display.set_caption(text)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    for i in range(num_block): 
        pygame.draw.rect(screen, (0, 0, 0), block[i])
    
    textsurface = myfont.render(f'Score {score}', False, (255, 255, 255))
    screen.blit(textsurface,(100,100))
    pygame.display.update()
    if block[curr].y == 0 and any([collison(block[curr], block[i]) for i in range(num_block) if i != curr ]):
            sys.exit()



    
import pygame

import random

width = 400
height = 500
back = (255, 255, 255)
mw = pygame.display.set_mode((width,height))
mw.fill(back)
clock = pygame.time.Clock()
pygame.init()
background = "white"
BLACK = (0, 0, 0)
GRAY = (211, 211, 211)
player = pygame.transform.scale(pygame.image.load("kotik.png"), (90, 70))
fps = 40
score = 0
high_score = 0
game_over = False

class Area():
    def __init__(self, x = 0, y = 0, width = 10, height = 10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color,  self.rect)
    def outline(self, frame_color, thickness):
        pygame.draw.rect(mw, frame_color, self.rect, thickness)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x,y)
    
class Label(Area):
    def set_text(self, text, fsize = 16, text_color = (0,0,0)):
        font = pygame.font.SysFont("verdana",fsize).render(text, True, text_color)
    def draw(self, shift_x, shift_y):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

player_x = 170
player_y = 400
platforms = [[175, 480, 70, 10], [85, 370, 70, 10], [260, 379, 70, 10], [175, 260, 70, 10], [85, 150, 70, 10], [260, 150, 70, 10], [175, 40, 70, 10]]
jump = False
y_change = 0
x_change = 0
player_speed = 5
score_last = 0
super_jumps = 2
jump_last = 0



pygame.display.set_caption("Kitty Jumper")

def check_collisions(rect_list, j):
    global player_x
    global player_y
    global y_change
    for i in range(len(rect_list)):
        if rect_list[i].colliderect([player_x + 20, player_y + 60, 35, 5]) and jump == False and y_change > 0:
            j = True
    return j


#прижок

def update_player(y_pos):
    global jump
    global y_change
    jump_height = 10
    gravity = .3
    if jump:
        y_change = -jump_height
        jump = False
    y_pos += y_change
    y_change += gravity
    return y_pos

#платформи та їх зміна

def update_platforms(my_list, y_pos, change):
    global score 
    if y_pos < 250 and change < 0:
        for i in range(len(my_list)):
            my_list[i][1] -= change
    else:
        pass
    for item in range(len(my_list)):
        if my_list[item][1] > 500:
            my_list[item] = [random.randint(10, 320), random.randint(-50, -10), 70, 10]
            score += 1
    return my_list

running = True
while running == True:
    clock.tick(fps)
    mw.fill(background)
    mw.blit(player, (player_x, player_y))
    blocks = []
    score_text = pygame.font.SysFont("Arial", 20).render("High Score:" + str(high_score), True, BLACK, background)
    mw.blit(score_text, (200, 0))
    high_score_text = pygame.font.SysFont("Arial", 20).render("Score:" + str(score), True, BLACK, background)
    mw.blit(high_score_text, (320, 20))

    score_text = pygame.font.SysFont("Arial", 20).render("Air Jumps (Пробіл) :" + str(super_jumps), True, BLACK, background)
    mw.blit(score_text, (10, 10))
    if game_over:
        game_over_text = pygame.font.SysFont("Arial", 20).render("Game Over: Пробіл щоб перезапустити" + str(score), True, BLACK, background)
        mw.blit(game_over_text, (80, 80))

    for i in range(len(platforms)):
        block = pygame.draw.rect(mw, BLACK, platforms[i], 0, 3)
        blocks.append(block)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                game_over = False
                score = 0
                player_x = 170
                player_y = 400
                background = "white"
                score_last = 0
                super_jumps = 2
                jump_last = 0
                platforms = [(175, 480, 70, 10), (85, 370, 70, 10), (260, 379, 70, 10), (175, 260, 70, 10), (85, 150, 70, 10), (260, 150, 70, 10), (175, 40, 70, 10)]
            #cупер-прижки
            if event.key == pygame.K_SPACE and not game_over and super_jumps > 0:
                super_jumps -= 1
                y_change = -15
            if event.key == pygame.K_a:
                x_change = -player_speed
            if event.key == pygame.K_d:
                x_change = player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                x_change = 0
            if event.key == pygame.K_d:
                x_change = 0
        
    if player_y < 460:
        player_y = update_player(player_y)
    else:
        game_over = True
        y_change = 0
        x_change = 0

    player_x += x_change
    jump = check_collisions(blocks, jump)
    pygame.display.update()
    #до платформ
    platforms = update_platforms(platforms, player_y, y_change)

    if player_x < -20:
        player_x = -20
    elif player_x == 330:
        player_x = 330

    if x_change > 0:
        player = pygame.transform.scale(pygame.image.load("kotik.png"), (90, 70))
    elif x_change < 0:
        player = pygame.transform.flip(pygame.transform.scale(pygame.image.load("kotik.png"), (90, 70)), 1, 0)
    
    clock.tick(40)

    if score > high_score:
        high_score = score

    if score - score_last > 15:
        score_last = score
        background = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    
    if score - jump_last > 50:
        jump_last = score
        super_jumps += 1

    pygame.display.flip()
pygame.quit()

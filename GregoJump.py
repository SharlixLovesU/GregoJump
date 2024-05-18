import pygame

back = (255, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()

pygame.init()

background = "white"
BLACK = (0, 0, 0)
GRAY = (211, 211, 211)
width = 400
height = 500

player = pygame.transform.scale(pygame.image.load("kotik.png"), (90, 70))

fps = 40

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
platforms = [(175, 480, 70, 10)]
jump = False
y_change = 0
x_change = 0
player_speed = 3

screen = pygame.display_set_mode(width, height)
pygame.display.set_caption("Kitty Jumper")

def check_collisions(rect_list, j):
    global player_x
    global player_y
    global y_change
    for i in range(len(rect_list)):
        if rect_list[i].colliderect([player_x, player_y + 60, 90, 5]) and jump == False and y_change > 0:
            j = True
    return j


def update_player(y_pos):
    global jump
    global y_change
    jump_height = 10
    gravity = .4
    if jump:
        y_change = -jump_height
        jump = False
    y_pos += y_change
    y_change += gravity
    return y_pos

running = True
while running == True:
    clock.tick(fps)
    mw.fill(background)
    screen.fill(background)
    screen.blit(player, (player_x, player_y))
    blocks = []

    for i in range(len(platforms)):
        block = pygame.draw.rect(screen, BLACK, platforms[i], 1, 2)
        blocks.append(block)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = -player_speed
            if event.key == pygame.K_d:
                x_change = player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                x_change = 0
            if event.key == pygame.K_d:
                x_change = 0
        

    player_y = update_player(player_y)
    player_x += x_change
    jump = check_collisions(blocks, jump)
    pygame.display.update()
    clock.tick(40)

    pygame.display.flip()
pygame.quit()


    
    

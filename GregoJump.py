import pygame

back = (255, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (211, 211, 211)
width = 400
height = 500

player = pygame.image.load("kotik.png")

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


pygame.display.set_caption("Kitty Jumper")

running = True
while running == True:
    clock.tick(fps)
    mw.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()
    clock.tick(40)

    
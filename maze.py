from pygame import *
mixer.init()
font.init()
font = font.SysFont ('Arial', 70)
win = font.render('YOU WIN', True, (0, 255, 0))
lose = font.render('YOU LOSE', True, (255,0,0))

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (55, 55))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Enemy(Gamesprite):
  def update(self):
    if self.rect.x <= 450:
        self.derection = 'right'
    if self.rect.x >= 620:
        self.derection = 'left'

    if self.derection == 'right':
        self.rect.x += self.speed
    else:
        self.rect.x -= self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.image = Surface((wall_width, wall_height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, self.rect)

win_height = 500
win_width = 700

window = display.set_mode((win_width, win_height))
display.set_caption('Лабиринт')
mixer.music.load('jungles.ogg')
money = mixer.Sound("money.ogg")
kick = mixer.Sound("kick.ogg")

background = transform.scale(image.load("background.jpg"), (win_width, win_height))

player = Player("hero.png", 4, win_height - 80,4)
monster = Enemy("cyborg.png", win_width - 80, 280, 2)
final = Gamesprite("treasure.png", 620, 400, 0)
w1 = Wall(150,200,50,100,20,550,10)
w2 = Wall(150,200,50,90,20,10,400)
w3 = Wall(150,200,50,170,120,10,400)
w4 = Wall(150,200,50,250,20,10,400)
w5 = Wall(150,200,50,250,420,270,10)
w6 = Wall(150,200,50,600,120,10,400)
w7 = Wall(150,200,50,510,220,10,200)
w8 = Wall(150,200,50,340,120,260,10)
w9 = Wall(150,200,50,430,120,10,200)
w10 = Wall(150,200,50,340,220,10,200)

finish = False
game = True
clock = time.Clock()
fps = 60
mixer.music.play()

while game :
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0,0))
        player.reset()
        monster.reset()
        player.update()
        monster.update()
        final.reset()
        final.update()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9) or sprite.collide_rect(player, w10):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()
    display.update()
    time.delay(20)
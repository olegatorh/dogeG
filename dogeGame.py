import pygame
import random

x = 300
y = 300
fps = 60
black = 0, 0, 0  # colors
width = 1000
height = 800
hp_minus = False
white = 0, 0, 0

pygame.init()
clock = pygame.time.Clock()
clock.tick(fps)  # game tickrate
screen = pygame.display.set_mode((width, height))  # window size


def hit(player):
    """ This function takes away health if the cat
        touches with the dog """
    global hp_minus
    e_x, e_y = dog.radius()
    e_x1, e_y1 = dog2.radius()
    e_x2, e_y2 = dog3.radius()
    e_x3, e_y3 = dog4.radius()
    p_x, p_y = player.x, player.y
    if p_x in e_x and p_y in e_y or p_x in e_x1 and p_y in e_y1 \
            or p_x in e_x2 and p_y in e_y2 or p_x in e_x3 and p_y in e_y3:
        hp_minus = True
    elif hp_minus:
        player.hp -= 1
        hp_minus = False


def take_health_point(player, heal):
    """ This function give cat healpoint if you take heart"""
    h_x, h_y = heal.radius()
    p_x, p_y = player.x, player.y
    if p_x in h_x and p_y in h_y:
        health4.x = 9000
        player.hp += 1


def load_hearth():
    """ This function load images"""
    return pygame.image.load('images/health1.png')


def spawn_health(hp):
    """ This function spawn hearths"""
    k = [n * 30 for n in range(1, hp + 1)]
    for i in k:
        screen.blit(load_hearth(), [i, 15])


def draw_text(surf, text, size, x, y):
    """ This function draw text """
    font_name = pygame.font.match_font('anti-aliased')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def player_score():
    """ This function draw score"""
    mytime = pygame.time.get_ticks()
    score = mytime // 1000
    draw_text(screen, str(score), 50, width - 20, 10)
    return str(score)


def stop_score():
    stop_scor = "Your score: " + player_score()
    return str(stop_scor)


def pause():
    """This function paused game"""
    pauss = True
    while pauss:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(BackGround.image, BackGround.rect)
        draw_text(screen, "you loss", 80, 500, 400)
        draw_text(screen, stop_score(), 90, 500, 700)
        draw_text(screen, "press - ESCAPE, TO LEAVE THE GAME", 50, 500, 100)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pauss = False
        elif keys[pygame.K_ESCAPE]:
            quit()


class Player:
    def __init__(self, name, picture, x, y):
        self.y = y
        self.x = x
        self.hp = 3
        self.picture = picture
        self.name = name
        self.name = pygame.image.load(self.picture)
        self.name.set_colorkey(black)

    def place(self):
        """ This function spawn object on screen"""
        return screen.blit(self.name, [self.x, self.y])

    def player_move(self):
        """ This function allows the cat to move"""
        if event.key == pygame.K_LEFT and self.x > 5:
            self.x -= 20
        elif event.key == pygame.K_RIGHT and self.x <= width - 60:
            self.x += 20
        elif event.key == pygame.K_UP and self.y > 0:
            self.y -= 20
        elif event.key == pygame.K_DOWN and self.y < height - 40:
            self.y += 20
        return self.x, self.y

    def radius(self):
        """ This function give back list of (x, y) for easy taking heart """
        x, y = self.x, self.y
        radius_x = list(range(x - 15, x + 15))
        radius_y = list(range(y - 15, y + 15))
        return radius_x, radius_y


class Enemy:
    def __init__(self, name, picture, x, y):
        self.x = x
        self.y = y
        self.picture = picture
        self.name = name
        self.name = pygame.image.load(self.picture)
        self.rect = self.name.get_rect()
        self.name.set_colorkey(black)
        self.speedy = [random.randint(2, 9), random.randint(3, 9)]

    def en_move(self):
        """ This function control the speed """
        self.rect = self.rect.move(self.speedy)
        if self.rect.left < 0 or self.rect.right > width:
            self.speedy[0] = -self.speedy[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speedy[1] = -self.speedy[1]
            return self.speedy[0], self.speedy[1]

    def en_place(self):
        """ This function spawn object on screen """
        screen.blit(self.name, self.rect)
        return

    def place(self):
        """ This function give back x, y of object """
        return screen.blit(self.name, [self.x, self.y])

    def radius(self):
        """ This function give back list of (x, y) for easy touch dog """
        x, y = self.rect[0], self.rect[1]
        radius_x = list(range(x - 45, x + 45))
        radius_y = list(range(y - 45, y + 45))
        return radius_x, radius_y


class Background(pygame.sprite.Sprite):

    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Music:
    def __init__(self, name):
        self.name = name

    def game_music(self):
        """ This function play song"""
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.load(self.name)
        pygame.mixer.music.play(-1)


BackGround = Background('images/back.jpg', [0, 0])
mus = Music("gameSong.mp3")
cat = Player('cat', 'images/cat.png', 300, 300)
dog = Enemy('garry', 'images/dog1.png', 0, 1000)
dog2 = Enemy('walter', 'images/dog2.png', 900, 900)
dog3 = Enemy('ben', 'images/dog3.png', random.randrange(width - 100),
             random.randrange(height - 100))
dog4 = Enemy('ros', 'images/dog4.png', random.randrange(width - 50),
             random.randrange(height - 50))
health1 = Player('health1', 'images/health1.png', 15, 15)
health4 = Player('+HealthPoint', 'images/health1.png',
                 random.randrange(width - 100), random.randrange(height - 100))
mus.game_music()
while 1:
    player_score()
    cat.place()
    dog.en_place()
    dog2.en_place()
    dog3.en_place()
    dog4.en_place()

    spawn_health(cat.hp)
    health4.place()
    dog.en_move()
    dog2.en_move()
    dog3.en_move()
    dog4.en_move()
    hit(cat)
    take_health_point(cat, health4)
    if cat.hp == 0:
        pause()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.KEYUP:
            cat.player_move()
    pygame.display.flip()
    screen.fill(white)
    screen.blit(BackGround.image, BackGround.rect)

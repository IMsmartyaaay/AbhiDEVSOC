import pygame, sys
import random

pygame.mixer.init()
pygame.mixer.music.load("gamemusic.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)


colors = [
    (255, 105, 180),  # pink
    (255, 0, 0),      # red
    (0, 0, 255),      # blue
    (0, 255, 0),      # green
    (255, 255, 0)     # yellow
]
ball_color = random.choice(colors)

def ballanimation():
    global ball_speedx, ball_speedy, player_score, opponent_score, game_active
    if ball.top <= 0 or ball.bottom >= h:
        ball_speedy = -ball_speedy

    if ball.left <= 0:
        player_score += 1
        ball_restart()
    if ball.right >= w:
        opponent_score += 1
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speedx = -ball_speedx
        global ball_color
        ball_color = random.choice(colors)  # change ball color randomly


def ball_restart():
    global ball_speedx, ball_speedy
    ball.center = (w / 2, h / 2)
    ball_speedy *= random.choice((1, -1))
    ball_speedx *= random.choice((1, -1))

def draw_text(text, size, color, x, y, center=True):
    font = pygame.font.Font(None, size)
    render = font.render(text, True, color)
    rect = render.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(render, rect)

pygame.init()
clock = pygame.time.Clock()

w = 1000
h = 700
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('TT Pong')

ball = pygame.Rect(w / 2 - 15, h / 2 - 15, 30, 30)
player = pygame.Rect(w - 20, h / 2 - 70, 10, 140)
opponent = pygame.Rect(10, h / 2 - 70, 10, 140)
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)
button_color = (180, 180, 180)
dark_grey = (40, 40, 40)
pink = (255, 182, 193)
blue = (0, 0, 255)

ball_speedx = 8
ball_speedy = 8
player_speed = 0
opponent_speed = 0
player_score = 0
opponent_score = 0
game_active = True

restart_button = pygame.Rect(w / 2 - 75, h / 2 + 60, 150, 60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed = 8
                if event.key == pygame.K_UP:
                    player_speed = -8
                if event.key == pygame.K_s:
                    opponent_speed = 8
                if event.key == pygame.K_w:
                    opponent_speed = -8

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_DOWN, pygame.K_UP):
                    player_speed = 0
                if event.key in (pygame.K_w, pygame.K_s):
                    opponent_speed = 0
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    player_score = 0
                    opponent_score = 0
                    ball_restart()
                    game_active = True

    if game_active:
        ballanimation()
        ball.x += ball_speedx
        ball.y += ball_speedy
        player.y += player_speed
        opponent.y += opponent_speed

        if player.top <= 0:
            player.top = 0
        if player.bottom >= h:
            player.bottom = h
        if opponent.top <= 0:
            opponent.top = 0
        if opponent.bottom >= h:
            opponent.bottom = h

        if player_score >= 11 or opponent_score >= 11:
            game_active = False

        screen.fill(bg_color)
        pygame.draw.aaline(screen, light_grey, (w / 2, 0), (w / 2, h))
        pygame.draw.ellipse(screen, ball_color, ball)
        pygame.draw.rect(screen, light_grey, player)
        pygame.draw.rect(screen, light_grey, opponent)
        draw_text(f"{opponent_score}", 74, light_grey, w / 2 - 100, 50)
        draw_text(f"{player_score}", 74, light_grey, w / 2 + 100, 50)

    else:
        # Game Over Screen
        screen.fill(pink)
        draw_text("GAME OVER", 120, blue, w / 2, h / 2 - 100)
        pygame.draw.rect(screen, button_color, restart_button, border_radius=8)
        draw_text("Restart", 48, dark_grey, restart_button.centerx, restart_button.centery)

    pygame.display.flip()
    clock.tick(60)


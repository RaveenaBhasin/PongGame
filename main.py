import pygame
import random

pygame.mixer.init()
pygame.init()

#Creating window
screen_x = 700
screen_y = 500
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("PONG GAME")
icon= pygame.image.load('icon.png')
pygame.display.set_icon(icon)
welcome_image= pygame.image.load("Untitled 1 (3).png")
clock= pygame.time.Clock()

bg_color= (157, 241, 250)
font = pygame.font.SysFont(None,45)
font_1 = pygame.font.SysFont(None,35)
text_font=pygame.font.Font(None,80)

def font_screen(text,color, x, y):
    pong_text = font.render(text, True, color)
    screen.blit(pong_text, [x,y])

def font_screen_1(text,color,x,y):
    enter_text = font_1.render(text,True,color)
    screen.blit(enter_text, [x,y])

def welcome_screen():
    exit_game= False
    while not exit_game:
        screen.blit(welcome_image, [0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    loop()
        pygame.display.update()
        clock.tick(60)

#Creating ball
ball_x = screen_x/2-15
ball_y = screen_y/2-15
ball = pygame.Rect(ball_x,ball_y, 25, 25)

def ball_restart(ball_velocity_x,ball_velocity_y):
    ball.center= (screen_x/2,screen_y/2)
    ball_velocity_x *= random.choice((1,-1))
    ball_velocity_y *= random.choice((1,-1))

#Creating game loop
def loop():
    player1_score = 0
    player2_score = 0
    player1_velocity = 0
    player1 = pygame.Rect(5, screen_y / 2 - 70, 8, 130)
    player2_velocity= 0
    player2 = pygame.Rect(screen_x - 12, screen_y/2-70, 8, 130)

    ball_velocity_x= 4*random.choice((1,-1))
    ball_velocity_y= 4*random.choice((1,-1))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    loop()
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_PAUSE:
                    ball_velocity_x=0
                    ball_velocity_y=0
                if event.key == pygame.K_UP:
                    player1.y = player1.y-90

                if event.key == pygame.K_DOWN:
                    player1.y= player1.y+90

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        player2.y = player2.y-90
                    if event.key == pygame.K_s:
                        player2.y = player2.y+90

        player1.y = player1.y + player1_velocity
        if player1.y < ball.y:
            player1.top += player1_velocity
        if player2.bottom > ball.y:
            player1.bottom -= player1_velocity
        if player1.top <= 0 :
            player1.top = 0
        if player1.bottom >= screen_y:
            player1.bottom = screen_y

        player2.y = player2.y + player2_velocity
        if player2.top <= 0:
            player2.top = 0
        if player2.bottom >= screen_y:
            player2.bottom = screen_y

        ball.x = ball.x + ball_velocity_x
        ball.y = ball.y + ball_velocity_y

        if ball.left <= 0 :
            player2_score += 1
            ball_restart(ball_velocity_x, ball_velocity_y)
        if ball.right >= screen_x:
            player1_score += 1
            ball_restart(ball_velocity_x,ball_velocity_y)

        if ball.top <= 0 or ball.bottom >= screen_y:
            pygame.mixer.music.load("BOUNCE+1.mp3")
            pygame.mixer.music.play()
            ball_velocity_y = ball_velocity_y*-1

        if ball.colliderect(player1) or ball.colliderect(player2):
            pygame.mixer.music.load("BOUNCE+1.mp3")
            pygame.mixer.music.play()
            ball_velocity_x = ball_velocity_x*-1

        screen.fill(bg_color)
        pygame.draw.ellipse(screen, pygame.Color('black'), ball)
        pygame.draw.rect(screen, pygame.Color('black'), player1)
        pygame.draw.rect(screen, pygame.Color('black'), player2)
        pygame.draw.aaline(screen, pygame.Color('black'), (screen_x/2, 0), (screen_x/2, screen_y))

        score_text = text_font.render(f"{player1_score}", True, pygame.Color('black'))
        screen.blit(score_text, (165, 10))
        score_text = text_font.render(f"{player2_score}", True, pygame.Color('black'))
        screen.blit(score_text, (520, 10))
        if player1_score == 10:
            ball_velocity_x = 0
            ball_velocity_y = 0
            font_screen("PLAYER 1 WON", pygame.Color('black'), 68, 200)
            font_screen_1("Play Again!!Press P", pygame.Color('black'), 68, 250)
        if player2_score == 10:
            ball_velocity_x = 0
            ball_velocity_y = 0
            font_screen("PLAYER 2 WON", pygame.Color('black'), 395, 200)
            font_screen_1("Play Again!!Press P", pygame.Color('black'), 395, 250)

        pygame.display.update()
        clock.tick(75)
    pygame.quit()
    quit()
welcome_screen()


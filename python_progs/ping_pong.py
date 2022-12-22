# Import the necessary modules
import pygame
import sys

# Initialize pygame
pygame.init()

# Set the window size
WIDTH = 800
HEIGHT = 600

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption("Ping Pong")

# Set the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set the player properties
player_width = 15
player_height = 60
player_velocity = 5

# Set the ball properties
ball_radius = 10
ball_velocity_x = 5
ball_velocity_y = 5

# Set the player positions
player1_x = 20
player2_x = WIDTH - 20 - player_width
player1_y = (HEIGHT - player_height) / 2
player2_y = (HEIGHT - player_height) / 2

# Set the ball position
ball_x = WIDTH / 2
ball_y = HEIGHT / 2

# Set the font
font = pygame.font.Font(None, 36)

# Set the score
player1_score = 0
player2_score = 0

# Create the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the player positions
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_y -= player_velocity
    if keys[pygame.K_s]:
        player1_y += player_velocity
    if keys[pygame.K_UP]:
        player2_y -= player_velocity
    if keys[pygame.K_DOWN]:
        player2_y += player_velocity

    # Make sure the player stays within the screen
    if player1_y < 0:
        player1_y = 0
    if player1_y > HEIGHT - player_height:
        player1_y = HEIGHT - player_height
    if player2_y < 0:
        player2_y = 0
    if player2_y > HEIGHT - player_height:
        player2_y = HEIGHT - player_height

    # Update the ball position
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Check if the ball has hit the top or bottom of the screen
    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
        ball_velocity_y *= -1

    # Check if the ball has hit player 1
    if ball_x - ball_radius < player1_x + player_width and ball_y > player1_y and ball_y < player1_y + player_height:
        ball_velocity_x *= -1
    # Check if the ball has scored on player 1
    elif ball_x < 0:
        player2_score += 1
        ball_x = WIDTH / 2
        ball_y = HEIGHT / 2

    # Check if the ball has hit player 2
    if ball_x + ball_radius > player2_x and ball_y > player2_y and ball_y < player2_y + player_height:
        ball_velocity_x *= -1
    # Check if the ball has scored on player 2
    elif ball_x > WIDTH:
        player1_score += 1
        ball_x = WIDTH / 2
        ball_y = HEIGHT / 2

    # Draw the players
    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, player_width, player_height))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y, player_width, player_height))

    # Draw the ball
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), ball_radius)

    # Draw the scores
    score1 = font.render(str(player1_score), True, WHITE)
    score2 = font.render(str(player2_score), True, WHITE)

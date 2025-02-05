import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer Game")

clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player attributes
player_width = 50
player_height = 50
player_x = 100
player_y = screen_height - player_height - 100
player_speed = 5
jump_speed = -15
gravity = 0.8

# Player state variables
player_vel_y = 0
player_vel_x = 0
player_on_ground = False
acceleration = 0.5
friction = 0.9

# Platforms list: each platform as a rect
platforms = []
platforms.append(pygame.Rect(0, screen_height - 50, screen_width, 50))
platforms.append(pygame.Rect(150, screen_height - 150, 100, 20))
platforms.append(pygame.Rect(300, screen_height - 250, 150, 20))
platforms.append(pygame.Rect(500, screen_height - 350, 100, 20))
platforms.append(pygame.Rect(650, screen_height - 450, 100, 20))  # End level platform

# Enemies list: each enemy as a rect
enemies = []
enemy_speed = 2

# Create an enemy on a platform
enemy = pygame.Rect(300, screen_height - 270, 40, 40)
enemies.append(enemy)

# Load and scale assets for animations based on object dimensions
player_frames = [
    pygame.transform.scale(pygame.image.load("assets/player1.png").convert_alpha(), (player_width, player_height)),
    # pygame.transform.scale(pygame.image.load("assets/player2.png").convert_alpha(), (player_width, player_height)),
    # pygame.transform.scale(pygame.image.load("assets/player3.png").convert_alpha(), (player_width, player_height)),
    # pygame.transform.scale(pygame.image.load("assets/player4.png").convert_alpha(), (player_width, player_height))
]
player_frame_index = 0
player_frame_delay = 5  # frames to wait before switching
player_frame_counter = 0

enemy_image = pygame.transform.scale(pygame.image.load("assets/enemy.png").convert_alpha(), (enemy.width, enemy.height))

win = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_vel_x -= acceleration
    if keys[pygame.K_RIGHT]:
        player_vel_x += acceleration
    if keys[pygame.K_SPACE] and player_on_ground:
        player_vel_y = jump_speed
        player_on_ground = False

    player_vel_x *= friction
    player_x += player_vel_x
    # Horizontal collision detection
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for plat in platforms:
        if player_rect.colliderect(plat):
            if player_vel_x > 0:
                player_x = plat.left - player_width
            elif player_vel_x < 0:
                player_x = plat.right
            player_vel_x = 0
            player_rect.x = player_x

    # Apply gravity and vertical movement
    player_vel_y += gravity
    player_y += player_vel_y
    player_rect.y = player_y
    player_on_ground = False
    for plat in platforms:
        if player_rect.colliderect(plat):
            if player_vel_y > 0:
                player_y = plat.top - player_height
                player_on_ground = True
            elif player_vel_y < 0:
                player_y = plat.bottom
            player_vel_y = 0
            player_rect.y = player_y

    # Improved enemy movement with patrol boundaries
    enemy_boundary_left = 300
    enemy_boundary_right = 450
    enemy.x += enemy_speed
    if enemy.x < enemy_boundary_left or enemy.x > enemy_boundary_right:
        enemy_speed = -enemy_speed
        enemy.x += enemy_speed

    # Check collision with enemy
    for e in enemies:
        if player_rect.colliderect(e):
            # Restart player position on collision
            player_x = 100
            player_y = screen_height - player_height - 100
            player_vel_y = 0
            player_vel_x = 0

    # Check win condition: if player touches the end platform
    if player_rect.colliderect(platforms[-1]):
        win = True

    # Drawing
    screen.fill(BLUE)
    for plat in platforms:
        pygame.draw.rect(screen, GREEN, plat)

    # Update player animation
    player_frame_counter += 1
    if player_frame_counter >= player_frame_delay:
        player_frame_index = (player_frame_index + 1) % len(player_frames)
        player_frame_counter = 0
    player_current = player_frames[player_frame_index]
    screen.blit(player_current, (player_x, player_y))

    # Draw enemy sprite
    screen.blit(enemy_image, (enemy.x, enemy.y))

    # Display win message if won
    if win:
        font = pygame.font.SysFont(None, 55)
        win_text = font.render("You Win!", True, WHITE)
        screen.blit(win_text, ((screen_width - win_text.get_width()) // 2, screen_height // 2))
    
    pygame.display.flip()
    clock.tick(FPS)

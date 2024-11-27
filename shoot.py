# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Constants
# WIDTH, HEIGHT = 800, 600
# FPS = 60
# FRUIT_SIZE = 50
# BULLET_SIZE = 5

# # Colors
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)

# # Set up the display
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Fruit Shooter Game")

# # Load images (you can replace these with your own images)
# fruit_image = pygame.Surface((FRUIT_SIZE, FRUIT_SIZE))
# fruit_image.fill(GREEN)

# # Game variables
# fruits = []
# bullets = []
# score = 0

# # Function to create a new fruit
# def create_fruit():
#     x = random.randint(0, WIDTH - FRUIT_SIZE)
#     fruits.append(pygame.Rect(x, 0, FRUIT_SIZE, FRUIT_SIZE))

# # Main game loop
# running = True
# clock = pygame.time.Clock()
# while running:
#     # Event handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Create fruits
#     if random.randint(1, 30) == 1:  # Adjust the frequency of fruit creation
#         create_fruit()

#     # Move fruits down
#     for fruit in fruits[:]:
#         fruit.y += 5  # Move fruit down
#         if fruit.y > HEIGHT:
#             fruits.remove(fruit)  # Remove fruit if it goes off screen

#     # Shooting bullets
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_SPACE]:  # Shoot bullet when space is pressed
#         bullet = pygame.Rect(WIDTH // 2, HEIGHT - 20, BULLET_SIZE, BULLET_SIZE)
#         bullets.append(bullet)

#     # Move bullets
#     for bullet in bullets[:]:
#         bullet.y -= 10  # Move bullet up
#         if bullet.y < 0:
#             bullets.remove(bullet)  # Remove bullet if it goes off screen

#     # Check for collisions
#     for bullet in bullets[:]:
#         for fruit in fruits[:]:
#             if bullet.colliderect(fruit):
#                 bullets.remove(bullet)
#                 fruits.remove(fruit)
#                 score += 1  # Increase score
#                 break

#     # Drawing
#     screen.fill(WHITE)
#     for fruit in fruits:
#         screen.blit(fruit_image, fruit.topleft)
#     for bullet in bullets:
#         pygame.draw.rect(screen, RED, bullet)

#     # Display score
#     font = pygame.font.Font(None, 36)
#     score_text = font.render(f'Score: {score}', True, (0, 0, 0))
#     screen.blit(score_text, (10, 10))

#     pygame.display.flip()
#     clock.tick(FPS)

# pygame.quit()

#Import necessary libraries
import pygame #Imports the Pygame library, which is used for developing games in python.
import sys #Imports the 'sys' module, which provides access to some variables used or maintained by the interpreter.

#Initialize Pygame
pygame.init() #Initializes the Pygame library. This must be called before using any Pygame functions.

#Constants
WIDTH, HEIGHT = 600, 400 #Defines constants for the dimensions of the window.
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 60 #Defines constants for the dimensions of the paddle.
BALL_SIZE = 15 #Defines constant for the dimension of the ball.
FPS = 60 #Defines frames per second.

#Colors. Defines color constants using RGB values. In Pygame, colors are represented as tuples of three integers:
#(Red, Green, Blue)
WHITE = (255,255,255) 
BLACK = (0,0,0)

#Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #Creates a Pygame window with dimensions specified by 'WIDTH' and 'HEIGHT'
pygame.display.set_caption("Pong") #Sets the window caption to "Pong".

#Clock for controlling the frame rate
clock = pygame.time.Clock() #Creates a Pygame clock object to control the frame rate.

#Paddle positions. Creates rectangles representing the positions and sizes of the player1's and player2's paddles using
#'pygame.Rect
player1_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2_paddle = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

#Ball position and speed
#Creates a rectangle representing the ball and initializes its position and size.
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
#'ball_speed' is a list representing the ball's speed in the x and y directions.
ball_speed = [5,5]

#Main game loop
#Enters the main game loop that will keep running until the game is closed.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Checks for events, such as quitting the game. If the close button is clicked, the game quits.
            pygame.quit()
            sys.exit()
    #Player controls. Checks for pressed keys using 'pygame.key.get_pressed()'
    keys = pygame.key.get_pressed()
    #Adjusts the player1's paddle position based on the pressed keys(up and down arrow keys).
    
    if keys[pygame.K_w] and player1_paddle.top > 0:
        player1_paddle.y -= 5
    if keys[pygame.K_s] and player1_paddle.bottom < HEIGHT:
        player1_paddle.y += 5
    #Adjusts the player2's paddle position based on the pressed keys(up and down arrow keys).
    if keys[pygame.K_UP] and player2_paddle.top > 0:
        player2_paddle.y -= 5
    if keys[pygame.K_DOWN] and player2_paddle.bottom < HEIGHT:
        player2_paddle.y += 5
   
   
    
    #Move the ball. Updates the ball's position based on its speed.
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]
    #Ball collisions with walls. Checks if the ball hits the top or bottom walls and reverses its vertical directions if so.
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]
    #Ball collisions with paddles. Checks if the ball collides with either the player1's or player2's paddle and
    #reverses its horizontal direction if so.
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_speed[0] = -ball_speed[0]
    #Ball out of bounds. Checks if the ball goes out of bounds on the left or right and resets its position if so.
    if ball.left <= 0 or ball.right >= WIDTH:
        #Reset ball position.
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
    #Draw everything. Clears the screen and draws the player1's paddle, player2's paddle, and the ball on the screen.
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1_paddle)
    pygame.draw.rect(screen, WHITE, player2_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    #Updates the display with the drawn elements.
    pygame.display.flip()
    
    #Cap the frame rate. Limits the fram rate to 'FPS' frames per second.
    clock.tick(FPS)
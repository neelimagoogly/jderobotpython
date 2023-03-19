import pygame
import numpy as np
import random

# Define the size of the arena and the robot
arena_size = 500
robot_radius = 10

# Define the initial position of the robot
robot_position = np.array([arena_size/2, arena_size/2])

# Define the initial direction of the robot as a random angle
robot_direction = random.uniform(0, 360)

# Define the speed of the robot in pixels per time step
robot_speed = 5

# Define the time step of the simulation in milliseconds
time_step = 10

# Define the duration of rotation in milliseconds when the robot collides with the boundary
rotation_duration = 500

# Define the maximum angle of random deviation in degrees when the robot changes direction
max_deviation_angle = 30

# Initialize Pygame and create a window to display the simulation
pygame.init()
screen = pygame.display.set_mode((arena_size, arena_size))
pygame.display.set_caption("Brownian Motion Simulation")

# Define the colors of the arena and the robot
arena_color = (255, 255, 255)
robot_color = (255, 0, 0)

# Define a function to check if the robot has collided with the boundary of the arena
def check_collision(position):
    if position[0] < robot_radius or position[0] > arena_size - robot_radius:
        return True
    if position[1] < robot_radius or position[1] > arena_size - robot_radius:
        return True
    return False

# Define a function to randomly rotate the robot for a set duration
def rotate_robot():
    global robot_direction
    rotation_direction = random.choice([-1, 1])
    rotation_duration_elapsed = 0
    while rotation_duration_elapsed < rotation_duration:
        pygame.time.delay(time_step)
        rotation_duration_elapsed += time_step
        robot_direction += rotation_direction * 1.0 * time_step / rotation_duration * 360
        robot_direction %= 360

# Define the main loop of the simulation
running = True
while running:
    # Check for events such as quitting the simulation
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the robot in the set direction by the defined speed
    robot_position += np.array([robot_speed * np.cos(np.radians(robot_direction)), 
                                robot_speed * np.sin(np.radians(robot_direction))])

    # Check if the robot has collided with the boundary of the arena
    if check_collision(robot_position):
        rotate_robot()

    # Randomly change the direction of the robot by a small angle
    robot_direction += random.uniform(-max_deviation_angle, max_deviation_angle)

    # Clear the screen and draw the arena and the robot
    screen.fill(arena_color)
    pygame.draw.circle(screen, robot_color, robot_position.astype(int), robot_radius)

    # Update the display and wait for the defined time step
    pygame.display.update()
    pygame.time.delay(time_step)

# Quit Pygame and close the window
pygame.quit()

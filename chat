from microbit import *

def move_forward(blocks):
    # Constants
    wheel_circumference = 17.6  # cm
    block_distance = 23.7  # cm
    counts_per_rotation = 360
    
    # Calculate encoder counts to travel
    counts_to_travel = int((block_distance / wheel_circumference) * counts_per_rotation * blocks)
    
    # Reset encoder counts
    motor_encoder_A = 0
    motor_encoder_B = 0
    
    # Set motor targets
    motor_encoder_target_A = counts_to_travel
    motor_encoder_target_B = counts_to_travel
    
    # Move motors forward
    motor_A = 50
    motor_B = 50
    
    while motor_encoder_A < motor_encoder_target_A and motor_encoder_B < motor_encoder_target_B:
        pass  # Wait until movement is complete
    
    # Stop motors
    motor_A = 0
    motor_B = 0
    sleep(500)  # Pause for stability

def turn_left_90():
    # Constants
    wheel_circumference = 17.6  # cm
    turn_distance = 8.6  # cm
    counts_per_rotation = 360
    
    # Calculate encoder counts
    counts_to_travel = int((turn_distance / wheel_circumference) * counts_per_rotation)
    
    # Reset encoder counts
    motor_encoder_A = 0
    motor_encoder_B = 0
    
    # Set motor targets
    motor_encoder_target_A = counts_to_travel
    motor_encoder_target_B = counts_to_travel
    
    # Set motors for left turn
    motor_A = 50
    motor_B = -50
    
    while motor_encoder_A < motor_encoder_target_A and motor_encoder_B < motor_encoder_target_B:
        pass  # Wait until movement is complete
    
    # Stop motors
    motor_A = 0
    motor_B = 0
    sleep(500)

def turn_right_90():
    # Constants
    wheel_circumference = 17.6  # cm
    turn_distance = 8.6  # cm
    counts_per_rotation = 360
    
    # Calculate encoder counts
    counts_to_travel = int((turn_distance / wheel_circumference) * counts_per_rotation)
    
    # Reset encoder counts
    motor_encoder_A = 0
    motor_encoder_B = 0
    
    # Set motor targets
    motor_encoder_target_A = counts_to_travel
    motor_encoder_target_B = counts_to_travel
    
    # Set motors for right turn
    motor_A = -50
    motor_B = 50
    
    while motor_encoder_A < motor_encoder_target_A and motor_encoder_B < motor_encoder_target_B:
        pass  # Wait until movement is complete
    
    # Stop motors
    motor_A = 0
    motor_B = 0
    sleep(500)

# Example usage
while True:
    if button_a.was_pressed():
        move_forward(1)
    elif button_b.was_pressed():
        turn_left_90()

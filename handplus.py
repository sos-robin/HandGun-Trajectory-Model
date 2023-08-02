import math
import matplotlib.pyplot as plt

def euler_method(x0, y0, v0, angle_deg, target_distance, wind_speed, dt):
    # Constants
    m = 0.008  # Bullet mass (kg)
    g = 9.81   # Acceleration due to gravity (m/s²)
    Cd = 0.3   # Drag coefficient (assumed value, adjust as needed)
    A = 0.0001 # Cross-sectional area (m², assumed value, adjust as needed)
    rho = 1.2  # Air density (kg/m³, standard value)
    
    # Convert angle to radians
    angle_rad = math.radians(angle_deg)
    
    # Initial velocities
    v0x = v0 * math.cos(angle_rad)
    v0y = v0 * math.sin(angle_rad)
    
    # Lists to store positions
    x_values = [x0]
    y_values = [y0]
    
    while y_values[-1] >= 0:
        # Air resistance term
        B = 0.5 * Cd * A * rho
        
        # Update velocities
        v_x = v0x - (B / m) * v0x * dt
        v_y = v0y - (B / m) * v0y * dt - g * dt
        
        # Update wind effect on horizontal motion
        v_x += wind_speed
        
        # Update positions
        x = x_values[-1] + v_x * dt
        y = y_values[-1] + v_y * dt
        
        # Append to lists
        x_values.append(x)
        y_values.append(y)
        
        # Update velocities for the next iteration
        v0x = v_x
        v0y = v_y
        
        # Check if the bullet has reached the peak height
        if v0y < 0:
            # During descent, adjust wind effect to opposite direction
            v_x -= wind_speed
        
    # Calculate the total horizontal distance traveled by the bullet
    total_horizontal_distance = max(x_values) - x0
    
    # Find the maximum height reached by the bullet
    max_height = max(y_values)
    
    # Calculate the vertical distance traveled by the bullet
    vertical_distance = max_height - y0
    
    # Check if the bullet hit the target
    if abs(total_horizontal_distance - target_distance) < 5:  # Consider a hit if within 5 meters
        print("Target hit!")
    else:
        print("Target missed.")
    
    return x_values, y_values, total_horizontal_distance, vertical_distance

# Simulation parameters
initial_x = 0
initial_y = 0
initial_velocity = 300   # m/s
firing_angle = 30 # degrees (adjust as needed)
target_distance = 50  # m
wind_speed = 10  # m/s (adjust as needed)
time_step = 0.001  # seconds

# Run the simulation
x_traj, y_traj, total_distance, vertical_distance = euler_method(initial_x, initial_y, initial_velocity, firing_angle, target_distance, wind_speed, time_step)

# Print the total horizontal distance traveled by the bullet
print(f"Total horizontal distance traveled by the bullet: {total_distance:.2f} meters")
  
# Print the vertical distance traveled by the bullet
print(f"Vertical distance traveled by the bullet: {vertical_distance:.2f} meters")

# Plot the trajectory
plt.plot(x_traj, y_traj)
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.title("Bullet Trajectory with Wind")
plt.axhline(0, color='gray', linestyle='--')  # Ground level
plt.axvline(target_distance, color='red', linestyle='--', label='Target')  # Target distance
plt.legend()
plt.grid(True)
plt.show()

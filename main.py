import math
import numpy as np
import matplotlib.pyplot as plt


# asking the user for the initial speed and angle

v0 = float(input("enter the inital speed in m/s"))
angle_deg = float(input("enter the desired angle of launch in degrees"))
g = 9.8

# IT works, in the terminal, navigate to the folder Projectile_motion, once insde, run python3 main.py and it asks the user for the input








####### DONE DONE DONE DONE DONE DONE SO FAR ################################################

#1. Get Input From the User
#Ask the user to enter the launch speed (in meters/second)

#Ask the user for the launch angle (in degrees)

#2. Convert and Set Up the Math
#Convert angle from degrees to radians (for sin() and cos()) since all programming languages
#cannot work with degrees only radians

angle_rad = math.radians(angle_deg)

#Break initial velocity into horizontal (vx) and vertical (vy) parts

horizontal_velocity = v0 * math.cos(angle_rad)

vertical_velocity = v0 * math.sin(angle_rad)

#Calculate total flight time using basic physics:
#Time to go up = vy / g
#Total flight time = 2 * vy / g (symmetric parabola)

total_flight_time = 2 * vertical_velocity / g

# now to output the result of the calculation for the total flight time

print("Hi!, here is the data you chose for the velocity and angle. Velocity:", v0, "Angle", angle_deg, "your angle in radians", angle_rad, "The total flight time is", total_flight_time)

#📏 3. Calculate the Trajectory Over Time
#Create a time array from 0 to total time (use np.linspace)

time_array = np.linspace(0,total_flight_time, 100)

#For each time step t, calculate:

#Horizontal position: x = vx * t

horizontal_position = horizontal_velocity * time_array

#Vertical position: y = vy * t - 0.5 * g * t²

vertical_position = (vertical_velocity * time_array) - (1/2)*g*(time_array)**2

#now that this is done, make the program output the calculuatino for the trjacetory

print("Also, here are the x and y points for the trajectory over time:", horizontal_position, vertical_position)

print("Here is the max height your object reached:", max(vertical_position))
#4. Plot the Results
#Use matplotlib to plot the x and y arrays”

plt.plot(horizontal_position, vertical_position)
plt.xlabel("Distance in meters")
plt.ylabel("Height in meters")
plt.title("Projectile motion simulation")
plt.grid(True)
plt.show()

#5. Print Useful Stats
#Print max height ///  ALREAY DONE: SEE LINE 74

####### DONE DONE DONE DONE DONE DONE SO FAR ################################################


#Print time of flight

#Print horizontal range (use last value of x)

#6. Optional Finishing Touches

#Add error checking to make sure the user enters valid numbers

"""XY-controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor, Keyboard, Connector
from math import pi, sin, cos

# Classes 

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def changeX(self, x):
        self.x = x
    
    def changeY(self, y):
        self.y = y
    
    
class Queue:
    def __init__(self):
        self.listX = [0.0]
        self.listY = [0.0]
    
    def add(self, positionX, positionY):
        self.listX.append(0.0)
        self.listX.append(positionX)
        self.listY.append(positionY)
        self.listY.append(positionY)
        
    def resetQueue(self):
        self.listX = [0.0]
        self.listY = [0.0]
    

# create the Robot instance.
robot = Robot()

# Create the other class instances
kb = Keyboard()

P1 = Position(0.34, 1.04)
P2 = Position(0.34, 0.50)
P3 = Position(-0.34, 0.50)
P4 = Position(-0.34, 1.04)

queue = Queue()



#Globale variable

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

#Her henter jeg de forskellige devices som er sat på robotten. 
#Husk at sensorer skal aktiveres ved hjælp af .enable() funktionen

sensorX = robot.getDevice("X-sensor")
sensorX.enable(timestep)

sensorY = robot.getDevice("Y-sensor")
sensorY.enable(timestep)

motorX = robot.getDevice("X-motor")

motorY = robot.getDevice("Y-motor")

kb.enable(timestep)


i = 0



# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    
    # Read the sensors:    
    xValue = sensorX.getValue()
    yValue = sensorY.getValue()
    
    # Print the sensor values:
    #print("X: ", str(xValue), "   Y: ", str(yValue))
    


    # Actuate motors
    motorY.setPosition(queue.listY[i])
    motorY.setVelocity(0.5)
    motorX.setPosition(queue.listX[i])
    motorX.setVelocity(0.5)
   
    # Check keyboard inputs
    key = kb.getKey()
    
    
    #Do something about the keyboard input
    if key == ord('V'):
        if queue.listX[-1] != P1.x or queue.listY[-1] != P1.y:
            queue.add(P1.x, P1.y)
 
    if key == ord('C'):
        if queue.listX[-1] != P2.x or queue.listY[-1] != P2.y:
            queue.add(P2.x, P2.y)
            
    if key == ord('D'):
        if queue.listX[-1] != P3.x or queue.listY[-1] != P3.y:
            queue.add(P3.x, P3.y)

 
    if key == ord('F'):
        if queue.listX[-1] != P4.x or queue.listY[-1] != P4.y:
            queue.add(P4.x, P4.y)
       

       
    if xValue == queue.listX[i] and yValue == queue.listY[i]:       
        if i == len(queue.listX) - 1  or i == len(queue.listY) - 1:
            i = i
        elif i < len(queue.listX) - 1 and i < len(queue.listY) - 1:
            i = i+1

# Enter here exit cleanup code.

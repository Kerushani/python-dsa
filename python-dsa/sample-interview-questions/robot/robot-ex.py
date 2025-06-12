"""
We’d like you to design a simple simulation of a robot vacuum cleaner operating in a rectangular room. 
The robot receives a list of commands to move in the four cardinal directions (up, down, left, right). 
The room is bounded, and the robot cannot move outside its boundaries. 
Additionally, there are certain tiles in the room that contain charging stations. 
The robot must keep track of its position and log any time it visits a charging station.

We’ll provide you with a simple input file that includes the room size, the robot’s starting position, 
locations of chargers, and the sequence of movement commands. Please write a class-based solution that 
parses this input and simulates the robot’s path.

We’ll want to see how you design your classes, 
handle edge cases (like hitting a wall), and track state (like visiting a charger). 
Bonus if you can return or print a summary at the end — for example, the number of unique charging stations 
visited.

->design it like a matrix
input: room size, robot starting position, locations of chargers [2 2], and sequence of movement commands

[0, 0] => [room_size]
"""
import yaml

class Robot:
    def __init__(self, room_size, start, chargers, max_battery=100, battery=100, walls=[]):
        self.length, self.width = room_size
        self.x, self.y = start
        self.chargers = chargers
        self.max_battery = max_battery
        self.battery = battery
        self.walls = walls
        self.directions = {
            "up" : (-1, 0),
            "down": (1, 0),
            "right": (0, 1),
            "left": (0, -1)
        }
    # update x, y with directions
    def getPosition(self):
        return self.x, self.y

    def Move(self, direction):
        if direction not in self.directions:
            print("Invalid direction")
            return False
        if self.battery == 0:
            print("Robot needs charge, cannot move")
            return False
        # valid direction + robot moves
        dx, dy = self.directions[direction]
        self.x += dx
        self.y += dy

        # check if its out of bounds
        if not (0 <= self.x < self.length and 0 <= self.y < self.width):
            print("Out of bounds")
            self.x -= dx
            self.y -= dy
        # check if robot is at a charger
        if [self.x,self.y] in self.chargers:
            self.battery = self.max_battery
        
        # check if its in walls
        if [self.x, self.y] in self.walls:
            print("Hit a wall")
            self.x -= dx
            self.y -= dy

with open("python-dsa/sample-interview-questions/robot/robot.txt", "r") as file:
    content = yaml.safe_load(file)
    # print(content["room_size"])

robot1 = Robot([6,6], [0,0], [[2,2],[5,5], [3,3],[0,5],[1,1]], 98,[[0,1], [2,2]])

commands = ["up", "right", "down", "down", "down"]
for cmd in commands:
    print(f"Currently at: {robot1.getPosition()}")
    robot1.Move(cmd)
    print(f"Now at: {robot1.getPosition()}")
    print(f"Battery: {robot1.battery}")
    print("----")

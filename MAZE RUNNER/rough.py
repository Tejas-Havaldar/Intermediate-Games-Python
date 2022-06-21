import turtle
import random

win = turtle.Screen()
win.bgcolor("black")
win.title("A Maze Runner")
win.setup(width=700,height=700)
win.tracer(0)

# # Register Shapes
# images = []

# for image in images:
#     turtle.register_shape(image)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        # Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor() 

        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor() 

        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def isCollision(self,other):
        if self.distance(other) < 5:
            return True
        else:
            return False

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x,y)
        self.direction = random.choice(["up", "down", "right", "left"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0
        # Calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        # Check if the space has a wall
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        else:
            # Choose a different direction
            self.direction = random.choice(["up", "down", "right","left"])
        
        # Set timer to move next time
        turtle.ontimer(self.move, t=random.randint(100, 300))

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

# Create levels list
levels = [""]

# Create treasures list
treasures = []

# Add enemies list
enemies = []

# Define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",    
"XP  XXXXXXXE        XXXXX",    
"X  XXXXXXX  XXXXXX  XXXXX",    
"X       XX  XXXXXX  XXXXX",    
"X       XX  XXX       EXX",    
"XXXXXX  XX  XXX        XX",    
"XXXXXX  XX  XXXXXX  XXXXX",    
"XXXXXX  XX    XXXX  XXXXX",    
"X  XXX        XXXXT XXXXX",    
"X  XXX  XXXXXXXXXXXXXXXXX",    
"X         XXXXXXXXXXXXXXX",    
"X                XXXXXXXX",    
"XXXXXXXXXXXXX     XXXXX X",    
"XXXXXXXXXXXXXXXX  XXXXX X",    
"XXX  XXXXXXXXXXX        X",    
"XXXE                    X",    
"XXX          XXXXXXXXXXXX",    
"XXXXXXXXXXX  XXXXXXXXXXXX",    
"XXXXXXXXXXX             X",    
"XX  XXXXX               X",    
"XX  XXXXXXXXXXXXXX  XXXXX",    
"XX   YXXXXXXXXXXXX  XXXXX",    
"XXXX        XXXX        X",    
"XXXXE                   X",    
"XXXXXXXXXXXXXXXXXXXXXXXXX"    
]
# Add maze to mazes list
levels.append(level_1)

# Create Level Setup Function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # Get the character at each x, y coordinate
            character = level[y][x]
            # Calculate the screen x, y coordinates
            screen_x = -288 + (x*24)
            screen_y =  288 - (y*24)

            # Check if it is an X (Representing a wall)
            if character == "X":
                pen.goto(screen_x,screen_y)
                pen.stamp()
                walls.append((screen_x,screen_y))
            
            # Check if it is an P (Representing a Player)
            if character == "P":
                player.goto(screen_x,screen_y)
                
            # Check if it is an T (Representing a Treasure)
            if character == "T":
                treasures.append(Treasure(screen_x,screen_y))

            # Check if it is an E (Representing a Enemy)
            if character == "E":
                enemies.append(Enemy(screen_x,screen_y))
# Create A Class Insa
pen = Pen()
player = Player()

# Create wall coordinate list
walls = []

# Set up the level
setup_maze(levels[1])


# Keyboard Bindings
win.listen()
win.onkeypress(player.go_left,"a")
win.onkeypress(player.go_right,"d")
win.onkeypress(player.go_up,"w")
win.onkeypress(player.go_down,"s")

for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

while True:
    win.update()

    # Check for player collision with treasure
    # Iterate through treasure list
    for treasure in treasures:
        if player.isCollision(treasure):
            # Add the treasure gold to the player gold
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            # Destroy the treasure
            treasure.destroy()
            # Remove the treasure from the treasures list
            treasures.remove(treasure)

    for enemy in enemies:
        if player.isCollision(enemy):
            print("Player died!")
    
    
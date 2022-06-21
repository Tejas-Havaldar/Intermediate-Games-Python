from math import gamma
import turtle
import random

win = turtle.Screen()
win.title("Simple Python Game")
win.bgcolor("lightgreen")
win.setup(width=700,height=700)
win.bgpic("space_station_defense_game_background.gif")
win.tracer(0)

class Game(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-290,300)
        self.score = 0

    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), False, align="center", font=("Courier",14,"normal"))

    def change_score(self, points):
        self.score += points
        self.update_score()
    
class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)

    def draw_border(self):
        self.penup()
        self.goto(-300,-300)
        self.pendown()
        self.goto(-300,300)
        self.goto(300,300)
        self.goto(300,-300)
        self.goto(-300,-300)

class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("triangle")
        self.color("white")
        self.speed = 0.09

    def move(self):
        self.forward(self.speed)

        # Check Boundary
        if self.xcor() > 287 or self.xcor() <-287:
            self.right(random.randint(0,180))
            # winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

        if self.ycor() > 287 or self.ycor() <-287:
            self.right(random.randint(0,180))
            # winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    def turnLeft(self):
        self.left(30)
    
    def turnRight(self):
        self.right(30)
    
    def increaseSpeed(self):
        self.speed += 0.01
    
    def decreaseSpeed(self):
        self.speed -= 0.01

    def stop_speed(self):
        self.speed = 0
     
class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        self.color("red")
        self.speed(0)
        self.speed = 0.05
        self.goto(random.randint(-250,250),random.randint(-250,250))
        self.setheading(random.randint(0,360))

    def move(self):
        self.forward(self.speed)

        # Check Boundary
        if self.xcor() > 287 or self.xcor() <-287:
            self.right(random.randint(0,180))
            # winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

        if self.ycor() > 287 or self.ycor() <-287:
            self.right(random.randint(0,180))
            # winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    def jump(self):
        self.goto(random.randint(-250,250),random.randint(-250,250))
        self.setheading(random.randint(0,360))

       

def isCollision(t1,t2):
    if t1.distance(t2) < 20:
        return True

    else:
        return False


# Creating instances
player = Player()
border = Border()
game = Game()

goals = []
for count in range(6):
    goals.append(Goal())

# Draw the Border
border.draw_border()

# Set Keyboard Bindings
win.listen()
win.onkeypress(player.turnLeft,"Left")
win.onkeypress(player.turnRight,"Right")
win.onkeypress(player.increaseSpeed,"Up")
win.onkeypress(player.decreaseSpeed,"Down")
win.onkeypress(player.stop_speed,"space")

# Main Loop
while True:
    win.update()
    player.move()
    for goal in goals:
        goal.move()

        if isCollision(player,goal):
            goal.jump()
            game.change_score(10)
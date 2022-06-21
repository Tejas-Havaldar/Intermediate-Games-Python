import turtle
import random
# import winsound

win = turtle.Screen()
win.title("Simple Python Game")
win.bgcolor("lightgreen")
win.setup(width=700,height=700)
win.bgpic("space_station_defense_game_background.gif")
win.tracer(0)

# Draw Border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.color("white")
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

#Score
score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-250,300)
pen.write("Score: 0", align="center", font=("Courier",18,"normal"))

# Create a Player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
# player.setheading(90)
player.speed(0)
player.penup()

# Create a goal
# goal = turtle.Turtle()
# goal.color("red")
# goal.shape("circle")
# # player.setheading(90)
# goal.speed(0)
# goal.penup()
# goal.goto(random.randint(-300,300),random.randint(-300,300))

# Create Multiple Goals
max_goals = 6
goals = []

for count in range(max_goals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    # player.setheading(90)
    goals[count].speed(0)
    goals[count].penup()
    goals[count].goto(random.randint(-300,300),random.randint(-300,300))

# Set Speed Variable for player
speed = 0.09

# Define Functions
def turnLeft():
    player.left(30)
    player.heading()

def turnRight():
    player.right(30)
    player.heading()

def increaseSpeed():
    global speed
    speed += 0.01

def decreaseSpeed():
    global speed
    speed -= 0.01

def stop_speed():
    global speed
    speed = 0

def isCollision(t1,t2):
    if t1.distance(t2) < 20:
        return True

    else:
        return False


# Keyboard Bindings
win.listen()
win.onkeypress(turnLeft,"Left")
win.onkeypress(turnRight,"Right")
win.onkeypress(increaseSpeed,"Up")
win.onkeypress(decreaseSpeed,"Down")
win.onkeypress(stop_speed,"space")



while True:
    win.update()
    
    player.forward(speed)

    # Check Boundary
    if player.xcor() > 287 or player.xcor() <-287:
        player.right(random.randint(0,180))
        # winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if player.ycor() > 287 or player.ycor() <-287:
        player.right(random.randint(0,180))
        # winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    
    # Collision Checking
    

    # Move the Goal
    for count in range(max_goals):
        goals[count].forward(0.5)

        if goals[count].xcor() > 287 or goals[count].xcor() <-287:
            goals[count].right(random.randint(0,180))
            # winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

        if goals[count].ycor() > 287 or goals[count].ycor() <-287:
            goals[count].right(random.randint(0,180))
            # winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

        if isCollision(player,goals[count]):
            goals[count].goto(random.randint(-300,300),random.randint(-300,300))
            goals[count].right(random.randint(0,360))
            score += 10
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Courier",18,"normal"))
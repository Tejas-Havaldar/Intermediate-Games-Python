import turtle
import random
import winsound

win = turtle.Screen()
win.bgcolor("black")
win.setup(700,700)
win.title("Space Wars")
win.bgpic("space_station_defense_game_background.gif")
win.tracer(0)

class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.lives = 3
        self.state = "playing"
        self.pen = turtle.Turtle() # For Border
        self.pen1 = turtle.Turtle() # For Score
        
    def draw_border(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300,300)
        self.pen.pendown()
        for side in range(4):
            self.pen.forward(600)
            self.pen.right(90)
        self.pen.penup()
        self.pen.hideturtle()

    def show_status(self):
        self.pen1.penup()
        self.pen1.color("white")
        self.pen1.pensize(3)
        self.pen1.goto(-300,310)
        self.pen1.write("Score: {}".format(self.score), False, align="center", font=("Courier",14,"normal"))

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, setx, sety):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.penup()
        self.speed(0)
        self.color(color)
        self.goto(setx, sety)
        self.speed = 0.1

    def move(self):
        self.fd(self.speed)

        # Boundary detection
        if self.xcor() > 290:
            self.setx(290)
            self.right(random.randint(10,170))
        
        if self.xcor() < -290:
            self.setx(-290)
            self.right(random.randint(10,170))

        if self.ycor() > 290:
            self.sety(290)
            self.right(random.randint(10,170))

        if self.ycor() < -290:
            self.sety(-290)
            self.right(random.randint(10,170))
    
    def is_collision(self,other):
        if self.distance(other) < 15:
            return True
        else:
            return False

class Player(Sprite):
    def __init__(self, spriteshape, color, setx, sety):
        Sprite.__init__(self, spriteshape, color, setx, sety)
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.speed = 0.09
        self.lives = 3
    
    def turn_left(self):
        self.left(45)

    def turn_right(self):
        self.right(45)
    
    def accelerate(self):
        self.speed += 0.01 
    
    def decelerate(self):
        self.speed -= 0.01
    
class Enemy(Sprite):
    def __init__(self, spriteshape, color, setx, sety):
        Sprite.__init__(self, spriteshape, color, setx, sety)
        self.speed = 0.2
        self.setheading(random.randint(0,360))

class Ally(Sprite):
    def __init__(self, spriteshape, color, setx, sety):
        Sprite.__init__(self, spriteshape, color, setx, sety)
        self.speed = 0.4
        self.setheading(random.randint(0,360))

    def move(self):
            self.fd(self.speed)

            # Boundary detection
            if self.xcor() > 290:
                self.setx(290)
                self.left(random.randint(10,170))
            
            if self.xcor() < -290:
                self.setx(-290)
                self.left(random.randint(10,170))

            if self.ycor() > 290:
                self.sety(290)
                self.left(random.randint(10,170))

            if self.ycor() < -290:
                self.sety(-290)
                self.left(random.randint(10,170))

class Missile(Sprite):
    def __init__(self, spriteshape, color, setx, sety):
        Sprite.__init__(self, spriteshape, color, setx, sety)
        self.shapesize(stretch_wid=0.2, stretch_len=0.3,outline=None)
        self.speed = 1
        self.status = "ready"
        self.goto(-1000,1000)

    def fire(self):
        if self.status == "ready":
            # winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
            self.goto(player.xcor(),player.ycor())
            self.setheading(player.heading())
            self.status = "firing"
        
    def move(self):
        if self.status == "ready":
            self.goto(-1000,1000)

        if self.status == "firing":
            self.forward(self.speed)

        # Border check
        if self.xcor() < -290 or self.xcor() > 290 or self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000,1000)
            self.status = "ready"


# Create game object
game = Game()

# Draw the game border
game.draw_border()

# Show game status
game.show_status()

# Create my sprites
player = Player("triangle","white",0,0)
missile = Missile("triangle","yellow",0,0)
# enemy = Enemy("circle","red",-100,0)
# ally = Ally("square","blue",0,0)

# Create Multiple Enemies
enemies = []
for i in range(5):
    enemies.append(Enemy("circle","red",-100,0))

# Create Multiple allies
allies = []
for i in range(5):
    allies.append(Ally("square","blue",0,0))

# Keyboard Bindings
win.listen()
win.onkeypress(player.turn_left, "a")
win.onkeypress(player.turn_right, "d")
win.onkeypress(player.accelerate, "w")
win.onkeypress(player.decelerate, "s")
win.onkeypress(missile.fire, "space")



while True:
    win.update()

    player.move()
    # enemy.move()
    missile.move()
    # ally.move()
    
    for enemy in enemies:
        enemy.move()

        # Check for collision
        if player.is_collision(enemy):
            # winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            x = random.randint(-250,250)
            y = random.randint(-250,250)
            enemy.goto(x,y)
    
        # Check for collision between missile and enemy
        if missile.is_collision(enemy):
            # winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            x = random.randint(-250,250)
            y = random.randint(-250,250)
            enemy.goto(x,y)
            missile.status = "ready"

            # Increase the score
            game.score += 10
            game.pen1.clear()
            game.show_status()
        
    for ally in allies:
        ally.move()
    
        # Check for collision between missile and ally
        if missile.is_collision(ally):
            # winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            x = random.randint(-250,250)
            y = random.randint(-250,250)
            ally.goto(x,y)
            missile.status = "ready"

            # decrease the score
            game.score -= 10
            game.pen1.clear()
            game.show_status()
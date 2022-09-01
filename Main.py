import turtle
# import os
import math
import random

# Screen Setup
wn = turtle.Screen()
width = 960
height = 540
wn.setup(width+20, height+20)
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("/home/abraar/Documents/CODE STUF/GitHub Backup/Chicken-Invaders-Clone/src/background.gif")
wn.tracer(0)

# Custom Shapes
wn.register_shape("/home/abraar/Documents/CODE STUF/GitHub Backup/Chicken-Invaders-Clone/src/chickff.gif")
wn.register_shape("/home/abraar/Documents/CODE STUF/GitHub Backup/Chicken-Invaders-Clone/src/player.gif")
wn.register_shape("/home/abraar/Documents/CODE STUF/GitHub Backup/Chicken-Invaders-Clone/src/missile.gif")

# Drawing border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
lcx = -width/2
lcy = -height/2
border_pen.setposition(lcx, lcy)
border_pen.pendown()
border_pen.pensize(1)
border_pen.fd(width)
border_pen.lt(90)
border_pen.fd(height)
border_pen.lt(90)
border_pen.fd(width)
border_pen.lt(90)
border_pen.fd(height)
border_pen.hideturtle()


score = 0

# Drawing the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("pink")
score_pen.penup()
score_pen.setposition(100, 100)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "bold"))
score_pen.hideturtle()

# Creatng the Spaceship
player = turtle.Turtle()
player.color("blue")
player.shape("/home/abraar/Documents/CODE STUF/GitHub Backup/Chicken-Invaders-Clone/src/player.gif")
player.penup()
player.speed(0)
buffer_player_y = 30
player.setposition(0, buffer_player_y-(height/2))
#  player.setheading(90) (for triangle)

player.speed = 0

# Choose a number of enemies
number_of_enemies = 20
# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.shape('/home/abraar/Documents/CODE STUF/GitHub Backup/Chicken-Invaders-Clone/src/chickff.gif')
	enemy.penup()
	enemy.speed(0)
	x = random.randint(int(-width/2 +60), int(width/2 -60))
	y = random.randint( 80, int(height/2 - 60))
	enemy.setposition(x, y)
enemyspeed = 0.05


# Create the player's bullet
bullet = turtle.Turtle()
bullet.shape("/home/abraar/Documents/CODE STUF/GitHub Backup/Chicken-Invaders-Clone/src/missile.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.8, 0.8)
bullet.hideturtle()

bulletspeed = 15

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"


# Move the player left and right
def move_left():
	player.speed = -25
	x = player.xcor()
	x += player.speed
# jodi boundari set korte chai -	if x < -280: x = - 280
	player.setx(x)
def move_right():
	player.speed = 25
	x = player.xcor()
	x += player.speed
# jodi boundari set korte chai -	if x < -280: x = - 280
	player.setx(x)

#def move_up():
#	player.speed = 15
#def move_down():
#	player.speed = -15

#def move_players_Y():
#	y = player.ycor()
#	y += player.speed/2
#	player.sety(y)


def fire_bullet():
	# Declare bulletstate as a global if it needs changed
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"
		# Move the bullet to the just above the player
		x = player.xcor()
		y = player.ycor() + 20
		bullet.setposition(x, y)
		bullet.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 30:
		return True
	else:
		return False
# Create keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
#wn.onkeypress(move_up, "Up")
#wn.onkeypress(move_down, "Down")
wn.onkeypress(fire_bullet, "space")

# Main game loop
while True:
	wn.update()

	for enemy in enemies:
		# Move the enemy
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		# Move the enemy back and down
		if enemy.xcor() > ((width/2)-25):
			for e in enemies:
				y = e.ycor()
				y -= 50
				e.sety(y)
			enemyspeed *= -1.02

		if enemy.xcor() < -((width/2)-25):
			for e in enemies:
				y = e.ycor()
				y -= 50
				e.sety(y)
			enemyspeed *= -1.02

		# Check for a collision between the bullet and the enemy
		if isCollision(bullet, enemy):
			# Reset the bullet
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)
			# Reset the enemy
			x = random.randint(int(-width/2 +60), int(width/2 -60))
			y = random.randint( 80 , int(height/2 -60))
			enemy.setposition(x, y)
			# Update the score
			score += 10
			scorestring = "Score: {}".format(score)
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			print ("Game Over")
			break


	# Move the bullet
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)

	# Check to see if the bullet has gone to the top
	if bullet.ycor() > height-40:
		bullet.hideturtle()
		bulletstate = "ready"

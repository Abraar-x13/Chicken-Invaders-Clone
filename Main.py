import turtle
import math
import random

# Variables
start_screen = "src/start_screen1.gif"
game_screen = "src/background.gif"
game_over_screen = "src/gameoverscreen.gif"
shape_chicken = "src/chickff.gif"
shape_player = "src/player.gif"
shape_missile = "src/missile.gif"
shape_enemy = "src/chickff.gif"
width, height = 960, 540
score, number_of_enemies = 0, 20
enemies, enemyspeed = [turtle.Turtle() for _ in range(number_of_enemies)], 0.045
# Note : 'enemyspeed' is an experimental value, have to change for different machines.


# Window Setup
wn = turtle.Screen()
wn.setup(width+60, height+60)
wn.bgcolor("black")
wn.title("Chiken Invaders")
wn.tracer(0)
wn.bgpic(start_screen)
player_name = wn.textinput("player_name", " Player Name :")
wn.bgpic(game_screen)
wn.register_shape(shape_chicken)
wn.register_shape(shape_player)
wn.register_shape(shape_missile)


# Player Spaceship Setup
player = turtle.Turtle()
player.color("blue")
player.shape(shape_player)
player.penup()
player.speed(0)
player.setposition(0, 30-(height/2))
player.speed = 0


# Bullet Setup
bullet = turtle.Turtle()
bullet.shape(shape_missile)
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.8, 0.8)
bullet.hideturtle()
bulletspeed = 15
bulletstate = "ready"


# Enemy Setup
for enemy in enemies:
	enemy.shape(shape_enemy)
	enemy.penup()
	enemy.speed(0)
	x = random.randint(int(-width/2 +60), int(width/2 -60))
	y = random.randint( 80, int(height/2 - 60))
	enemy.setposition(x, y)



# Scoring System
score_pen = turtle.Turtle()
def update_score(_score, _x = -120, _y = 250, _fontsz = 14):
	score_pen.speed(0)
	score_pen.pensize(5)
	score_pen.color("white")
	score_pen.penup()
	score_pen.setposition(_x, _y)
	scorestring = f"Player : {player_name}	Score : {_score}"
	score_pen.write(scorestring, False, align="left", font=("Arial", _fontsz, "bold"))
	score_pen.hideturtle()
update_score(0)


# Functions to move player
def move_left():
	player.speed = -25
	x = player.xcor() + player.speed
	player.setx(x)
def move_right():
	player.speed = 25
	x = player.xcor() + player.speed
	player.setx(x)


def fire_bullet():
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"
		bullet.setposition(player.xcor(), player.ycor() + 20)
		bullet.showturtle()


def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 30:
		return True
	else:
		return False


# Keyboard Bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")


# Main Game loop
is_alive = True
while is_alive:
    
	wn.update()
	
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)

	if bullet.ycor() > height-40:
		bullet.hideturtle()
		bulletstate = "ready"
  

	for enemy in enemies:
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		if enemy.xcor() > ((width/2)-25):
			for e in enemies:
				e.sety(e.ycor() - 50)
			enemyspeed *= -1.015

		if enemy.xcor() < -((width/2)-25):
			for e in enemies:
				e.sety(e.ycor() - 50)
			enemyspeed *= -1.015

		if isCollision(bullet, enemy):

			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)

			x = random.randint(int(-width/2 +60), int(width/2 -60))
			y = random.randint( 80 , int(height/2 -60))
			enemy.setposition(x, y)

			score += 10
			score_pen.clear()
			update_score(score)

		if isCollision(player, enemy):
			is_alive = False
			wn.clear()
			break


# Game Over Screen
while True:
    wn.bgpic(game_over_screen)
    update_score(score, -165, -50, 20)
    wn.update()
 
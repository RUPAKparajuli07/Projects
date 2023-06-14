from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
score = 0
high_score = 0
game_over = False

def tap(x, y):
    """Respond to screen tap."""
    global speed, game_over
    if game_over:
        # If the game is over, reset the game and start a new game
        reset_game()
    elif not inside(ball):
        ball.x = -199
        ball.y = -199
        # Set the speed vector based on the position of the tap
        speed = vector((x + 200) / 25, (y + 200) / 25)

def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(10, 'red')

    goto(-190, 190)
    write(f"Score: {score}, High Score: {high_score}", align="left", font=("Arial", 14, "normal"))

    if game_over:
        goto(0, 0)
        write("Game Over!\nClick anywhere to play again.", align="center", font=("Arial", 20, "normal"))

    update()


def move():
    """Move ball and targets."""
    global score, high_score, game_over
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        # Apply gravity to the ball
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        else:
            score += 1
            if score > high_score:
                high_score = score

    draw()

    for target in targets:
        if not inside(target):
            game_over = True

    if game_over:
        ontimer(move, 0)
    else:
        ontimer(move, 50)


def reset_game():
    """Reset the game."""
    global ball, speed, targets, score, game_over
    ball = vector(-200, -200)
    speed = vector(0, 0)
    targets = []
    score = 0
    game_over = False


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

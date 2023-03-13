from random import *
from turtle import *
from freegames import vector

bird = vector(0, 0)
balls = []
score = 0
high_score = 0

def tap(x, y):
    """Move bird up in response to screen tap."""
    up = vector(0, 30)
    bird.move(up)

def inside(point):
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200

def draw(alive):
    """Draw screen objects."""
    clear()

    goto(bird.x, bird.y)

    if alive:
        dot(10, 'green')
    else:
        dot(10, 'red')

    for ball, color in balls:
        goto(ball.x, ball.y)
        dot(20, color)

    # Draw the score board on the left side
    goto(-200, 180)
    write(f'Score: {score} High Score: {high_score}', font=('Arial', 16, 'normal'))

    update()

def move():
    """Update object positions."""
    global score, high_score

    bird.y -= 5

    for ball, _ in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        color = choice(['red', 'blue', 'green', 'yellow', 'purple']) # randomly choose a color
        balls.append((ball, color))

    while len(balls) > 0 and not inside(balls[0][0]):
        balls.pop(0)

    if not inside(bird):
        if score > high_score:
            high_score = score
        score = 0
        draw(False)
        replay = textinput("Game Over", "Play again? (Y/N)").lower()
        if replay == 'y':
            reset()
        else:
            return

    for ball, color in balls:
        if abs(ball - bird) < 15:
            score += 1
            if score > high_score:
                high_score = score
            balls.remove((ball, color))
            break

    draw(True)

    # Increase speed when score is a multiple of 50
    if score % 10 == 0 and score != 0 and score % 20 != 0:
        delay = 10
    else:
        delay = 50

    ontimer(move, delay)

def reset():
    """Reset game to initial state."""
    global bird, balls, score
    bird = vector(0, 0)
    balls = []
    score = 0
    move()

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

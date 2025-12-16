import turtle, random

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)

for _ in range(200):
    t.color(random.random(), 0, random.random())
    t.dot(random.randint(4,12))
    t.goto(random.randint(-200, 200), random.randint(-200, 200))

from turtle import Turtle
MOVE_DISTANCE = 20
POSITIONS = ((0, 0), (-20, 0), (-40, 0))
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        new_snake = Turtle(shape="square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def extend(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for n in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[n - 1].xcor()
            new_y = self.snakes[n - 1].ycor()
            self.snakes[n].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

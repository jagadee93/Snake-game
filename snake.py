from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] # initializes head

    def create_snake(self):
        """ creates the initial snake aligns snake positions"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """defines the snake specifications"""
        new_segment = Turtle("circle")
        new_segment.color("blue")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """ adds extra segment to the tail when called """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """ moves the snake and ensures that the snake is moving properly when snake is turned """
        for segment in range(len(self.segments)-1, 0, -1): # moving from last segment
            new_x = self.segments[segment-1].xcor()
            new_y = self.segments[segment-1].ycor()
            self.segments[segment].goto(new_x, new_y) # last segment will goto second segment position vice versa
        self.segments[0].forward(MOVE_DISTANCE) # moves the head

    def up(self):
        """ ensures snake moves in single direction"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """ ensures snake moves in single direction"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """ ensures snake moves in single direction"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """ ensures snake moves in single direction"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
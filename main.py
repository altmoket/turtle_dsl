
from textx import metamodel_from_file

turtleMeta = metamodel_from_file('turtle.tx')

scene = turtleMeta.model_from_file('codeExamples/triangle_and_square.turtle')

import turtle

def draw_shape(shape):
    turtle.pencolor(shape.line_color.color if shape.line_color is not None else 'black')
    turtle.fillcolor(shape.fill_color.color if shape.fill_color is not None else 'white')
    turtle.down()
    turtle.begin_fill()
    for l in shape.lines:
        draw_line(l)
    turtle.end_fill()
    
def draw_line(l):
    bearing = l.direction.bearing
    if bearing == 'N':
        turtle.setheading(90)
    elif bearing == 'NE':
        turtle.setheading(45)
    elif bearing == 'E':
        turtle.setheading(0)
    elif bearing == 'SE':
        turtle.setheading(315)
    elif bearing == 'S':
        turtle.setheading(270)
    elif bearing == 'SW':
        turtle.setheading(215)
    elif bearing == 'W':
        turtle.setheading(180)
    elif bearing == 'NW':
        turtle.setheading(135)
    else:
        turtle.left(l.direction.angle.degrees)
    turtle.forward(l.length)

for d in scene.draw_instructions:
    turtle.up()
    turtle.goto(d.position.x if d.position is not None else 0,
                d.position.y if d.position is not None else 0)
    draw_shape(d.shape)

turtle.hideturtle()
turtle.done()



from textx import metamodel_from_file

turtleMeta = metamodel_from_file('turtle.tx')

scene = turtleMeta.model_from_file('codeExamples/triangle_and_square.turtle')


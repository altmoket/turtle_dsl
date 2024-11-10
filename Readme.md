# Turtle DSL

## Project Description
Turtle DSL is a Domain-Specific Language designed to provide intuitive instructions for the Python Turtle graphics library. This project allows users to define shapes and their properties in a simple and readable syntax, enabling easy drawing on a canvas.

## Example Syntax
Here’s an example of how to use the Turtle DSL:

```plaintext
shape triangle
    line red
    fill yellow
    line E 400
    line N 300
    line 126.9 deg 500
end

shape square
    line blue
    fill #aaffaa
    line S 100
    line W 100
    line N 100
    line E 100
end

shape black_and_white
    line E 150
    line NW 71
    line W 50
    line SW 71
end

draw triangle // The default position is 0,0, the center of the canvas
draw square at -10, -10
draw black_and_white at 225, 150
```

## Features

- **Shape Definition**: Easily define custom shapes with specific colors and fill patterns.
- **Simple Drawing Commands**: Use intuitive commands to draw lines in various directions.
- **Positioning**: Specify the position of shapes on the canvas with ease.
- **Color Support**: Utilize named colors and hex codes for fills and lines.

## Installation

To get started with Turtle DSL, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/turtle-dsl.git
   ```
2. Navigate to the project directory:
   ```bash
   cd turtle-dsl
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Usage
```zsh
python main.py
```

The import of the turtle module is necessary to draw the snowflake because turtle is a really good library for the goal to achieve with this function.
```python
import turtle
```

The function setSpeed is used to set the speed of the turtle. The speed is set to 0 by default because the turtle should draw the snowflake as fast as possible.
```python
def setSpeed(speedtoset:int=0):
    turtle.speed(speedtoset)
```

The function finish is used to hide the turtle and to end the program. This function is normally called at the end of the program. The turtle is hidden because it is not necessary to see the turtle anymore. The turtle.done() function is used to end the program. This function is necessary because the turtle module is not able to end the program by itself.
```python
def finish():
    turtle.hideturtle()
    turtle.done()
```

The function kochcurve is used to draw a koch curve. The leng parameter is used to set the length of the koch curve. The i parameter is used to set the number of iterations. The turn parameter is used to set the turn direction of the turtle. The turn parameter is set to turtle.left by default because the default of the programm is the normal koch snowflake.
First the function checks if the number of iterations is 0. If the number of iterations is 0 the function draws a line with the length of the leng parameter. Then the function turns the turtle 60 degrees to the left. Then the function draws a line with the length of the leng parameter. Then the function turns the turtle 240 degrees to the left. Then the function draws a line with the length of the leng parameter. Then the function turns the turtle 60 degrees to the left. Then the function draws a line with the length of the leng parameter. If the number of iterations is not 0 the function draws a koch curve with the length of the leng parameter divided by 3 and the number of iterations minus 1. Then the function turns the turtle 60 degrees to the left. Then the function draws a koch curve with the length of the leng parameter divided by 3 and the number of iterations minus 1. Then the function turns the turtle 240 degrees to the left. Then the function draws a koch curve with the length of the leng parameter divided by 3 and the number of iterations minus 1. Then the function turns the turtle 60 degrees to the left. Then the function draws a koch curve with the length of the leng parameter divided by 3 and the number of iterations minus 1.
```python
def kochcurve(leng:int, i:int, turn=turtle.left) -> None:
    if i == 0:
        turtle.forward(leng)
        turn(60)
        turtle.forward(leng)
        turn(240)
        turtle.forward(leng)
        turn(60)
        turtle.forward(leng)
    else:
        kochcurve(leng/3, i - 1, turn)
        turn(60)
        kochcurve(leng/3, i - 1, turn)
        turn(240)
        kochcurve(leng/3, i - 1, turn)
        turn(60)
        kochcurve(leng/3, i - 1, turn)
```

The function kochsnowlake is used to draw a koch snowflake. The leng parameter is used to set the length of the koch snowflake. The i parameter is used to set the number of iterations. The howoften parameter is used to set the number of sides of the koch snowflake. The howoften parameter is set to 3 by default because the default of the programm is the normal koch snowflake. The turncurve parameter is used to set the turn direction of the turtle. The turncurve parameter is set to turtle.left by default because the default of the programm is the normal koch snowflake. The turn parameter is used to set the turn direction of the turtle. The turn parameter is set to turtle.right by default because the default of the programm is the normal koch snowflake. The colorOutline parameter is used to set the color of the outline of the koch snowflake. The colorOutline parameter is set to "black" by default because the default of the programm is the normal koch snowflake. The colorFill parameter is used to set the color of the fill of the koch snowflake. The colorFill parameter is set to "white" by default because the default of the programm is the normal koch snowflake. First the function sets the color of the outline and the fill of the koch snowflake. Then the function begins the fill of the koch snowflake. Then the function calculates the degrees of the koch snowflake. Then the function draws a koch snowflake with the length of the leng parameter, the number of iterations of the i parameter, the number of sides of the howoften parameter, the turn direction of the turncurve parameter, the turn direction of the turn parameter, the color of the outline of the colorOutline parameter and the color of the fill of the colorFill parameter. Then the function ends the fill of the koch snowflake.
```python
def kochsnowlake(leng:int, i:int, howoften:int=3, turncurve=turtle.left, turn=turtle.right, colorOutline:str="black", colorFill:str="white"):
    turtle.color(colorOutline, colorFill)
    turtle.begin_fill()

    degres = 360/howoften
    for _ in range(howoften):
        kochcurve(leng, i, turncurve)
        turn(degres)

    turtle.end_fill()
```

This main script is how the drawing should look like. In the middle of the script (the empty line) a drawing function is called (customizable by the user).
```python
if __name__ == "__main__":
    setSpeed(0)

    finish()
```
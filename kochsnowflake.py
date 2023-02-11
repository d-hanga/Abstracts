import turtle






def setSpeed(speedtoset:int=0):
    turtle.speed(speedtoset)



def finish():
    turtle.hideturtle()
    turtle.done()



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



def kochsnowlake(leng:int, i:int, howoften:int=3, turncurve=turtle.left, turn=turtle.right, colorOutline:str="black", colorFill:str="white"):
    turtle.color(colorOutline, colorFill)
    turtle.begin_fill()

    degres = 360/howoften
    for _ in range(howoften):
        kochcurve(leng, i, turncurve)
        turn(degres)

    turtle.end_fill()



if __name__ == "__main__":
    setSpeed(0)

    finish()
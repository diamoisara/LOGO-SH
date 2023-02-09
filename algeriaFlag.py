import turtle
turtle.bgcolor("cyan")
turtle.title("Happy Independance Day Algeria")
def drawfillRectangle(x,y,length,width,color):
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  turtle.color(color)
  turtle.begin_fill()
  turtle.forward(width)
  turtle.right(90)
  turtle.forward(length)
  turtle.right(90)
  turtle.forward(width)
  turtle.right(90)
  turtle.forward(length)
  turtle.right(90)
  turtle.end_fill()

def drawStar(x,y,color,length):
  turtle.penup()
  turtle.goto(x,y)
  turtle.setheading(0)
  turtle.pendown()
  turtle.begin_fill()
  turtle.color(color)
  for star in range(0,5):
    turtle.forward(length)
    turtle.right(144)
  turtle.end_fill()

def drawCircle(x,y,color,radius):
  turtle.penup()
  turtle.goto(x,y)
  turtle.color(color)
  turtle.begin_fill()
  turtle.circle(radius)
  turtle.end_fill()

def drawMoon(x,y,color,radius):
  turtle.penup()
  turtle.goto(x,y)
  turtle.color(color)
  turtle.begin_fill()
  turtle.circle(radius)
  turtle.end_fill()

drawfillRectangle(-230,125,280,460,'white')
drawfillRectangle(-230,125,280,230,'dark green')
drawCircle(35,-90,'red',60)
drawMoon(50,-80,'white',50)
drawStar(-5,-20,'red',60)

turtle.hideturtle()
turtle.done()


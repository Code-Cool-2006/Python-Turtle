import turtle
t = turtle.Turtle()
#t.hideturtle()
#t.speed(10)
t.shape("turtle")

t.color("#FF4E08")

t.penup()
t.right(180)
t.forward(700)
t.left(180)
t.pendown()
t.begin_fill()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(180)
t.forward(100)
t.end_fill()

t.penup()
t.right(90)
t.forward(110)
t.pendown()

t.color("#5ABB00")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(180)
t.forward(100)
t.end_fill()

t.penup()
t.forward(110)
t.left(90)
t.pendown()

t.color("#FFBA00")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

t.penup()
t.forward(110)
t.left(90)
t.pendown()

t.color("#00ADEC")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

t.penup()
t.right(90)
t.forward(140)
t.pendown()

t.pensize(10)
t.pencolor("#706D6E")

t.right(90)
t.forward(50)
t.right(180)
t.forward(100)
t.left(210)
t.forward(70)
t.left(120)
t.forward(70)
t.left(210)
t.forward(100)

t.penup()
t.left(90)
t.forward(30)
t.pendown()
t.left(90)
t.forward(50)
t.penup()
t.forward(14)
t.pendown()
t.dot(16)
t.penup()
t.right(180)
t.forward(13)
t.left(90)
t.forward(50)
t.left(180)
t.pendown()
t.circle(25 , 180 ) 

t.penup()
t.forward(24)
t.left(90)
t.pendown()

t.forward(50)
t.back(13)
t.right(0)
t.circle(-11 , 180)

t.penup()
t.forward(41)
t.left(90)
t.forward(28)
t.pendown()
t.circle(23 , 360)
t.penup()
t.forward(38)
t.pendown()
t.forward(5)
t.circle(13 , 160)
t.circle(-13 , 160)
t.penup()
t.right(90)
t.forward(50)
t.left(90)
t.forward(45)
t.pendown()
t.circle(23 , 360)
t.penup()
t.forward(44)
t.pendown()
t.left(90)
t.forward(46)
t.right(90)
t.fd(20)
t.bk(40)
t.fd(20)
t.left(90)
t.circle(-25 , 90)
t.right(90)
t.penup()
t.forward(25)
t.left(90)
t.forward(10)
t.pendown()
t.fd(40)
t.back(20)
t.right(90)
t.fd(45)
t.bk(65)
t.penup()
t.fd(65)
t.left(90)
t.fd(50)
t.stamp()
turtle.done()
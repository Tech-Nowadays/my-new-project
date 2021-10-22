# import turtle
#
# # turtle object
# pen = turtle.Turtle()
#
#
# # function for creation of eye
# def eye(col, rad):
#     pen.down()
#     pen.fillcolor(col)
#     pen.begin_fill()
#     pen.circle(rad)
#     pen.end_fill()
#     pen.up()
#
#
# # draw face
# pen.fillcolor('yellow')
# pen.begin_fill()
# pen.circle(100)
# pen.end_fill()
# pen.up()
#
# # draw eyes
# pen.goto(-40, 120)
# eye('white', 15)
# pen.goto(-37, 125)
# eye('black', 5)
# pen.goto(40, 120)
# eye('white', 15)
# pen.goto(40, 125)
# eye('black', 5)
#
# # draw nose
# pen.goto(0, 75)
# eye('black', 8)
#
# # draw mouth
# pen.goto(-40, 85)
# pen.down()
# pen.right(90)
# pen.circle(40, 180)
# pen.up()
#
# # draw tongue
# pen.goto(-10, 45)
# pen.down()
# pen.right(180)
# pen.fillcolor('red')
# pen.begin_fill()
# pen.circle(10, 180)
# pen.end_fill()
# pen.hideturtle()
# turtle.done()
import turtle

# define pen size
turtle.pensize(5)

# define pen color
turtle.pencolor("Blue")
# for outer bigger circle
facesize = 200
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(facesize)
# for eyes
# Màu nền mắt là màu đỏ
turtle.fillcolor("red")
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()

# khai bao bien eyesize lưu kích thước mắt
eye_size = 17.5

turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()
turtle.penup()

turtle.goto(100, 50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()
# for nose
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.circle(-70, steps=3)
# for smile
turtle.penup()
turtle.goto(-100, -70)
turtle.pendown()
turtle.right(90)
turtle.circle(100, 180)
turtle.mainloop()
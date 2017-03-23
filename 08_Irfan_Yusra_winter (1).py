import turtle
import random
import math
t=turtle.Pen()#other details
t1=turtle.Pen()#snowman
t2=turtle.Pen()#house and window
t3=turtle.Pen()#right eye
t4=turtle.Pen()#santa
t5=turtle.Pen()#deer
t6=turtle.Pen()#smoke
turtle.delay(0)
t.hideturtle()
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
t4.hideturtle()

t.speed("fastest")
t1.speed("fastest")
t2.speed("fastest")
t3.speed("fastest")
t4.speed("fastest")
t5.speed("fastest")
t6.speed("fastest")
turtle.setup(1200,1000)

t.color("#48F4F9")#light blue
t.begin_fill()
t.goto(-1000,1000)
t.goto(1000,1000)
t.goto(1000,-1000)
t.goto(-1000,-1000)
t.goto(-1000,1000)
t.end_fill()

##############ground#########################
#snow
t.color("white")
t.begin_fill()        
t.goto(-1000,-300)
t.goto(1000,-300)
t.goto(1000,-1000)
t.goto(-1000,-1000)
t.goto(-1000,-300)
t.end_fill()

turtle.delay(0)
t.up()
t.color("white")
t.goto(-750,-300)
t.down()
t.begin_fill()

#hill bottom- right
t.color("white")
t.begin_fill()
t.up()
t.goto(250,-360)
t.seth(40)
t.down()

for x in range (60):
    t.forward(8)
    t.right(1)
t.forward(110)
t.end_fill()

#hill
def hill(x,y):
    t.pensize(1)
    t.color("white")
    t.begin_fill()
    t.up()
    t.goto(x,y)
    t.seth(120)
    t.down()
    for x in range (60):
        t.forward(8)
        t.left(2)
    t.forward(100)
    t.end_fill()




#############snowman###################
    
def snowman():
    t1.up()
    t1.goto(-350,-390)
    t1.down()
    #Bottom snowball
    t1.seth(0)
    t1.fillcolor("white")
    t1.pencolor("gray75")
    t1.begin_fill()
    t1.circle(75)
    t1.end_fill()

    t1.pencolor("white")
    t1.pensize(20)
    t1.forward(90)
    t1.backward(150)

    #Second snowball
    t1.up()
    t1.pensize(3)
    t1.pencolor("gray75")
    t1.seth(90)
    t1.forward(130)
    t1.seth(0)
    t1.forward(60)
    t1.down()
    t1.begin_fill()
    t1.circle(45)
    t1.end_fill()
    t1.pencolor("white")
    t1.pensize(6)
    t1.forward(30)
    t1.backward(55)
    #third snowball
    t1.up()
    t1.pensize(3)
    t1.pencolor("gray75")
    t1.seth(90)
    t1.forward(80)
    t1.seth(0)
    t1.forward(27)
    t1.down()
    t1.begin_fill()
    t1.circle(30)
    t1.end_fill()
    t1.pencolor("white")
    t1.pensize(6)
    t1.forward(6)
    t1.backward(33)

    #nose
    t1.pensize(1)
    t1.up()
    t1.goto(-350,-150)
    t1.down()
    t1.color("orange")
    t1.begin_fill()
    t1.circle(5)
    t1.end_fill()

    #go to left eye (lifted)
    t1.up()
    t1.goto(-365,-140)
    t1.down()

    #draw and fill left eye
    t1.color("black")
    t1.begin_fill()
    t1.circle(5)
    t1.end_fill()

    #go to right eye(lifted)
    t3.up()
    t3.goto(-335,-140)
    t3.down()
    #draw and fill right eye
    t3.color("black")
    t3.begin_fill()
    t3.circle(5)
    t3.end_fill()
    t3.hideturtle()

    #go to mouth (lifted)
    t1.up()
    t1.goto(-360,-165)
    t1.down()

    #draw and fill the mouth
    t1.width("5")
    for x in range (4):
        t1.forward(5)
        t1.left(10)

    #right arm
    t1.up()
    t1.color("brown")
    t1.goto(-310,-200)
    t1.down()

    t1.goto(-280,-210)
    t1.right(50)
    t1.forward(25)
    t1.backward(25)
    t1.left(20)
    t1.forward(25)
    t1.backward(25)
    t1.left(20)
    t1.forward(25)

    #left arm
    t1.up()
    t1.goto(-390,-200)
    t1.down()
    t1.goto(-420,-210)
    t1.right(110)
    t1.forward(25)
    t1.backward(25)
    t1.right(20)
    t1.forward(25)
    t1.backward(25)
    t1.right(20)
    t1.forward(25)
    t1.backward(25)

    #scarf
    t1.width("10")
    t1.color("red")
    t1.up()
    t1.goto(-375,-170)
    t1.left(45)
    t1.down()
    t1.circle(30,120)
    t1.setheading(270)
    t1.forward(50)
    t1.backward(60)

    #buttons
    t1.up()
    t1.goto(-350,-205)
    t1.down()
    t1.width(10)
    t1.color("green")
    t1.circle(1)
    t1.up()
    t1.goto(-350,-250)
    t1.down()
    t1.circle(1)
    t1.up()
    t1.goto(-350,-290)
    t1.down()
    t1.circle(1)


#################Trees#######
def trees(x,y):
    #The Tree... branch
    t.left(90)
    t.color("#715418")#brown color
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.forward(50)
    t.right(90)
    t.forward(10.5)
    t.end_fill()  
    #Green part of tree
    t.up()
    t.backward(50)
    t.right(90)
    t.backward(40)
    t.down()
    t.color("#008500")#Green color
    t.begin_fill()
    for a in range (3):
        t.forward(150)
        t.right(120)
        t.forward(150)
        t.right(120)
        t.forward(150)
        t.up()
        t.seth(90)
        t.forward(40)
        t.left(90)
        t.down()
    t.end_fill()
    t.seth(0)
    t.left(270)

def small_trees(x,y):
     #The Tree... branch
    t.left(90)
    t.color("#715418")#brown color
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.forward(12.5)
    t.right(90)
    t.forward(2.625)
    t.end_fill()  
    #Green part of tree
    t.up()
    t.backward(12.5)
    t.right(90)
    t.backward(10)
    t.down()
    t.color("#008500")#Green color
    t.begin_fill()
    for a in range (3):
        t.forward(37.5)
        t.right(120)
        t.forward(37.5)
        t.right(120)
        t.forward(37.5)
        t.up()
        t.seth(90)
        t.forward(10)
        t.left(90)
        t.down()
    t.end_fill() 
    t.seth(0)
    t.left(270)
    

#############house##################3
def house():
    turtle.delay(0)
    t2.up()
    t2.goto(-600,-250)
    t2.seth(360)
    t2.fillcolor("#9E784C")
    t2.begin_fill()
    t2.down()
    t2.forward(75) 
    t2.right(-90) 
    t2.forward(75) 
    t2.right(-90) 
    t2.forward(75) 
    t2.right(-90) 
    t2.forward(75)
    t2.end_fill()
    t2.up()
    t2.right(180)
    t2.forward(75)
    t2.fillcolor("#A91B1B")
    t2.begin_fill()
    t2.down()
    t2.right(45)
    t2.forward(53.5)
    t2.right(90)
    t2.forward(53.5)
    t2.end_fill()
    
    #chimeny
    t2.color("#A91B1B")
    t2.begin_fill()
    t2.backward(26.5)
    t2.left(135)
    t2.forward(25)
    t2.right(90)
    t2.forward(12.5)
    t2.right(90)
    t2.forward(40)
    t2.end_fill()
#door
    
    t2.up()
    t2.goto(-558,-250)
    t2.seth(90)
    t2.down()
    t2.pencolor("BLACK")
    t2.fillcolor("#A91B1B")
    t2.begin_fill()
    t2.forward (30)
    t2.left(90)
    t2.forward (20)
    t2.left(90)
    t2.forward (30)
    t2.left(90)
    t2.forward (20)
    t2.end_fill()
    
    
    #window
    t2.up()
    t2.color("#9EB2B7")
    t2.goto(-555,-210)
    t2.seth(90)
    t2.down()
    #t2.fillcolor("black")
    t2.begin_fill()
    t2.forward(20)
    t2.right(90)
    t2.forward(20)
    t2.right(90)
    t2.forward(20)
    t2.right(90)
    t2.forward(20)
    t2.end_fill()
    
    t2.up()
    t2.goto(-595,-210)
    t2.seth(90)
    t2.down()
    #t2.fillcolor("black")
    t2.begin_fill()
    t2.forward(20)
    t2.right(90)
    t2.forward(20)
    t2.right(90)
    t2.forward(20)
    t2.right(90)
    t2.forward(20)
    t2.end_fill()
    
  

############## snowflakes##############3
def snowflakes(x,y):
    for i in range (10):
        t.up()
        t.goto(x,y)
        t.down()
        t.color("white")
        for i in range (10):
            for i in range (2):
                t.forward(5)
                t.right(60)
                t.forward(5)
                t.right(120)
            t.right(36)
        x=random.randint(-600,600)#random x #random numbers
        y=random.randint(-600,500)#random y

#sledge with snowman
turtle.delay(0)
def sledgesnowman(x):
    turtle.delay(0)
    t4.clear()
    t4.color("brown")
    t4.width("10")
    t4.seth(0)
    t4.up()
    t4.goto(-300+x,105)
    t4.down()
    t4.forward(350)#bottom line
    t4.backward(100)
    t4.left(90)
    t4.width("7")
    t4.forward(30)
    t4.backward(30)
    t4.left(90)
    t4.forward(150)
    t4.right(90)
    t4.forward(30)
    t4.right(90)
    t4.begin_fill()
    t4.width("1")
    t4.forward(200)
    t4.backward(225)

    t4.left(135)
    t4.forward(90)
    t4.seth(0)
    t4.forward(120)

    t4.right(65)
    t4.forward(40)
    t4.seth(0)
    t4.forward(120)
    t4.left(100)
    t4.forward(40)
    t4.seth(0)
    t4.forward(20)
    t4.right(75)
    t4.forward(68)
    t4.seth(180)
    t4.forward(200)
    t4.end_fill()

def other_stuff(x):
    #face
    t4.width("1")
    t4.color("salmon1")
    t4.begin_fill()
    t4.up()
    t4.goto(-100+x,250)
    t4.down()
    t4.circle(20)
    t4.end_fill()
    #hat
    t4.color("red")
    t4.begin_fill()
    t4.up()
    t4.goto(-115+x,240)
    t4.down()
    t4.right(125)
    t4.forward(45)
    t4.seth(280)
    t4.forward(45)
    t4.seth(160)
    t4.forward(40)
    t4.end_fill()

    t4.color("white")
    t4.begin_fill()
    t4.up()
    t4.goto(-88+x,282)
    t4.down()
    t4.circle(7)
    t4.end_fill()
    #eyes
    t4.up()
    t4.goto(-105+x,235)
    t4.down()
    t4.color("black")
    t4.begin_fill()
    t4.circle(3)
    t4.up()
    t4.goto(-90+x,230)
    t4.down()
    t4.circle(3)
    t4.end_fill()

    #smile
    t4.up()
    t4.goto(-97+x,220)
    t4.down()
    t4.seth(180)
    t4.width("3")
    turtle.delay(0)
    for x in range (2):
        t4.forward(5)
        t4.right(35)
    turtle.delay(0)
    
    #shirt
    t4.color("red")
    t4.width("1")
    t4.up()
    t4.goto(25+x,210)
    t4.down()
    t4.begin_fill()
    t4.backward(25)
    t4.left(90)
    t4.forward (5)
    t4.right(90)
    t4.forward(15)
    t4.seth(90)
    t4.backward(15)
    t4.left(90)
    t4.forward (20)
    t4.right(90)
    t4.forward(15)
    t4.left(145)
    t4.forward(15)
    t4.right(90)
    t4.forward(5)
    t4.right(90)
    t4.forward(25)
    t4.end_fill()

    #pant
    t4.up()
    t4.goto(23+x,190)
    t4.down()
    t4.color("red")
    t4.begin_fill()
    t4.seth(270)
    t4.forward(28)
    t4.right(90)
    t4.forward(7)
    t4.right(90)
    t4.forward(28)
    t4.left(90)
    t4.forward(3)
    t4.left(90)
    t4.forward(28)
    t4.right(90)
    t4.forward(7)
    t4.right(90)
    t4.forward(28)
    t4.end_fill()

    t4.color("white")
    t4.up()
    t4.goto(2+x,190)
    t4.down()
    t4.width("3")
    t4.right(90)
    t4.forward(25)
    t4.backward(11.5)
    t4.left(90)
    t4.forward(20)
    
    #left hand
    t4.up()
    t4.goto(-8+x,188)
    t4.down()
    t4.width("5")
    t4.color("salmon1")
    t4.goto(-11+x,184)
    #right hand
    t4.up()
    t4.goto(32+x,188)
    t4.down()
    t4.goto(35+x,184)

    #beard
    t4.up()
    t4.goto(40+x,220)
    t4.down()
    t4.color("white")
    t4.begin_fill()
    t4.circle(5)
    t4.goto(35+x,215)
    t4.circle(5)
    t4.goto(30+x,210)
    t4.circle(5)
    t4.goto(25+x,210)
    t4.circle(5)
    t4.goto(20+x,210)
    t4.circle(5)
    t4.goto(15+x,215)
    t4.circle(5)
    t4.end_fill()

    t4.begin_fill()
    t4.goto(10+x,215)
    t4.circle(5)
    t4.goto(8+x,220)
    t4.circle(5)
    t4.goto(5+x,225)
    t4.circle(5)
    t4.end_fill()
   
    #gift bag
    turtle.delay(0)
    t4.up()
    t4.goto(-20+x,160)
    t4.down()
    t4.color("black")
    t4.begin_fill()
    t4.seth(110)
    for x in range(110):
        t4.forward(1)
        t4.left(0.75)
    t4.left(90)
    t4.forward(7)
    t4.color("black")
    t4.left(70)
    t4.forward(30)
    t4.right(70)
    t4.forward(35)
    t4.end_fill()

    t4.up()
    t4.goto(-200+x,200)
    t4.down()
    t4.seth(180)
    t4.left(30)
    t4.forward(20)
    t4.backward(18)

    t4.right(30)
    t4.forward(20)
    t4.backward(18)
    t4.right(30)
    t4.forward(20)
    t4.backward(18)
    t4.right(30)
    t4.forward(25)
    t4.backward(18)
    t4.color("red")
    t4.left(190)
    t4.forward(10)

    #the deer pic
    turtle.delay(0)
    screen=t5.getscreen()
    screen.register_shape("Capture1.GIF")
    t5.penup()
    t5.shape("Capture1.GIF")
    t5.goto(175+x,190)

    #ropes
    t4.up()
    t4.goto(-23+x,165)
    t4.seth(0)
    t4.down()
    t4.width("3")
    t4.color("black")
    t4.forward(173)

    t4.up()
    t4.goto(-20+x,190)
    t4.seth(0)
    t4.down()
    t4.width("3")
    t4.color("black")
    t4.forward(163)

############winking snowman (right eye)###########
def winking_snowman():
    turtle.delay(10)
    t3.up()
    t3.goto(-335,-138)
    t3.down()
    t3.width("1")
    t3.color("white")
    t3.begin_fill()
    t3.circle(5)
    t3.end_fill()

    turtle.delay(50)#delays the winking
    t3.speed(0)#increases the speed
    t3.up()
    t3.goto(-335,-140)
    t3.down()
    t3.width("1")
    t3.color("black")
    t3.begin_fill()
    t3.circle(5)
    t3.end_fill()
    
############light the window############
def light_window():
    turtle.delay(10)
    t2.up()
    t2.goto(-555,-210)
    t2.seth(90)
    t2.down()
    t2.fillcolor("yellow")
    t2.begin_fill()
    t2.forward(20)
    t2.right(90)
    t2.forward(20)
    t2.right(90)
    t2.forward(20)
    t2.right(90)
    t2.forward(20)
    t2.end_fill()
    
    t2.up()
    t2.goto(-595,-210)
    t2.seth(90)
    t2.down()
    t2.fillcolor("yellow")
    t2.begin_fill()
    t2.forward(20)
    t2.right(90)
    t2.forward(20)
    t2.right(90)
    t2.forward(20)
    t2.right(90)
    t2.forward(20)
    t2.end_fill()

############smoke##############
def smoke(x,y,z):
    turtle.delay(50)
    t6.clear()
    for i in range (10):
        turtle.delay(0)
        t6.up()
        t6.color("gray60")
        t.seth(0)
        t6.goto(x,y)
        t6.down()
        t6.width("6")  
        t6.circle(12-z)
        t6.right(20)
        x=x-10
        y=y+5
        z=z+1
    
################calling######
##hills##
x=-390
y= -340
hill(x,y)

x=-300
y= -360
hill(x,y)

x=-150
y= -380
hill(x,y)

x=0
y= -390
hill(x,y)

x=200
y= -385
hill(x,y)

x=350
y= -385
hill(x,y)

x=500
y= -385
hill(x,y)

##trees##
t.seth(270)
x=500
y=-295
turtle.delay(0)
for i in range(3):
    trees(x,y)
    y=y-5
    x=x-100

x=-500
y=-250
for i in range(2):
    small_trees(x,y)
    x=x+20
    y=y-5





##house###
house()
##snowman##
snowman()
##snowflakes##
x=500
y=400
for i in range (10):
    turtle.delay(0)
    snowflakes(x,y)

##sleigh##
x=-400
turtle.delay(0)
for i in range(26):
    turtle.delay(0)
    sledgesnowman(x)
    x=x+20
other_stuff(x)
##winking snowman##
for i in range(5):
    winking_snowman()

##light window##
light_window()
##smoke##
for i in range(10):
    x=-530
    y=-100
    z=0
    t6.color("gray60")
    t6.begin_fill 
    smoke(x,y,z)
    t6.end_fill
    




import turtle
import math
import random

##Arkaplan
lcd = turtle.Screen()
lcd.bgpic('giphy1.gif')
lcd.tracer(2)


screen = turtle.Screen()
screen2 = turtle.Screen()
screen3 = turtle.Screen()
image1 = "pac.gif"
screen.addshape(image1)
image2 = "yem.gif"
screen2.addshape(image2)
image3 = "yem2.gif"
screen3.addshape(image3)



##Imlec isareti
tik = turtle.Turtle()
tik.color("gold")
tik.shape('turtle')
tik.pu()

##Cerceve
kalem = turtle.Turtle()
kalem.speed(10)
kalem.color("white")
kalem.pu()
kalem.setposition(-400,-400)
kalem.pd()
kalem.pensize(10)
for i in range(4):
    kalem.fd(800)
    kalem.left(90)
kalem.hideturtle()


skor = 0
can = 3
kalem2 = turtle.Turtle()



maxPuanlar =5 
puan = [ ]
ceza = [ ]

##Puanlar
for sayac in range(maxPuanlar):
    puan.append(turtle.Turtle())
    puan[sayac].speed(1)
    puan[sayac].shape("yem.gif")
    puan[sayac].pu()
    puan[sayac].setposition(random.randint(-400, 400), random.randint(-400, 400))


for sayac in range(maxPuanlar):
    ceza.append(turtle.Turtle())
    ceza[sayac].speed(1)
    ceza[sayac].shape("yem2.gif")
    ceza[sayac].pu()
    ceza[sayac].setposition(random.randint(-400, 400), random.randint(-400, 400))






speed =1


def hizartir():
    global speed
    speed+=1

def hizazalt():
    global speed
    speed-=1

def sol():
    tik.left(30)

def sag():
    tik.right(30)

def carpisma(c1,c2):
    a = math.sqrt(math.pow(c1.xcor()-c2.xcor(),2) + math.pow(c1.ycor()-c2.ycor(),2))
    if a < 20:
        return True;
    else:
        return False;


turtle.listen()
turtle.onkey(sol, "Left"   )
turtle.onkey(sag, "Right")
turtle.onkey(hizartir, "Up")
turtle.onkey(hizazalt, "Down")


##DONGU
while True:
    tik.forward(speed)


    if tik.xcor() > 400 or tik.xcor() <-400:
        tik.right(180)
        
    if tik.ycor() > 400 or tik.ycor() <-400:
        tik.right(180)

    ##yem hareketi

    for sayac in range(maxPuanlar):
        puan[sayac].fd(6)

        if puan[sayac].xcor() > 390 or puan[sayac].xcor() <-390:
            puan[sayac].right(150)
            
        if puan[sayac].ycor() > 390 or puan[sayac].ycor() <-390:
            puan[sayac].right(150)

        if carpisma(tik,puan[sayac]):
            puan[sayac].setposition(random.randint(-400, 400), random.randint(-400, 400))
            puan[sayac].right(random.randint(0,360))
            skor += 10
            kalem.undo()
            kalem.pu()
            kalem.hideturtle()
            kalem.setposition(-390, 410)
            skoryazi = "Skorun: %s" %skor
            kalem.write(skoryazi, False , align="left", font=("Arial",14,"normal"))



    for sayac in range(maxPuanlar):
        ceza[sayac].fd(6)

        if ceza[sayac].xcor() > 390 or ceza[sayac].xcor() <-390:
            ceza[sayac].right(150)
            
        if ceza[sayac].ycor() > 390 or ceza[sayac].ycor() <-390:
            ceza[sayac].right(150)

        if carpisma(tik,ceza[sayac]):
            ceza[sayac].setposition(random.randint(-400, 400), random.randint(-400, 400))
            ceza[sayac].right(random.randint(0,360))
            can -=1
            kalem2.undo()
            kalem2.pu()
            kalem2.hideturtle()
            kalem2.setposition(-200, 410)
            canyazi = "Can: %s" %can
            kalem2.write(canyazi, False , align="left", font=("Arial",14,"normal"))
            
    if can==0:
        kalem2.undo()
        kalem2.pu()
        kalem2.hideturtle()
        kalem2.setposition(-200, 410)
        canyazi = "OYUN BITTI"
        kalem2.write(canyazi, False , align="left", font=("Arial",14,"normal"))
        break;












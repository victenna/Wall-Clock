import turtle
wn=turtle.Screen()
wn.bgcolor("lightblue")
import time
turtle.tracer(2)

# Clock Face

TEXT_FONT=('Arial',30,'bold')
digit=turtle.Turtle()
digit.up()
digit.hideturtle()
digit.color('black')
digit.goto(-12,205)
#digit.write(12,font=TEXT_FONT)
for q in range (12):
    digit.circle(-230,30)
    digit.write(1+q,font=TEXT_FONT)
    #t0.stamp()


t0 = turtle.Turtle('square')
t0.up()
t0.color('blue')
t0.shapesize(4,0.5)
t0.goto(0,150)
t0.stamp()

for i in range (11):
    t0.circle(-150,30)
    t0.stamp()

#--------------------------------------
# Hour Hand
t1=turtle.Turtle('triangle')

t1.goto(0,0)
t1.color('red')
t1.pensize(8)
t1.hideturtle()
#---------------------------
# Minute Hand
t2=turtle.Turtle('triangle')
t2.goto(0,0)
t2.color('red')
t2.pensize(6)
t2.hideturtle()

#-------------------------
#Second Hand
t3=turtle.Turtle('square')
t3.color('gold')
t3.pensize(4)
t3.hideturtle()

def sec_angle(angle):
    t3.setheading(angle+90)
    t3.fd(180)
    t3.fd(-180)
    time.sleep(1)
    t3.clear()
            
#---------------------------------            
#Point (0,0)
t4=turtle.Turtle('circle')

#----------------------------
while True:
   
    #Time
    time_hour=time.strftime("%H")
    time_min=time.strftime("%M")
    time_sec=time.strftime("%S")
    t_s=int(time_sec)
    t_h=int(time_hour)
    tt1=t_h%12 #round every 12 hourss
    angle_hour=tt1*30 #hour in degrees

    t_m=int(time_min)
    angle_minute=t_m*6 # minutes in degrees
    print('angle_minute=', angle_minute/6)
    print(t_h,t_m)
    angle_hour=angle_hour+angle_minute/12
    print('angle_hour=', angle_hour)
       
    #Hour arrow
    t1.setheading(-angle_hour+90)    
    t1.fd(90)
    t1.fd(-90)
    
    #----------------------------------------
    #Minute Arrow
    t2.setheading(-angle_minute+90)
    t2.fd(110)
    t2.fd(-110)
   
    #--------------------
    m=0
    #Second Arrow
    for m in range (60):
        sec_angle(-6*m)
        if m==59:
            t1.clear()
            t2.clear()
        
    #Central point
    t4.goto(0,0)
    #---------------------------------
   
    


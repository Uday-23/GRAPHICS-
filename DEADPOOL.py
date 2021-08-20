#DEADPOOL
from turtle import *
import time
color('red')
penup()
goto(0, -200)
pendown()
begin_fill()  
circle(200) 
end_fill()
def black_circle():
   begin_fill()
   color('black')
   circle(160, -160)
   end_fill()

goto(0, -160)
circle(160, -10)
black_circle()

color('red')

goto(25, 160)
rt(20)
black_circle()
def eye(a):
    begin_fill()
    goto(a * 40, 0)
    color('white')
    pendown()
    goto(a * 140, 45)
    goto(a * 120, 10)
    goto(a * 40, 0)
    end_fill()
    penup()

eye(1)      
eye(-1)     

hideturtle()
time.sleep(8)




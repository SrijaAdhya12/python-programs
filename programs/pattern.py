import turtle
from time import sleep
s=turtle.getscreen()
t=turtle.Turtle()
t.right(90)
t.forward(100)
t.left(90)     
t.forward(100) 
t.right(90)    
t.left(90)           
t.left(90)
t.forward(100)
t.right(90)    
t.right(90)       
t.left(90)        
t.right(90)    
t.left(90)
t.right(90)    
t.right(90)
t.forward(100)
t.home()

colors = ["blue","red"]
i=0
while i<100:
    turtle.bgcolor(colors[i %2])
    i+=1
    sleep(.4)
turtle.done()    
    
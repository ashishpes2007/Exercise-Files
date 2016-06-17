import turtle

def draw_art():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    
def draw_square(some_turtle):
    i = 0
    while(i<4):
        some_turtle.forward(100)
        some_turtle.right(90)
        i = i+1
        
#def draw_circle():
 #   angie = turtle.Turtle()
  #  angie.shape("arrow")
   # angie.color("blue")
    #angie.circle(100)
    
#def draw_triangle():
 #   leo = turtle.Turtle()
  #  leo.right(120)
   # leo.forward(150)
    #leo.right(120)
    #leo.forward(150)
    #leo.right(120)
    #leo.forward(150)
    
window = turtle.Screen()
window.bgcolor("red")

draw_art()
#draw_circle()
#draw_triangle()
window.exitonclick()







    




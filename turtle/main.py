import turtle

larry = turtle.Turtle()

larry.shape("turtle")
larry.pensize(3)


#telhado
larry.forward(100)
larry.left(120)
larry.forward(100)
larry.left(120)
larry.forward(100)
larry.left(120)
larry.forward(200)
larry.left(90)
larry.forward(87)
larry.left(90)
larry.forward(150)
larry.penup()
larry.forward(10)

#janela
larry.left(90)
larry.penup()
larry.forward(70)
larry.pendown()
larry.circle(10)
larry.left(90)
larry.forward(20)
larry.penup()
larry.left(180)
larry.forward(5)
larry.pendown()
larry.forward(5)
larry.left(90)
larry.forward(10)
larry.left(180)
larry.forward(20)

#paredes
larry.penup()
larry.home()
larry.pendown()
larry.right(90)
larry.forward(100)
larry.left(90)
larry.forward(100)
larry.left(90)
larry.forward(100)
larry.left(180)
larry.penup()
larry.forward(100)
larry.pendown()
larry.right(270)
larry.forward(100)
larry.left(90)
larry.forward(100)

#portas
larry.penup()
larry.home()
larry.right(90)
larry.forward(100)
larry.left(90)
larry.forward(60)
larry.left(90)
larry.pendown()
larry.forward(30)
larry.left(90)
larry.forward(20)
larry.left(90)
larry.forward(30)
larry.penup()
larry.home()
larry.right(90)
larry.forward(100)
larry.left(90)
larry.forward(160)
larry.left(90)
larry.pendown()
larry.forward(30)
larry.left(90)
larry.forward(20)
larry.left(90)
larry.forward(30)

turtle.done



'''
for i in ['red', 'orange' , 'black' , 'green', 'yellow', 'blue', 'purple']:
  larry.color (i)
  larry.forward(100)
  larry.stamp()
  larry.right(100)
  larry.forward(100)
  larry.left(150)
  larry.stamp()

turtle.done

'''

'''
for c in ['red', 'green', 'yellow', 'blue']:
    t.color(c)
    t.forward(75)
    t.left(90)
'''
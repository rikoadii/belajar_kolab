import turtle

# Buat objek turtle
t = turtle.Turtle()

# Buat kepala Spiderman
t.color("red")
t.begin_fill()
t.circle(50)
t.end_fill()

# Buat mata Spiderman
t.color("white")
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
t.goto(-15, 50)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

# Buat tubuh Spiderman
t.color("blue")
t.penup()
t.goto(0, -50)
t.pendown()
t.begin_fill()
t.circle(50, 180)
t.left(90)
t.forward(100)
t.left(90)
t.circle(50, 180)
t.end_fill()

# Buat tangan Spiderman
t.color("red")
t.penup()
t.goto(-75, -10)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(75, -10)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

# Buat kaki Spiderman
t.color("blue")
t.penup()
t.goto(-35, -100)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(35, -100)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

# Tampilkan gambar
turtle.done()

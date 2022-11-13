from turtle import Turtle
class Gun(Turtle):
    def __init__(self):
        super().__init__()
        self.createGun()
        self.create_bullet()

    def createGun(self):
         self.gun = Turtle()
         self.gun.shape("square")
         self.gun.color("white")
         self.gun.penup()
         self.gun.shapesize(stretch_wid=1, stretch_len=3)
         self.gun.goto(x=0, y=-280)

    def create_bullet(self):
        self.bullet = Turtle()
        self.bullet.shape("circle")
        self.bullet.color("red")
        self.bullet.penup()
        x =self.gun.xcor()

        self.bullet.goto(x=x, y=-260)

    def move_bullet_left(self):
        x = self.gun.xcor()

        self.bullet.goto(x=x, y=-260)

    def move_bullet_right(self):
        x = self.gun.xcor()
        self.bullet.goto(x=x, y=-260)

    def fire_bullet(self):
        self.bullet.setheading(90)
        self.bullet.forward(30)


    def move_left(self):
        self.gun.backward(10)
        self.move_bullet_left()

    def move_right(self):
      self.gun.forward(10)
      self.move_bullet_right()
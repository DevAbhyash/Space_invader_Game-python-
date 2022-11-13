from turtle import Turtle
position = [(-200,300),(-150,300),(-100,300),(-50,300),(0,300),(50,300),(100,300),(150,300)]
class Enemy(Turtle):
    def __init__(self):
     super().__init__()
     self.enemy = []
     self.create_enemy()


    def create_enemy(self):
     for i in range(len(position)):
       enemy = Turtle()
       enemy.shape("turtle")
       enemy.color("white")
       enemy.penup()
       enemy.setheading(90)
       enemy.goto(position[i])
       self.enemy.append(enemy)





    def move_enemy(self):
        for e in self.enemy:
         e.backward(5)

    def delete(self, id):
      self.enemy[id].reset()


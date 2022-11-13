import turtle
from gun import Gun
from enemy import Enemy


from turtle import Turtle
screen = turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.listen()

gun = Gun()
enemy = Enemy()
enemy_array=enemy.enemy

screen.onkey(gun.move_left,"Left")
screen.onkey(gun.move_right,"Right")
game_is_on = True
while game_is_on:
    gun.fire_bullet()
    enemy.move_enemy()

    for ene in range(len(enemy.enemy)):
      if gun.bullet.distance(enemy.enemy[ene]) < 15:
          enemy.delete(ene)

      if enemy.enemy[ene].ycor() <-280:
          game_is_on =False






screen.exitonclick()
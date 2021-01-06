import pyxel
from random import randint

class BouncingBall:
    def __init__(self):
        self.x = randint(0, 100)
        self.y = randint(0, 100)
        self.speed = randint(1, 5)
        self.dx = self.speed
        self.dy = self.speed
        self.color = randint(1, 15)
        self.radius = randint(1, 10)

    def update(self):
        self.x += self.dx
        self.y += self.dy

        if self.x > pyxel.width:
            self.dx = -self.speed
        if self.x < 0:
            self.dx = self.speed
        if self.y > pyxel.height:
            self.dy = -self.speed
        if self.y < 0:
            self.dy = self.speed

balls = []
for _ in range(20):
    balls.append(BouncingBall())

def draw():
    pyxel.cls(0)
    for b in balls:
        pyxel.circ(b.x, b.y, b.radius, b.color)

def update():
    for b in balls:
        b.update()





pyxel.init(120, 180)
pyxel.run(update, draw)
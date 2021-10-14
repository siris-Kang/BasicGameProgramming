from math import sqrt
import cocos
import cocos.collision_model as cm
import cocos.euclid as eu
import random

from collections import defaultdict
from pyglet.window import key

class Actor(cocos.sprite.Sprite):
    def __init__(self, x, y, color):
        super(Actor, self).__init__('ball.png', color=color)
        self.position = pos = eu.Vector2(x, y)
        self.cshape = cm.CircleShape(pos, self.width/2)

        self.direction = None

class MainLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(MainLayer, self).__init__()
        self.player = Actor(320, 240, (0, 0, 255))
        self.add(self.player)
        for pos in [(100,100), (540,380), (540,100), (100,380)]:
            self.add(Actor(pos[0], pos[1], (255, 0, 0)))

        cell = self.player.width * 1.25
        self.collman = cm.CollisionManagerGrid(0, 640, 0, 480, cell, cell)
        self.speed = 100.0
        self.pressed = defaultdict(int)
        self.schedule(self.update)

    def on_key_press(self, k, m):
        self.pressed[k] = 1

    def on_key_release(self, k, m):
        self.pressed[k] = 0
       

    def update(self, dt):
        self.collman.clear()
        for _, node in self.children:
            self.collman.add(node)
        for other in self.collman.iter_colliding(self.player):
            other.position = (random.randint(10, 630),random.randint(10, 470))
            other.cshape.center[0] = other.position[0]
            other.cshape.center[1] = other.position[1]

        for _, node in self.children:
            pos = node.position
            if node is not self.player:
                change = random.randint(0, 50)
                if change == 0 or node.direction is None:
                    x = random.random() - 0.5
                    y = random.random() - 0.5
                    size = sqrt(x**2 + y**2)
                    x = x/size
                    y = y/size
                    node.direction = [x, y]
            else: 
                x = self.pressed[key.RIGHT] - self.pressed[key.LEFT]
                y = self.pressed[key.UP] - self.pressed[key.DOWN]
                node.direction = [x, y]
            new_x = pos[0] + self.speed * node.direction[0] * dt
            new_y = pos[1] + self.speed * node.direction[1] * dt
            
            if new_x < 0:
                new_x = 639
            if new_y < 0:
                new_y = 479
            if new_x >= 640:
                new_x = 0
            if new_y >= 480:
                new_y = 0

            node.position = (new_x, new_y)
            node.cshape.center[0] = node.position[0]
            node.cshape.center[1] = node.position[1]


if __name__ == '__main__':
    cocos.director.director.init(caption='Hello, Cocos')
    layer = MainLayer()
    scene = cocos.scene.Scene(layer)
    cocos.director.director.run(scene)
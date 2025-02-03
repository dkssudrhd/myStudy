class Enemy :
    def __init__(self, width, height, pos_x, pos_y, speed):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed

    def move(self):
        self.pos_y += self.speed
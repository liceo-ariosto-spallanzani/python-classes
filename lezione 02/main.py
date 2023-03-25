class Monster:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == "up" and self.y > 0:
            self.y -= 1
        elif direction == "down":
            self.y += 1
        elif direction == "left" and self.x > 0:
            self.x -= 1
        elif direction == "right":
            self.x += 1

    def print_pos(self):
        print(self.x, self.y)

m1 = Monster(0, 0)
m1.print_pos() # 0 0
m1.move("right")
m1.print_pos() # 1 0
m1.move("left")
m1.print_pos() # 0 0
m1.move("up")
m1.print_pos() # 0 0 (non si può andare più in alto di 0)
m1.move("down")
m1.print_pos() # 0 1
m1.move("up")
m1.print_pos() # 0 0

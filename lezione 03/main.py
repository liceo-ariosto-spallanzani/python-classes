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

class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.monsters = []
    
    def print(self):
        out = ""
        for y in range(self.height):
            for x in range(self.width):
                out += "[ ]"

            out += "\n"
        print(out)

level = Level(5, 5)
m1 = Monster(0, 0)
level.monsters.append(m1)
level.print()

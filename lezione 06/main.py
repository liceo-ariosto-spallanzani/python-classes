import os 
from random import choice

def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

class Entity:
    def __init__(self, x, y, level, icon):
        self.x = x
        self.y = y
        self.level = level
        self.icon = icon

    def print_pos(self):
        print(self.x, self.y)

class MovingEntity(Entity):
    def __init__(self, x, y, level, icon):
        super().__init__(x, y, level, icon)

    def move(self, direction):
        if direction == "up":
            self.y -= 1
        elif direction == "down":
            self.y += 1
        elif direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1

        if self.y < 0:
            self.y = level.height -1
        elif self.y > level.height -1:
            self.y = 0
        
        if self.x < 0:
            self.x = level.width -1
        elif self.x > level.width -1:
            self.x = 0

class Monster(MovingEntity):
    def __init__(self, x, y, level):
        super().__init__(x, y, level, "M")

class Player(MovingEntity):
    def __init__(self, x, y, level):
        super().__init__(x, y, level, "P")

class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.entities = []
    
    def print(self):
        out = ""
        for y in range(self.height):
            for x in range(self.width):
                for e in self.entities:
                    if x == e.x and y == e.y:
                        out += "[" + e.icon + "]"
                        break
                else:
                    out += "[ ]"
    
            out += "\n"
        print(out)


level = Level(5, 5)

m1 = Monster(3, 3, level)
p = Player(3, 4, level)

level.entities.append(m1)
level.entities.append(p)

command = ""
while command != "q":
    clear()
    level.print()

    command = input("usa wasd per muoverti o q per uscire\n").lower()

    if command == "w":
        p.move("up")
    elif command == "a":
        p.move("left")
    elif command == "s":
        p.move("down")
    elif command == "d":
        p.move("right")
    
    m1.move(choice(["up", "down", "left", "right"]))

import os 

def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

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
                for monster in self.monsters:
                    if x == monster.x and y == monster.y:
                        out += "[M]"
                        break
                else:
                    out += "[ ]"
    
            out += "\n"
        print(out)


level = Level(5, 5)
m1 = Monster(3, 3)
level.monsters.append(m1)

command = ""
while command != "q":
    clear()
    level.print()

    command = input("usa wasd per muoverti o q per uscire\n").lower()

    if command == "w":
        m1.move("up")
    elif command == "a":
        m1.move("left")
    elif command == "s":
        m1.move("down")
    elif command == "d":
        m1.move("right")
        

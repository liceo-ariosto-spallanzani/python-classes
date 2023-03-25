from random import randint

class Monster:
  def __init__(self, name):
    self.name = name
    self.max_hp = randint(10, 50)
    self.cur_hp = self.max_hp
    self.dmg = randint(10, 30)
    self.alive = True

  def print_stats(self): 
    print(self.name, self.cur_hp, "/", self.max_hp, self.dmg)

  def kill(self, target):
    if self.alive == False:
        print(self.name, "non può attaccare da morto")
        return

    if target.alive == False:
        print(target.name, "è morto, non infierire")
        return
    
    print(self.name, "attacca", target.name, "facendogli", self.dmg, "danni")
    target.cur_hp -= self.dmg
    if target.cur_hp <= 0:
        target.alive = False 
        print(target.name, "è morto")

x = 1
y = "ciao mare"
m1 = Monster("John")
m2 = Monster("Zorro")

for i in range(4):
  m1.print_stats()
  m2.print_stats()
  m1.kill(m2)
  m2.kill(m1)

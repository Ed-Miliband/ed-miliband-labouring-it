class Person: #Applies to all
  def __init__(self):
    self.health = 100
    self.level = 5
    self.power = 10
    self.attack = 20
    self.defense = 10
    self.abilities = []
    self.critMultiplier = 1

class Player(self, Person):
  def __init__(self):
    self.inventory = [ ] 

class AttDef: #AttackDefense
  def __init__(self):
    return
  def Attack(level, power, attack, crit):
    d1 = ((2*level*crit)+2)/5
    damage = ((d1*power*attack)/50)+2
    return damage
  def Defense(level, power, defense, crit):
    d2 = ((2*level*crit)+2)/5
    damage = ((d2*power*defense)/50)+2
    return damage
  
  
    

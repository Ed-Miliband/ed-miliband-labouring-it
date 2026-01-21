import json

class BillyBob: #Applies to the player
  def __init__(self):
    self.health = 100
    self.level = 5
    self.power = 10
    self.attack = 20
    self.defense = 10
    self.abilities = []
    self.critMultiplier = 1
    self.inventory = [ ] 
  def CheckInventory():
    print(self.inventory)

class AttDef: #AttackDefense
  def __init__(self):
    return
  def Attack(level, power, attack, crit):
    d1 = ((2*level*crit)+2)/5
    damage = ((d1*power*attack)/50)+2
    return damage
  def Defense(level, power, defense, crit):
    d2 = ((2*level*crit)+2)/5
    defense = ((d2*power*defense)/50)+2
    return defense
  def FinalDamage(damage, defense): #5 billion functions
    finalDamage = damage - defense
    return finalDamage

#Utility functions for JSON
def load_json(filepath):
    with open(filepath, "r") as f:
        return json.load(f)
      
def save_json(filepath, data):
    with open(filepath, "a") as f:
        json.dump(data, f, indent=4)
  
  
    

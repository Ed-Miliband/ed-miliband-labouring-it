import json
import abilities
import enemyComp
import loot

class BillyBob: #Applies to only the player, companion+enemy data in json files
  def __init__(self):
    self.maxHealth = 100
    self.health = 100
    self.level = 5
    self.experience = 0
    self.power = 10
    self.defense = 10
    self.abilities = []
    self.critMultiplier = 1
    self.inventory = [ ] 

    def Healing(maxHealth, healMultiplier):
      healAmount = maxHealth * healMultipler
      return healAmount
    
  def CheckInventory():
    print(self.inventory)
  def AddtoInventory(item):
    self.inventory.append(item)
  def RemovefromInventory():
    item = input()
    self.inventory.remove(item)

  def SortInventory(inventory): #merge sort
    if len(inventory} > 1:
      mid len(inventory)/2
      lefthalf = inventory[:mid]
      righthalf = inventory[mid:]
      sortInventory(righthalf)
      sortInventory(lefthalf)
      i = 0
      j = 0
      k = 0
      while i < len(lefthalf) amd j < len(righthalf):
      if lefthalf[i] < righthalf[j]:
        inventory[k] = lefthalf[i]
      else:
        inventory[k] = righthalf[i]
        j += 1
      while j < len(righthalf):
        inventory[k] = righthalf[j]
        j = j+1
        k = k+1
      

class AttDef: #AttackDefense
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

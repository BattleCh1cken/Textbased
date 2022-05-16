'''Player_Custom
  Inputs: None
  Outputs: None
  Prints: Welcome and End Screen
  *** means add feature in the future
'''

Title="Textbased"
wins=0
loses=0
class starting:
  def __init__(self):
    self.playername = input("What is your name: ")
    print("Welcome to",Title,",",self.playername,"!")
    normalending.__init__(self)
  def getname(self) -> str:
    return self.playername
    
class normalending:
  def __init__(self):
    print("End of Start")
    print("Player:",starting.getname(self),"\n"," wins:",wins,"\n","loses:",loses)

class Player:
  def __init__(self):
    self.name = "placeholder"
    self.level = 42
    self.damage = 42
    self.health = 100
    self.healthMax = 100
    self.weapon = Weapon("basicSword", 22)
  def equipWeapon(self, weapon):
    self.weapon = weapon
  
  def calcDamage(self):
    self.damage = self.weapon.power
    print(self.damage)
    
    
    

class Weapon:
  def __init__(self, name, power):
    self.name = name
    self.power = power

class Armour:
  def __init__(self, name, power):
    self.name = name
    self.power = power

player1 = Player()
print(player1.weapon.power)
sword = Weapon("basicSword", 42)
player1.equipWeapon(sword)
print(player1.weapon.power)
#We could calculate damage dealt based on the power of the weapon. We could also add stats like crit chance. Then we would then calculate final damage with the calculate damage method.
  

    
    
    
    
    

    
#Starting up the game
#starting()
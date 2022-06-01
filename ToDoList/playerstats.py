class Player:
  name = "placeholder"
  damage = 42
  health = 100
  healthMax = 100
  
  def __init__(self):
    print("init")
    
  def equipWeapon(self, weaponInput):
    print("weapon equiped")
  
  
    
    

    
#The weapon and armour should by in the class of item or just slap onto player cuz single calculation don't need self. self just give everything global access. Optimized player is prob going to be [final stats that we work with],[base stats(when they open their stats/inv page),[weapon and armour calculations],[inv],***[flavor text or something]] crate and cdmg are just modifier that can easily be added on with arrays for example 
    #pdmg:[[23(norm),90(crit)], [0.7,0.3]] 
    #after calling the dmg calculation(70% norm, 30% crit), it inputs into Hp_Bar and shows the dmg dealt
    #There are way worst ways
    # Please leave this comment here
    # So I can look at it later
    

#Lmao this is so much jankier than version control
#Its like google drive for code
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
'''Enemy_Generator
  Inputs: level of the player
  Outputs: Stats_List:[name,maxhp,dmg,***xp,***[drops],***[droprate]]
  Prints: EnemyStats(Del before game)
  *** means add feature in the future
'''
import random
#crit chance and dmg will be automatic added as a def function calcdmg(dmg) in the future code for dmg and player-mob interactions
#place is the location on the array[EnemyName] and generate a enemy based on location

place=0

def generate_enemy(level)-> list:
  #Types of Enemies
  EnemyType=[["Normal ",1,1],["Elite ",1.5,1.2],["High ",2,1.5],["King ",3,2]]
  EnemyName=[[["Slime",20,2],["Blob",25,1]],[["Goblin",50,5],["Bat",30,8]]]
  #Level Bonus
  lvbonus=level/5
  #Randomly Selection(enemytype is manualy changed so don't change the order of the list)  
  enemytype=random.choices(EnemyType,weights=[0.5,0.4,0.10,0.01])
  #Gets the List[List] that it input as one List
  etype=enemytype[0]
  #Choosing a random enemy in the first place(plains or something)
  temp=EnemyName[place]
  lst=random.choice(temp)
  
  #Add the two names together o make a cooler name
  lst[0]=etype[0]+lst[0]
  #HP: int
  lst[1]=int(etype[1]*lst[1]*(1+lvbonus))
  #Dmg: list(enemy have a fix cratio of 10%:150%)
  lst[2]=[int(etype[2]*lst[2]*(1+lvbonus)),0.1,1.5]
  
  return lst



#Level testing  
level=1
continued=0
while continued!="stop":
  print(generate_enemy(level))
  level+=1
  tryagain=input("Stop?  ")
  if level == 100:
    place = 1
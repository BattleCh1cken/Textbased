'''Enemy_Generator
  Inputs: level of the player
  Outputs: Stats_List:[name,maxhp,dmg,***xp,***[drops],***[droprate]]
  *** means add feature in the future
'''
import random
#crit chance and dmg will be automatic added as a def function calcdmg(dmg) in the future code for dmg and player-mob interactions
place=0


def generate_enemy(level)-> list:
  #Types of Enemies
  EnemyType=[["Normal ",1,1],["Elite ",1.5,1.2],["High ",2,1.5],["King ",3,2]]
  EnemyName=[[["Slime",20,2],["Blob",25,1]],[["Goblin",50,5],["Bat",30,8]]]
  #Level Bonus
  lvbonus=level/5
  #Randomly Selection(enemytype is manualy changed so don't change the order of the list)  
  enemytype=random.choices(EnemyType,weights=[0.5,0.4,0.10,0.01])
  etype=enemytype[0]
  temp=EnemyName[place]
  lst=random.choice(temp)
  lst[0]=etype[0]+lst[0]
  for i in range(1,3):
    lst[i]=int(etype[i]*lst[i]*(1+lvbonus))
  print("level:",level,"  level bonus:",str((1+lvbonus)*100)+"%")
  #append special stuff if i get to it
  return lst
  

#Level testing  
level=1
continued=0
while continued==0:
  enemy=generate_enemy(level)
  print(enemy)
  level+=1
  tryagain=input("Try again?")
  if level == 100:
    place = 1
  if tryagain=="stop":
    break
  


'''Hp_Bar
  Inputs: Stats_List, health left, final dmg
  Outputs: health left and 
  Prints: hp bar
  *** means add feature in the future
'''
from math import ceil
import random
#*** means in the future


def hp(stats:list, currhp:int, dmg:int)-> int:
  max=stats[1]
  currhp=currhp-dmg
  if currhp<0:
    currhp=0
  length_bar = 20
  #multiply x to represent hp
  hp = ceil(currhp / max * length_bar)
  bar = "=" * hp
  emptybar = " " * (length_bar - hp)
  #add bars together
  print(stats[0],"Hp:","["+bar+emptybar+"]")
  return currhp

enemy=["Test Dummy",100,0]
enemyhp=enemy[1]
loop=True
while loop==True:
  enemy=["Test Dummy",100,0]
  enemyhp=enemy[1]
  #generate_enemy(level)
  #enemyhp = hp(enemystats,enemyhp,dmg)
  enemyhp = hp(enemy,enemyhp,0)
  while enemyhp > 0:
    #dmg=int(input("Dmg dealt:"))
    dmg=random.randint(5,20)
    print("Bot deals",dmg,"damage")
    enemyhp = hp(enemy,enemyhp,dmg)
  print(enemy[0],"has been defeated")
  tryagain=input("Do you want to continue? [type 'stop']  ")
  if tryagain == "stop":
    loop=False



print("You have completed the tutorial!!!")


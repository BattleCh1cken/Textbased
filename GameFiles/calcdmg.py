import random
def finaldmg(dmg:list, defense:int)->int:
  #choice returns a list within a list so ()[0]
  cr=dmg[1]
  if cr>1:
    crate=[1,0]
  else:
    crate=[1-cr,cr]
  Final_dmg=(random.choices([dmg[0],dmg[0]*dmg[2]],crate))[0]
  Final_dmg=Final_dmg-defense
  #so the armor didn't block everything or should i do reductions
  if Final_dmg < 0:
    return 1
  return int(Final_dmg)
#Testing Function
#Tip: inputs dont mess with the input name in the def function
lst=[20,0.3,1.3]
Enemystats=["Slime",314,123,12]
defense=Enemystats[3]
testagain=""
while testagain != "stop":
  print(finaldmg(lst,defense),finaldmg(lst,defense),finaldmg(lst,defense),finaldmg(lst,defense),finaldmg(lst,defense))
  testagain = input("Type 'stop' to stop    ")
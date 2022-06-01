#Rainbow Graphics
import time
import replit
#fps of the color
delay=0.2
#inputs
print("Warning the following can't be ran on shell for \nit will go on for about",int((delay*300)/60),"minutes. \nSelect typing \n[l] letter by letter \n[f] full color change\n[e] exit code")
type=input("")
if type!="e":
  stuff=input("Rainbowized: ")
  color=["\033[31m","\033[33m","\033[93m","\033[92m","\033[34m","\033[36m","\033[35m"]
  lencolor=len(color)
  #actual code
  def rainbow(words:str,c:int)-> str:
    word=list(words)
    l=len(words)*2
    for i in range(0,l,2):
      if c == lencolor:
        c=0
      word.insert(i,color[c])
      c+=1
      
    return "".join(word)
  change=0
  
  #loading screen for fun
  def loading()->None:
    replit.clear()
    for dotnumber in range(0,4):
      print("loading"+("."*dotnumber))
      time.sleep(0.5)
      replit.clear()
  loading()
  
  if type == "l":
    for i in range(0,300):
      if change == lencolor:
        change=0
      replit.clear()
      print(rainbow(stuff,change))
      time.sleep(delay)
      change+=1
  elif (type == "f") or (type == ""):
    for i in range(0,300):
      if change == lencolor:
        change=0
      replit.clear()
      print(color[change],stuff,"\033[0m")
      time.sleep(delay)
      change+=1
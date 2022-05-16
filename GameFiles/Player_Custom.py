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
    
#Starting up the game
starting()
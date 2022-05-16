'''GuessingGame.py'''
import random


min=1
max=100
print("Pick a number between",min,"and",max)
guess = int(input("Your guess: "))

def guessNumber(guess):
    randomN = random.randint(min,max)
    sum = 0
    while guess != randomN:
      if (guess < min) or (guess > max):
          print("Not between",min,"and",max)
      elif guess > randomN:
          print ("Down")
          sum+=1
      elif guess < randomN:
          print ("Up")
          sum+=1
      guess = int(input("Your guess: "))   
    sum += 1
    print ("Congratulations, the number was " + str(randomN) + "! It took " + str(sum) + " tries!")

guessNumber(guess)
print("Would you want to try again? Yes or No")
again = input()
while again.casefold() == "yes":
  guess = int(input("Your guess: "))
  guessNumber(guess)
  print("Do you want to try again? Yes or No")
  again = input()
else:
  print("Exiting")
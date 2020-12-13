print("Enter number bewtween 1 and 9")
y = 2

maxchances = 5
chances = 0
while (chances <5):

 chances=chances+ 1

 x = input()
 y = 2
 if (x == y):
  print ("Congrats you won this game")
  exit
 elif x > y:
  print ("your guess is high try again")
 else :
  print ("your guess is low try again")
if(chances ==5):
  print (" Sorry you lost my game try again any time") 

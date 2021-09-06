'''
These functions are good practice with
lists, loops, input, and random
Each function is worth 5 points:
2 for trying, 2 for right direction, 1 for correct
'''
import random
#1) Returns the longer list
def get_longer_list(l1, l2):
  if len(l1)>len(l2):
    return l1
  else:
    return l2

#2) Returns the average of a list of numbers
def get_average(l):
  sum = 0
  for i in range(0, len(l)):
    sum = sum + l[i] 
  return sum/len(l)


#3) Count how many times my favorite song
#   appears in a playlist (use == for equals)
def count_favorite_song(playlist, song):
  total =  0
  for i in playlist: 
    if i == song:
      total = total + 1
  return total

#4) Change this function so the only valid inputs are
#   "A" "B" "C" or "D"
def multiple_choice():
  ans = input("Please input your answer:\n")
  
  while ans not in ["A","B","C","D"]:
    ans = input("Invalid response. Type A, B, C, or D.")
  
  print(ans)

#5) Fix this function so it runs correctly without bugs
def canVote():
  age = int(input("Please input your age:"))
  if age>=18:
    return True
  else:
    return False

#6) Returns True 30% of the time and False otherwise
#   Hint: Use randint
def chance30():
  x = random.randint(0,10)
  if x<=3:
    return True
  else:
    return False

#7) Turn this psuedocode into code
'''
randomly choose a number
while user hasn't guessed my number:
  ask user for guess and give appropriate message (too low, too high)
user success!
'''
def guess_my_number():
  myNumber = 349
  guess = int(input("Please guess a number:\n"))
  while guess != myNumber:
      if guess > myNumber:
        print("Lower...")
      else:
        print("Higher...")
      guess = int(input("Please guess a number:\n"))
  print("You got it, good job")

   


# Make sure to test your code below!!
guess_my_number()

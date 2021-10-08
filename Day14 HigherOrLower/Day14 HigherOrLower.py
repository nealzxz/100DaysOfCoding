#display logo
from art import logo
from art import vs
print(logo)

#random one choice
import random
from game_data import data
def grab():
  return random.choice(data)
def compare(a, b):
  if a > b:
    return 'l'
  elif a < b:
    return 'h'
  else:
    return 0
#ask a guess
def guess_hl():
  return input("h or l").lower()
#check answer
end_of_game = False

score = 0
a = grab()
b = grab()
while not end_of_game:
  print(f"{a['name']}: {a['description']} from {a['country']}")
  print(vs)
  print(f"{b['name']}: {b['description']} from {b['country']}")
  c = compare(a['follower_count'], b['follower_count'])
  guess = guess_hl()
  if c == guess:
    print("you are right!")
    score += 1
    print(f"Your score is {score}")
    a = b
    b = grab()
  else:
    print("you lose")
    print(f"Your score is {score}")
    end_of_game = True
  

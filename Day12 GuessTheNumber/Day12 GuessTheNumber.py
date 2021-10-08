#Number Guessing Game Objectives:
logo = """
   _____                     
  / ____|                    
 | |  __ _   _  ___  ___ ___ 
 | | |_ | | | |/ _ \/ __/ __|
 | |__| | |_| |  __/\__ \__ \
  \_____|\__,_|\___||___/___/
                             
                             
"""
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
print(logo)
import random
answer = random.randint(1, 100)

def choose_difficulty():
  s = ''
  while not s == 'easy' or s == 'hard':
    s = input("choose easy or hard")
    if s == 'easy':
      return 10
    elif s == 'hard':
      return 5
  
def check_answer(n,a):
  if n > a:
    print("too high")
  elif n < a:
    print("too low")
  else:
    print("you got it!")

lives = choose_difficulty()
guess = 0

while lives > 0 and guess != answer:
  guess = int(input("guess a number"))
  check_answer(guess, answer)
  lives -= 1





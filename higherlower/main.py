"""
This project is about Udemy day 14 challenge
SUPAR HARD!!! BUT REMEMBER THE MORE YOU STRUGGLE, THE SUPERIOR YOU BECOME

IN the game loop if the user gets the answer right, for the next question we have to set 'Compare B' as the A and a new 'B'
That's where I get stuck
I'm almost successful except this shit problem
"""

import art
from game_data import data
import random
import replit

def rand_account():
  randomly = random.choice(data)
  return randomly

def format(the_list: dict):
  datas = the_list
  name = datas['name']
  desc = datas['description']
  country = datas['country']
  return f"{name}, a {desc}, from {country}"

def get_count(rand_acc: dict):
  return rand_acc['follower_count']


def rightness(a_count, b_count, answer):
  if answer == 'a':
    if a_count > b_count:
      return 'right'
    else:
      return 'wrong'
  else:
    if b_count > a_count:
      return 'right'
    else:
      return 'wrong'


score = 0
print(art.logo)
while True:
  compare_a = rand_account()
  compare_b = rand_account()

  print(f'Compare A: {format(compare_a)}')
  print(art.vs)
  print(f'Against B: {format(compare_b)}')
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()

  if rightness(get_count(compare_a), get_count(compare_b), answer) == 'right':
    score += 1
    replit.clear()
    print(art.logo)
    print(f"Your answer is right, Current score: {score}")
    continue
 
  else:
    replit.clear()
    print(art.logo)
    print(f"Sorry that's wrong, the final score is {score}")
    break
# I think I did it, YAY!!!
# They say it is better to make functions for every little thing but experts do it this way 😎

from art import logo
import random
import replit

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
  
  while True:
    want_or_not = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if want_or_not == 'y':
      replit.clear()
      print(logo)
      user_cards = [random.choice(cards), random.choice(cards)]
      comp_cards = [random.choice(cards), random.choice(cards)]
      print(f'Your cards: {user_cards}, current score: {sum(user_cards)}')
      print(f"Computer's current score: {comp_cards[0]}\n")
      more_cards = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      
      if more_cards == 'y':
        user_cards.append(random.choice(cards))

      comp_sum = sum(comp_cards)
      user_sum = sum(user_cards)
      print(f"Your final hand: {user_cards}, final score: {user_sum}")
      print(f"Computer's final hand: {comp_cards}, final score: {comp_sum}\n")

      if user_sum > 21:
        if comp_sum <= 21:
          print('You busted, You Lose!')
        else:
          print('Since the both dealer and you have passed the limit of 21, it is a draw!')
          
      else:
        if comp_sum > 21:
          print('You win since the dealer busted')
        else:
          if comp_sum == user_sum:
            print("It's a draw!")
          elif comp_sum < user_sum:
            print("Win, you have Blackjack 😁")
          else:
            print("Lose, opponent has Blackjack")
          
    else:
      break


blackjack()
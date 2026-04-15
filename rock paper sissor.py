Rock = '''
    _______
---'   ____)
      (_____)
      (_____) ROCK
      (____)
---.__(___)

'''
Paper = '''
    _______
---'   ____)____
          ______)
          _______) PAPER
         _______)
---.__________)

'''
Scissor = '''
    _______
---'   ____)____
          ______)
       __________) SCISSOR
      (____)
---.__(___)

'''

import random
user_input = int(input("What do you want to choose? (Type 0 for 'ROCK' 1 for 'PAPER' 2 for 'SCISSOR'): "))
game_list = [Rock,Paper,Scissor]
user_picture = game_list[user_input]
random_choice = random.choice(game_list)
if random_choice == Rock and user_input ==0:
    print(f"You choose: {user_picture} Computer choose: {random_choice} Draw")
elif random_choice == Paper and user_input ==1:
    print(f"You choose: {user_picture} Computer choose: {random_choice} Draw")
elif random_choice == Scissor and user_input ==2:
    print(f"You choose: {user_picture} Computer choose: {random_choice} Draw")
elif random_choice == Rock and user_input ==2:
    print(f"You choose: {user_picture} Computer choose: {random_choice} Win")
elif random_choice == Paper and user_input ==0:
    print(f"You choose: {user_picture} Computer choose: {random_choice} Win")
elif random_choice == Scissor and user_input ==1:
    print(f"You choose: {user_picture} Computer choose: {random_choice} Win")
elif random_choice == Rock and user_input ==1:
    print(f"You choose: {user_picture} Computer choose: {random_choice} Loose")
elif random_choice == Paper and user_input ==2:
    print(f"You choose: {user_picture} Computer choose: {random_choice} Loose")
elif random_choice == Scissor and user_input ==0:
    print(f"You choose: {user_picture} Computer choose: {random_choice} Loose")
else:
    print("You are a fucking idiot. Choose a correct character")










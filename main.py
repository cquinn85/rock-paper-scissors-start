import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images =[rock, paper, scissors]
user = int(input("What do you choose: 0 for rock, 1 for paper, and 2 for scissors\n"))
print(images[user]) 

computer = random.randint(0,2)
print("Computer chose: ")
print(images[computer])

if user >= 3 or user < 0:
  print("Didn't choose a proper number. You lose")
elif user == 0 and computer == 2: 
  print("Rock beats scissors. You Win!")
elif computer > user:
  print("You lose")
elif user > computer:
  print("You win!")
elif user == computer:
  print("It's a draw")

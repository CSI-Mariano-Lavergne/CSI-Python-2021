import random
print('Lets play a game of Rock, Paper, Scissors')
RPS = ['rock', 'paper', 'scissors']

playerChoice = input("Choose 'rock', 'paper', 'scissors'")

compChoice = random.choice(RPS)
print(f"Computer Selected: {compChoice}")
print(f"Player Selected: {playerChoice}")

if(playerChoice == compChoice):     
    print("You tied")
elif(playerChoice == 'rock' and compChoice == 'paper'):
    print("Computer won")
elif(playerChoice == 'paper' and compChoice == 'rock'):
    print("Player won")
elif(playerChoice == 'scissors' and compChoice == 'rock'):
    print("Computer won")
elif(playerChoice == 'rock' and compChoice == 'scissors'):
    print("Player won")
elif(playerChoice == 'paper' and compChoice == 'scissors'):
    print("Computer won")
elif(playerChoice == 'scissors' and compChoice == 'paper'):
    print("Player won")
else:
    print("There was an error. Maybe you tied the answer wrong")
import random
games = ['Ludo', 'Chess', 'Rock-Paper-Scissors', 'Sudoku']
alias_map = {'rps': 'Rock-Paper-Scissors'}

game = [g.casefold() for g in games]
game = alias_map.get[(game, game)]

game = input("What game would you like to play? ")
if game in games and game == 'rock-paper-scissors':
    print("Welcome to the Rock-Paper-Scissors Game")
    options = ['rock', 'paper', 'scissors']
    options = [i.casefold() for i in options]
    computer_choice = random.choice(options)
    # rock > scissors, paper > rock, scissors > paper

    player_choice = input("\nRock\nPaper\nScissors\nShoot!: ").casefold()
    print(f"Computer chose: {computer_choice}")
    if player_choice not in options:
            print("Invalid choice! Please choose Rock, Paper, or Scissors.")
    else:
        print(f"Computer chose: {computer_choice}")
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice, computer_choice) in [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]:
            print("You win!")
        else:
            print("You lose!")
else:
    print("Sorry, game currently not available")
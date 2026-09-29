import random

# 1. Setup games and lowercased list
games = ['ludo', 'chess', 'rock-paper-scissors', 'sudoku']
alias_map = {"rps": "rock-paper-scissors"}

# 2. Get user game choice & normalize
game = input("What game would you like to play? ").strip().casefold()
game = alias_map.get(game, game)

# 3. Check availability
if game in games and game == 'rock-paper-scissors':
    print("Welcome to the Rock-Paper-Scissors Game!")
    
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    
    player_choice = input("\nRock\nPaper\nScissors\nShoot!: ").strip().casefold()
    
    # Validate user choice
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
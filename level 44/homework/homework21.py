def determine_winner(player1, player2):
    if player1 == player2:
        return "Draw!"

    winning_conditions = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if winning_conditions[player1] == player2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"

result1 = determine_winner("scissors", "paper")
result2 = determine_winner("scissors", "rock")
result3 = determine_winner("paper", "paper")
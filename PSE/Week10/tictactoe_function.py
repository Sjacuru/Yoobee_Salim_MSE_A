''' TOP-DOWN IMPLEMENTATION'''



def game_loop(board, current_player):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

    print(f"Player {current_player}'s turn. Choose a spot (1-9): ")

def valid_move(board, current_player):
    """
    Handles player input, validates the move, and updates the board list.
    Returns the updated board list or None if the input was invalid/taken.
    """
    while True:
        try:
            # We use input() directly here since the game_loop already printed the prompt
            position_input = input()
            position = int(position_input) - 1  # Convert to 0-indexed position
            
            # Check if position is valid (0-8) and spot is not taken
            if 0 <= position <= 8 and board[position] != 'X' and board[position] != 'O':
                # Update the board and return it
                board[position] = current_player
                return board 
            elif 0 <= position <= 8:
                print("That spot is already taken. Try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number (1-9).")
        except EOFError:
            # Handle input termination in some environments
            print("Game input terminated.")
            return board # Return board without changing it


def check_rows(board, current_player):
    win = False
    # Check Rows
    if board[0] == board[1] == board[2]: win = True
    elif board[3] == board[4] == board[5]: win = True
    elif board[6] == board[7] == board[8]: win = True
    # Check Columns
    elif board[0] == board[3] == board[6]: win = True
    elif board[1] == board[4] == board[7]: win = True
    elif board[2] == board[5] == board[8]: win = True
    # Check Diagonals
    elif board[0] == board[4] == board[8]: win = True
    elif board[2] == board[4] == board[6]: win = True
    
    if win:
        return (False, current_player) # Game ends, current player is the winner
        
    # Check for TIE
    elif all(spot == 'X' or spot == 'O' for spot in board):
        return (False, None) # Game ends, it's a tie
    
    # Game is still running
    else:
        return (True, None)

def final_move(board, winner):
# show final move
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")
    if winner is not None:
        print(f"Game Over! Player {winner} wins!")
    else:
        print("Game Over! It's a tie.")

def main():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    current_player = 'X'
    game_running = True
    winner = None

    print("--- Functional Tic-Tac-Toe! ---")
    
    while game_running:
        # 1. Display board and prompt
        game_loop(board, current_player)
        
        # 2. Handle move and update the board variable
        updated_board = valid_move(board, current_player)
        if updated_board is not None:
            # Explicitly update the main 'board' state
            board = updated_board 

            # 3. Check Game Status
            # check_rows returns (game_running: bool, winner: str or None)
            game_running, winner = check_rows(board, current_player)
            
            # 4. Switch Player (only if the game is still running)
            if game_running:
                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'
        
    # 5. Show Final Result
    final_move(board, winner)

if __name__ == '__main__':
    main()
import math


class Board:
    def __init__(self, board):
        self.board = board

    # Function that returns vacant positions
    def get_empty_positions(self):
        return [i for i in range(9) if self.board[i] == ' ']

    # updating function
    def update_board(self, position, player):
        self.board[position] = player

    # Function that controls the winner
    def is_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
            [0, 4, 8], [2, 4, 6]              # cross
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if board.is_winner('X'):
        return -1
    elif board.is_winner('O'):
        return 1
    elif len(board.get_empty_positions()) == 0:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for empty_position in board.get_empty_positions():
            board.update_board(empty_position, 'O')
            score = minimax(board, depth + 1, False)
            board.update_board(empty_position, ' ')
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for empty_position in board.get_empty_positions():
            board.update_board(empty_position, 'X')
            score = minimax(board, depth + 1, True)
            board.update_board(empty_position, ' ')
            best_score = min(score, best_score)
        return best_score

# Function that determines the computer's move
def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for empty_position in board.get_empty_positions():
        board.update_board(empty_position, 'O')
        score = minimax(board, 0, False)
        board.update_board(empty_position, ' ')
        if score > best_score:
            best_score = score
            best_move = empty_position
    return best_move


def main():
    board = Board([' ' for _ in range(9)])
    print("Welcome to Tic Tac Toe!")
    while not board.is_winner('X') and not board.is_winner('O') and len(board.get_empty_positions()) > 0:
        # Player's move
        player_move = int(input("Enter your move (0-8): "))
        if board.board[player_move] != ' ':
            print("Invalid move, please try again.")
            continue
        board.update_board(player_move, 'X')
        print("Player's move:")
        print_board(board.board)

        # computer's move
        if not board.is_winner('O') and len(board.get_empty_positions()) > 0:
            computer_move = get_best_move(board)
            board.update_board(computer_move, 'O')
            print("Computer's move:")
            print_board(board.board)

    
    if board.is_winner('X'):
        print("Congratulations! You win!")
    elif board.is_winner('O'):
        print("Sorry, computer wins!")
    else:
        print("It's a draw!")


def print_board(board):
    for i in range(0, 9, 3):
        print(' | '.join(board[i:i+3]))
        if i < 6:
            print('-' * 9)

# game start 
if __name__ == "__main__":
    main()

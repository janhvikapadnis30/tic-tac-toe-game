from board import Board
from game_engine import GameEngine
from ai_engine import AIEngine
from score_tracker import ScoreTracker
from validator import InputValidator

def main():
    board = Board()
    engine = GameEngine(board)
    ai = AIEngine()
    tracker = ScoreTracker()

    print("=== Welcome to Tic-Tac-Toe ===")
    board.display()

    while True:
        # Player Move
        user_input = input("Enter cell position (1-9): ")
        is_valid, result = InputValidator.validate_position(user_input, board.grid)
        
        if not is_valid:
            print(f"Error: {result}")
            continue

        board.update_cell(result, "X")
        board.display()

        if engine.check_win("X"):
            print("Congratulations! You won!")
            tracker.record_result("X")
            break
        if engine.check_draw():
            print("It's a draw!")
            tracker.record_result("Draw")
            break

        # AI Move
        print("AI is making a move...")
        ai_move = ai.get_move(board.grid)
        board.update_cell(ai_move, "O")
        board.display()

        if engine.check_win("O"):
            print("AI wins! Better luck next time.")
            tracker.record_result("O")
            break
        if engine.check_draw():
            print("It's a draw!")
            tracker.record_result("Draw")
            break

if __name__ == "__main__":
    main()

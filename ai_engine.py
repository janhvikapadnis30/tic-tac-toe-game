import random

class AIEngine:
    @staticmethod
    def get_move(board_grid: list) -> int:
        available_moves = [i for i, spot in enumerate(board_grid) if spot == " "]
        if available_moves:
            return random.choice(available_moves)
        return -1

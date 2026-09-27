class GameEngine:
    WINNING_COMBOS = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)               # Diagonal
    ]

    def __init__(self, board):
        self.board = board

    def check_win(self, symbol: str) -> bool:
        grid = self.board.grid
        return any(
            grid[a] == grid[b] == grid[c] == symbol 
            for a, b, c in self.WINNING_COMBOS
        )

    def check_draw(self) -> bool:
        return " " not in self.board.grid and not self.check_win("X") and not self.check_win("O")

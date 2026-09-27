class Board:
    def __init__(self):
        self.grid = [" "] * 9

    def reset(self):
        self.grid = [" "] * 9

    def update_cell(self, position: int, symbol: str) -> bool:
        if 0 <= position < 9 and self.grid[position] == " ":
            self.grid[position] = symbol
            return True
        return False

    def display(self):
        print("\n")
        print(f" {self.grid[0]} | {self.grid[1]} | {self.grid[2]} ")
        print("---+---+---")
        print(f" {self.grid[3]} | {self.grid[4]} | {self.grid[5]} ")
        print("---+---+---")
        print(f" {self.grid[6]} | {self.grid[7]} | {self.grid[8]} ")
        print("\n")

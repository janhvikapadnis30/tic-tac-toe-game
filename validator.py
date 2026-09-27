class InputValidator:
    @staticmethod
    def validate_position(user_input: str, board_grid: list):
        if not user_input.isdigit():
            return False, "Input must be a number between 1 and 9."
        
        pos = int(user_input) - 1
        if pos < 0 or pos > 8:
            return False, "Choice must be a number from 1 to 9."
        if board_grid[pos] != " ":
            return False, "Cell is already occupied! Choose an empty spot."
            
        return True, pos

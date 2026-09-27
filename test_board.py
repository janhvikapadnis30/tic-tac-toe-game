import unittest
from board import Board

class TestBoard(unittest.TestCase):
    def test_win_condition(self):
        b = Board()
        b.grid = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(b.check_win('X'))

if __name__ == '__main__':
    unittest.main()

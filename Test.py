import unittest
import random
from GameScoreBoard import GameScoreBoard

class GameScoreBoardTest(unittest.TestCase):
    def test_updateScore(self):
        gameScoreBoard = GameScoreBoard();
        line = "abababaa"
        expectedScore = "Game-40"
        for player in line:
            gameScoreBoard.updateScore(player)
        self.assertEqual(expectedScore,gameScoreBoard.toString())

# Main
if __name__ == '__main__':
    unittest.main()

import unittest
import random
from GameScoreBoard import GameScoreBoard
from SetScoreBoard import SetScoreBoard

class GameScoreBoardTest(unittest.TestCase):
    def test_updateScore(self):
        self.compareToString("abababaa", "Game-40");
        self.compareToString("aaabaaa","Game-15");
        self.compareToString("aaaaaa","Game-0");
        self.compareToString("ababab","40-40");
        self.compareToString("abababa","A-40");
        self.compareToString("abababab","D-D");
    def compareToString(self,inputStr, expectedScore):
        gameScoreBoard = GameScoreBoard();
        for player in inputStr:
            gameScoreBoard.updateScore(player)
        self.assertEqual(expectedScore,gameScoreBoard.toString())

class SetScoreBoardTest(unittest.TestCase):
        def test_updateScore(self):
            setScoreBoard = SetScoreBoard();
            setScoreBoard.updateScore(self.createGameScoreBoard("abababaa"))
            setScoreBoard.updateScore(self.createGameScoreBoard("aaaaabaa"))
            setScoreBoard.updateScore(self.createGameScoreBoard("bbabbbaa"))
            setScoreBoard.updateScore(self.createGameScoreBoard("bbabaaaa"))
            setScoreBoard.updateScore(self.createGameScoreBoard("abababaa"))
            setScoreBoard.updateScore(self.createGameScoreBoard("aaababaa"))
            
            self.assertEqual("5 - 1",setScoreBoard.toString())
        def createGameScoreBoard(self,inputStr):
            gameScoreBoard = GameScoreBoard();
            for player in inputStr:
                gameScoreBoard.updateScore(player)
            return gameScoreBoard;


# Main
if __name__ == '__main__':
    unittest.main()

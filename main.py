#!/usr/bin/python

from GameScoreBoard import GameScoreBoard
from SetScoreBoard import SetScoreBoard
from MatchScoreBoard import MatchScoreBoard


def main(fileinput):
	matchScoreBoard  = MatchScoreBoard()
	setScoreBoard = SetScoreBoard();


	with open(fileinput, 'r') as f:
		lines = [line.rstrip('\n') for line in f]
		

	for line in lines:
		if line == "END SET":
			print "--------------"
			matchScoreBoard.addSet(setScoreBoard)
			setScoreBoard = SetScoreBoard();

			print matchScoreBoard.toString();
			print "---------------"
			continue
		
		gameScoreBoard = GameScoreBoard();
		
		for player in line:
			gameScoreBoard.updateScore(player)

		print gameScoreBoard.toString();
		setScoreBoard.updateScore(gameScoreBoard)

	print matchScoreBoard.toString();

if __name__ == '__main__':
	main("score.txt")
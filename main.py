#!/usr/bin/python

from GameScoreBoard import GameScoreBoard

def main():
	scoreBoard = GameScoreBoard();

	for c in "abababaa":
		scoreBoard.updateScore(c);
		print scoreBoard.toString();

if __name__ == '__main__':
	main()
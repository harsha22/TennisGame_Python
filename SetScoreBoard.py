
NO_WINNER = False
class SetScoreBoard(object):
	"""ScoreBoard"""
	def __init__(self):
		super(SetScoreBoard, self).__init__()
		self.score = {};
		self.score['a'] = 0;
		self.score['b'] = 0;

	def updateScore(gameScoreBoard):
		winner = gameScoreBoard.winner();
		if winner == NO_WINNER:
			pass
		self.score[winner] += 1;


	def winner(self):
		if any( [score >=6 for score in self.score.values()]) and abs(self.score['a']-self.score['b']) >= 2:
			if self.score['a'] > self.score['b']:
				return 'a'
			else :
				return 'b'
		else:
			return False;

	def toString(self):
		return self.score['a'] + " - " + self.score['b'];



class MatchScoreBoard(object):
	"""MatchScoreBoard"""
	
	def __init__(self):
		super(MatchScoreBoard, self).__init__()
		self.score = {};
		self.score['a'] = 0;
		self.score['b'] = 0;
		self.setScoreBoards = [];

	def addSet(self,setScoreBoard):
		if len(self.setScoreBoards) != 5:
			winner = setScoreBoard.winner();
			self.score[winner] += 1;
			setScoreBoards.append(setScoreBoard)

	def winner(self):
		if any( [score >=3 for score in self.score.values()] ):
			if self.score['a'] > self.score['b']:
				return 'a'
			else :
				return 'b'
		else:
			return False;

	def toString(self):
		return self.score['a'] + " - " + self.score['b'];
		
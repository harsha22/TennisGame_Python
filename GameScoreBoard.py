
WINNING_DIFF = 2;
DEUCE_CONDITION = 3
MIN_WINNING_SCORE = 4
SCORE_VALUES = ["0","15","30","40"]
NO_WINNER = False
LOSS = '40'

class GameScoreBoard(object):
	"""GameScoreBoard"""
	def __init__(self):
		super(GameScoreBoard, self).__init__()
		self.score = {};
		self.score['a'] = 0;
		self.score['b'] = 0;

	def updateScore(self, player):

		score = self.score[player];
		other = 'b' if (player == 'a') else 'a'

		if score == 'D':
			self.score[player] = 'A';
			self.score[other] = '*'
		elif score == '*':
			self.score[player] = 'D';
			self.score[other] = 'D'
		elif score == 'A':
			self.score[player] = 'Game';
			self.score[other] = LOSS;			
		elif score == 'Game' or score == LOSS :
			pass
		else:
			self.score[player] += 1;

			moreThanWinnigScore = (self.score[player] ==  MIN_WINNING_SCORE)
			 
			if  moreThanWinnigScore and isinstance(self.score[other],int) and (self.score[player] - self.score[other]) >=2:
			 	self.score[player] = 'Game'
			elif (self.score[other] == DEUCE_CONDITION) and moreThanWinnigScore:
			 	self.score[player] = 'A'
			else:
			 	pass
				

	
	def winner(self):
		if (self.score['a'] == 'Game') :
			return 'a';
		elif (self.score['b'] == 'Game') :
			return 'b'
		else :
			return NO_WINNER;

	def toString(self):
		scoreA = self.score['a'];
		scoreB = self.score['b'];
		
		if (scoreA <= DEUCE_CONDITION) :
			scoreA = SCORE_VALUES[scoreA] ; 
		if (scoreB <= DEUCE_CONDITION) :
			scoreB = SCORE_VALUES[scoreB];

		return  scoreA + "-" + scoreB
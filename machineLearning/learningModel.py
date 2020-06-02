class learningModel(object):
	x_dim = -1
	coef = np.zeros(0)
	def __init__(self, x_dim = -1):
		self.x_dim = x_dim
		if x_dim > 0:
			coef = np.zeros((1, x_dim + 1))
	def fit(X, y):
	def predict(X):
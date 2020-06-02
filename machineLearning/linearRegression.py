import numpy as np
from IPython import embed

class LinearRegression(object):
    coef = np.zeros(0)
    x_dim = 0
    def __init__(self):
        coef = np.zeros(0)
        x_dim = 0
    def fit(self, X, y):
        x_np = np.array(X)
        y_np = np.array(y)
        sample_Num, self.x_dim = x_np.shape
        self.x_dim += 1       
        x_np = np.insert(x_np, self.x_dim - 1, 1, axis = 1)
        self.coef = np.matmul(np.matmul(np.linalg.inv(np.matmul(x_np.T, x_np)), x_np.T), y)
        print("finish")
    def predict(X):
        x_np = np.array(X)
        x_np = np.insert(x_np, self.x_dim - 1, 1, axis = 1)
        y = np.matmul(x_np, coef.T)
        return y


X = [[1,1],[2,2],[3,3]]
y = [1,2,3]

X2 = [[4,4], [5,5]]

b = LinearRegression()
b.fit(X, y)
c = b.predict(X)
embed()





import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
np.random.seed(29)


n_samples=506
n_featrues=13
X=np.random.rand(n_samples,n_featrues)
Y=np.random.rand(n_samples)

X_train, X_test, Y_train, Y_test=train_test_split (X, Y, test_size=0.2)
regression_clf=LinearRegression()
regression_clf.fit (X_train, Y_train)
Y_predict=regression_clf.predict(X_test)
score=r2_score (Y_test, Y_predict)
print("房價的預測準確率:", score)


plt.plot(Y_test, label='Real Price')
plt.plot(Y_predict, label='Predict Price')
plt.xlabel("index")
plt.ylabel("price")
plt.title('real vs predict')
plt.legend()
plt.show()
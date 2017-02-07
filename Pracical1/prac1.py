import cPickle as cp
import numpy as np
import matplotlib.pyplot as plt

X, y = cp.load(open('winequality-white.cPickle','rb'))

N, D = X.shape
N_train = int(0.8 * N)
N_test = N - N_train

X_train = X[:N_train]
y_train = y[:N_train]
X_test = X[N_train:]
y_test = y[N_train:]

# Handin 1: Creating the bar chart for y_train

#quality=range(3, 10)
#frequency=np.zeros(7)
#for i in y_train:
	#frequency[i-3]+=1
#width=0.5
#bar1=plt.bar(quality, frequency, width, align='center', color='r')
#plt.show()

# Handin 2: Mean squared error for simple predictor

#y_mean=np.mean(y_train)
#SqErr=(y_test-y_mean)**2
#SqErr_Mean=np.mean(SqErr)
#print(SqErr_Mean)

# Handin 3: Linear Model Using Least Squares

print(X_train.shape)

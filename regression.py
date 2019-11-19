# Applying Regression Model to predict the error

from sklearn.linear_model import LogisticRegression
from sklearn.datasets.samples_generator import make_blobs
from sklearn import metrics

# Training data for Regression Model
# 80% for training and 20% for testing

train_x = X[:80]
train_y = Y[:80]

# Testing data
test_x = X[80:]
test_y = Y[80:]

# # pick some random from given
# import random
# for i in range(10):
# 	j = random.randint(0,len(X))
# 	test_x.append(X[j])
# 	test_y.append(Y[j])


# fit final model
model = LogisticRegression()
model.fit(train_x, train_y)

# make predictions
predicted = model.predict(test_x)
# show the inputs and predicted outputs
for i in range(len(test_x)):
	print("X=%s, Predicted=%s, Actual=%s" % (test_x[i], predicted[i], test_y[i]))
 
print("Accuracy:",metrics.accuracy_score(test_y, predicted))
print("Precision:",metrics.precision_score(test_y, predicted))

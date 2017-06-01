import numpy as np
from sklearn import cross_validation
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import LogisticRegression
import sklearn.metrics
import sys

read_data = np.genfromtxt(sys.argv[1])
# print data.shape 

class Data:
	def __init__(self):
		pass

data = Data()
data.X = read_data[:,:2]
data.Y = np.ravel(read_data[:,2:])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(data.X, data.Y, 
	test_size = 0.2)

model = LogisticRegression()
model = model.fit(X_train,y_train)

print model.coef_

print model.score(X_train,y_train)
print model.score(X_test, y_test)

y_pred = model.predict(X_test)
print sklearn.metrics.confusion_matrix(y_test, y_pred)

y_whole_pred = model.predict(data.X)
print "wg"
print sklearn.metrics.confusion_matrix(data.Y, y_whole_pred)
print sklearn.metrics.average_precision_score(data.Y,model.predict_proba(data.X)[:,1])

p = model.predict_proba(X_test) 
print "AuROC"
print sklearn.metrics.roc_auc_score(y_test,p[:,1])
print "AuPRC"
print sklearn.metrics.average_precision_score(y_test,p[:,1])


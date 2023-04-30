# SUPPORT VECTOR REGRESSION
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
import numpy as np


# load data
path = r"https://drive.google.com/uc?export=download&id=1xxDtrZKfuWQfl-6KA9XEd_eatitNPnkB" 
df = pd.read_csv(path)
df.head()
 
# Split Data
X = df.drop('price', axis=1)
y = df['price']
 
print('Shape of X = ', X.shape)
print('Shape of y = ', y.shape)
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)
 
print('Shape of X_train = ', X_train.shape)
print('Shape of y_train = ', y_train.shape)
print('Shape of X_test = ', X_test.shape)
print('Shape of y_test = ', y_test.shape)
 
# Feature Scaling
sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)
 
# Support Vector Regression - ML Model Training  
svr_rbf = SVR(kernel='rbf')
svr_rbf.fit(X_train, y_train)
svr_rbf.score(X_test, y_test)
svr_linear = SVR(kernel='linear')
svr_linear.fit(X_train, y_train)
svr_linear.score(X_test, y_test)
svr_poly = SVR(kernel='poly',degree=2,)
svr_poly.fit(X_train, y_train)
svr_poly.score(X_test, y_test)
 
#  Predict the value of Home and Test
X_test[0] 
svr_linear.predict([X_test[0]])
y_pred = svr_linear.predict(X_test)
y_pred
y_test
 
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print('MSE = ', mse)
print('RMSE = ', rmse)

#End

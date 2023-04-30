# SUPPORT VECTOR CLASSIFICATION:- Linear Kernel
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

#load dataset
data = load_breast_cancer()
data.data
 
data.feature_names
data.target
data.target_names
 
# create dtaframe
df = pd.DataFrame(np.c_[data.data, data.target], columns=[list(data.feature_names)+['target']])
df.head()
df.tail()
df.shape
 
"""### Split Data"""
 
X = df.iloc[:, 0:-1]
y = df.iloc[:, -1]
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2020)
print('Shape of X_train = ', X_train.shape)
print('Shape of y_train = ', y_train.shape)
print('Shape of X_test = ', X_test.shape)
print('Shape of y_test = ', y_test.shape)
 
"""## Train Support Vector Classification Model"""
 
classification_rbf = SVC(kernel='rbf')
classification_rbf.fit(X_train, y_train)
classification_rbf.score(X_test, y_test)
 
"""## Feature Scaling"""
 
sc = StandardScaler()
sc.fit(X_train)
 
X_train_sc = sc.transform(X_train)
X_test_sc = sc.transform(X_test)
 
"""## SVC with Kernel Linear"""
classification_linear = SVC(kernel='linear')
classification_linear.fit(X_train_sc, y_train)
classification_linear.score(X_test_sc, y_test)
 
"""## Predict Cancer"""
 
patient1 = [17.99,10.38,122.8,1001.0,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019.0,0.1622,0.6656,0.7119,0.2654,0.4601, 0.1189]
patient1_sc = sc.transform(np.array([patient1]))
patient1_sc
pred= classification_linear.predict(patient1_sc)
pred
 
data.target_names
 
if pred[0] == 0:
  print('Patient has Cancer (malignant tumor)')
else:
  print('Patient has no Cancer (malignant benign)')

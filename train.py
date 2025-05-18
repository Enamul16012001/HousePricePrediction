import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

boston = fetch_california_housing()

dataset=pd.DataFrame(boston.data,columns=boston.feature_names)

dataset['Price']=boston.target

X=dataset.iloc[:,:-1]
y=dataset.iloc[:,-1]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

pickle.dump(scaler,open('scaling.pkl','wb'))

regression=LinearRegression()
regression.fit(X_train,y_train)

print(regression.coef_)
print(regression.intercept_)

pickle.dump(regression,open('regmodel.pkl','wb'))
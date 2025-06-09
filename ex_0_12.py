from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('customer_churn.csv')
print(data.head())
print(data.info())

data=data.drop(columns=['CustomerID'])
data=data.dropna()

data=pd.get_dummies(data,drop_first=True)

X = data.drop('Churn', axis=1)
y = data['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=200, random_state=42)

model.fit(X_train, y_train)

predictions=model.predict(X_test)
accuracy= accuracy_score(y_test,predictions)
print(f'Test accuracy: {accuracy}')
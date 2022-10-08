# importing required libraries
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# loading and reading the dataset

diabetes = pd.read_csv("diabetes_cleveland_upload.csv")

# creating a copy of dataset so that will not affect our original dataset.
diabetes_df = diabetes.copy()

# Renaming some of the columns 
diabetes_df = diabetes_df.rename(columns={'condition':'target'})
print(diabetes_df.head())

# model building 

#fixing our data in x and y. Here y contains target data and X contains rest all the features.
x= diabetes_df.drop(columns= 'target')
y= diabetes_df.target

# splitting our dataset into training and testing for this we will use train_test_split library.
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.20, random_state=1)

#feature scaling
# scaler= StandardScaler()
# x_train_scaler= scaler.fit_transform(x_train)
# x_test_scaler= scaler.fit_transform(x_test)

# creating K-Nearest-Neighbor classifier
# model=RandomForestClassifier(n_estimators=20)
# model.fit(x_train_scaler, y_train)
# y_pred= model.predict(x_test_scaler)
# p = model.score(x_test_scaler,y_test)
# print(p)

# print('Classification Report\n', classification_report(y_test, y_pred))
# print('Accuracy: {}%\n'.format(round((accuracy_score(y_test, y_pred)*100),2)))

# cm = confusion_matrix(y_test, y_pred)
# print(cm)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(x_train,y_train)
Y_pred_lr = lr.predict(x_test)
score_lr = round(accuracy_score(Y_pred_lr,y_test)*100,2)

print("The accuracy score achieved using Logistic Regression is: "+str(score_lr)+" %")

# Creating a pickle file for the classifier

print('Classification Report\n', classification_report(y_test, Y_pred_lr))
print('Accuracy: {}%\n'.format(round((accuracy_score(y_test, Y_pred_lr)*100),2)))

cm = confusion_matrix(y_test, Y_pred_lr)
print(cm)

filename = 'diabetes-disease-prediction-model.pkl'
pickle.dump(lr, open(filename, 'wb'))


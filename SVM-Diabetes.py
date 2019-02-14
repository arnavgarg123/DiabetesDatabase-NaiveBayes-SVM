import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
df = pd.read_csv("/home/arnav/WorkSpace/GitHub/DiabetesDatabase-NaiveBayes-SVM/diabetes.csv")
df.head(20)
df.notnull().sum()
df.info()
print(sns.pairplot(df))
plt.pyplot.figure(figsize=(16, 16))
print(sns.heatmap(df.corr(), annot=True))
print(sns.boxplot(x='Outcome', y='Glucose', data=df))
X = df.drop(['Outcome'], axis=1)
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)
model = svm.SVC(C=2, gamma='scale', kernel='linear')
model.fit(X_train, y_train)
prediction = model.predict(X_test)
print(metrics.accuracy_score(prediction, y_test) * 100)
print(confusion_matrix(y_test, prediction))
print(classification_report(y_test, prediction))
print('MAE:', metrics.mean_absolute_error(y_test, prediction))
print('MSE:', metrics.mean_squared_error(y_test, prediction))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, prediction)))

import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
df = pd.read_csv("/home/arnav/WorkSpace/GitHub/DiabetesDatabase-NaiveBayes-SVM/diabetes.csv")
df.head(20)
df.isnull().sum()
df.info()
print(sns.pairplot(df))
plt.pyplot.figure(figsize=(16, 16))
print(sns.heatmap(df.corr(), annot=True))
print(sns.boxplot(x='Outcome', y='Glucose', data=df))
X = df.drop(['Outcome', 'Age'], axis=1)
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
model = GaussianNB()
model.fit(X_train, y_train)
prediction = model.predict(X_test)
print(metrics.accuracy_score(prediction, y_test) * 100)
print(confusion_matrix(y_test, prediction))
print(classification_report(y_test, prediction))

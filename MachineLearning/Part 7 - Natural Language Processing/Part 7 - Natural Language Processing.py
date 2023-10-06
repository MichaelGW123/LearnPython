# Natural Language Processing
# Sentiment Analysis

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# Importing the dataset
path = Path(__file__).parent / 'Restaurant_Reviews.tsv'
dataset = pd.read_csv(path, delimiter = '\t', quoting = 3)

# Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, len(dataset.index)):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    all_stopwards = stopwords.words('english')
    all_stopwards.remove('not')
    review = [ps.stem(word) for word in review if not word in set(all_stopwards)]
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features= 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Training the Logistic Regression model on the Training set
# from sklearn.linear_model import LogisticRegression
# classifier = LogisticRegression(random_state=0)
# classifier.fit(X_train, y_train)
# 0.775

# Training the KNN model on the Training set
# from sklearn.neighbors import KNeighborsClassifier
# classifier = KNeighborsClassifier()
# classifier.fit(X_train, y_train)
# 0.66

# Training the SVM on the Training set
from sklearn.svm import SVC
classifier = SVC(kernel='linear', random_state=0)
classifier.fit(X_train, y_train)
# 0.79

# Training the Kernal SVM on the Training set
# from sklearn.svm import SVC
# classifier = SVC(kernel='rbf', random_state=0)
# classifier.fit(X_train, y_train)
# 0.78

# Training the Naive Bayes model on the Training set
# from sklearn.naive_bayes import GaussianNB
# classifier = GaussianNB()
# classifier.fit(X_train, y_train)
# 0.73

# Training the Decision Tree on the Training set
# from sklearn.tree import DecisionTreeClassifier
# classifier = DecisionTreeClassifier(criterion="entropy", random_state= 0)
# classifier.fit(X_train, y_train)
# 0.75

# Training the Random Forest on the Training set
# from sklearn.ensemble import RandomForestClassifier
# classifier = RandomForestClassifier(n_estimators=10, criterion="entropy", random_state= 0)
# classifier.fit(X_train, y_train)
# 0.725

# Predicting the Test set results
y_pred = classifier.predict(X_test)
# print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score, precision_recall_fscore_support
cm = confusion_matrix(y_test, classifier.predict(X_test))
print(cm)
accuracy = accuracy_score(y_test, classifier.predict(X_test))
print(accuracy)
stats = precision_recall_fscore_support(y_test, classifier.predict(X_test), average='binary')
print(stats)
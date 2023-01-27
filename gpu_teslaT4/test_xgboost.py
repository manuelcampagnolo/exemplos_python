import sys
sys.path.insert(0, 'myvenv\Lib\site-packages')

import pandas as pd
from xgboost import XGBClassifier
import sklearn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.datasets import make_classification # cria dados
import time
import sys


# create data set
X, y = make_classification(n_samples=500000,class_sep=0.7)
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.33, random_state=42)

# XGBClassifier’s default settings and didn’t pass in any optional parameters
start = time.time()
classifier = XGBClassifier()
model = classifier.fit(X_train, y_train)
predictions = model.predict(X_test)
classification = classification_report(y_test, predictions)
print(classification)
print(time.time() - start)

# All you need to do to make it run on your GPU is pass in the gpu_hist value and define this tree_method.
start = time.time()
classifier = XGBClassifier(tree_method='gpu_hist')
model = classifier.fit(X_train, y_train)
predictions = model.predict(X_test)
classification = classification_report(y_test, predictions)
print(classification)
print(time.time() - start)

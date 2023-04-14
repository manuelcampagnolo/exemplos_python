'''

This will create a plot that shows the LDA projection of the iris dataset onto a two-dimensional subspace. The different colors represent the different classes (species) in the dataset, while the dots represent the individual data points.

Note that the n_components parameter in the LinearDiscriminantAnalysis function determines the number of dimensions in the LDA projection. In this example, we chose n_components=2 to project the data onto a two-dimensional subspace.

'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

lda = LinearDiscriminantAnalysis(n_components=2)
X_r = lda.fit(X, y).transform(X)
colors = ['navy', 'turquoise', 'darkorange']
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=.8, lw=lw,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA of iris dataset')
plt.show()

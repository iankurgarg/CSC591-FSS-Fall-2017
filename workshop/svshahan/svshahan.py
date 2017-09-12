# Workshop TODO code
# coding: utf-8

import numpy as np
from sklearn import datasets

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test  = iris_X[indices[-10:]]
iris_y_test  = iris_y[indices[-10:]]

def variationOfK(n):
    # KNN Visualization.
    n_neighbors = n
    h = .02  # step size in the mesh

    # Create color maps
    from matplotlib.colors import ListedColormap
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

    for weights in ['uniform', 'distance']:
        # we create an instance of Neighbours Classifier and fit the data.
        knn = KNeighborsClassifier(n_neighbors, weights=weights)
        knn.fit(X, y)

        # Plot the decision boundary. For that, we will assign a color to each
        # point in the mesh [x_min, x_max]x[y_min, y_max].
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                             np.arange(y_min, y_max, h))
        Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        plt.figure()
        plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

        # Plot also the training points
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,
                    edgecolor='k', s=20)
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.title("3-Class classification (k = %i, weights = '%s')"
                  % (n_neighbors, weights))

    plt.show()


for i in range(1,5):
    variationOfK(i)


#### Choosing best K should be done using cross-validation on a metric of choice like accuracy score, precision, recall, or f1
import numpy as np
scores=[]
for i in range(1,40):
    neighbors = i
    knn_model = KNeighborsClassifier(n_neighbors=neighbors)
    knn_model.fit(iris_X_train,iris_y_train)
    scores.append(knn_model.score(iris_X_test, iris_y_test))
print scores
print 'optimal k:',np.argmax(scores)+1
plt.plot(scores)
plt.ylim((0,1.1))
plt.show()


# ### Try cross-validation for best k

from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

knn_model = KNeighborsClassifier()
parameters = {'n_neighbors':range(1,40),'weights':['uniform','distance']}
best_knn = GridSearchCV(knn_model,param_grid=parameters,n_jobs=-1,cv=10)
best_knn.fit(iris_X,iris_y)

print 'Results after Cross-Validation'
print 'Best parameters:', best_knn.best_params_
print 'Best cross-validation score:',best_knn.best_score_
best_model = best_knn.best_estimator_
print 'Best model:\n',best_model


# ## SVM choosing the kernel

from sklearn.svm import SVC
def variationOfkernal(kernel='rbf'):
    # KNN Visualization.
    h = .02  # step size in the mesh

    # Create color maps
    from matplotlib.colors import ListedColormap
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

    for weights in ['uniform', 'distance']:
        # we create an instance of Neighbours Classifier and fit the data.
        svc = SVC(kernel=kernel)
        svc.fit(X, y)

        # Plot the decision boundary. For that, we will assign a color to each
        # point in the mesh [x_min, x_max]x[y_min, y_max].
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                             np.arange(y_min, y_max, h))
        Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        plt.figure()
        plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

        # Plot also the training points
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,
                    edgecolor='k', s=20)
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.title("3-Class classification KERNEL="+kernel)
    plt.show()


variationOfkernal('linear')
variationOfkernal('rbf')
variationOfkernal('poly')
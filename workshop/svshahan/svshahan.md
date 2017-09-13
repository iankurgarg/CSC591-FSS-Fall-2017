# Workshop - Answers (agarg12)

### Experiments with different values of K:

The plots in the experiments show that lower values of k create separated boundaries. This can represent overfitting case. Too high values add a lot of bias.

K=1
![Low K](k_1.png)

K=4
![High K](k_4.png)


### Choosing best K:

Should be done using cross-validation on a metric of choice like accuracy score, precision, recall, or f1

### Explore different kernels of Support Vector Machine:

Different kernels like rbf, linear, poly create different decision boundries for the classification

Kernel = rbf

![Low K](kernel_rbf.png)

Kernel = polynomial

![Low K](kernel_poly.png)

Kernel = linear

![Low K](kernel_linear.png)

### Explian how we should choose the kernel.

Should be done using cross-validation on a metric of choice by fitting different models with different kernels and choose the best one

## Bonus Part

### PCA for dimensionality reduction

We perform PCA using scikit learn's PCA function and then choose enough number of components to cover 97% of the variance in the data

Below are the resultant visualizations after performing PCA and then training:

1. KNN

![Low K](pca_knn.png)

2. SVC

![Low K](pca_svc.png)

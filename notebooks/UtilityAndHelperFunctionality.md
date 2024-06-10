# Utilities and Helper Functionality used in the Notebooks

## Keras utilities for data prepropcessing

`keras.utils.to_categorical()`

Keras provides numpy utility library, which provides functions to perform actions on numpy arrays. Using the method `to_categorical()`, a numpy array (or) a vector which has integers that represent different categories, can be converted into a numpy array (or) a matrix which has binary values and has columns equal to the number of categories in the data.

**Syntax:** `keras.utils.to_categorical(y, num_classes=None, dtype="float32")`

**Parameters:**

`y (input vector)`: a vector which has inegers representing various classes in the data

`num_classes`: total number of classes. If omitted it is set to the largest number in the input vector plus 1. 

`dtype`: the desired data type of the output values. 

**Output:**

A matrix of binary values (either `1` or `0`). It has number of rows equal to the length of the input vector and number of columns equal to the number of classes.

**Example:** Converting `cifar10` dataset labels vector to categorical data matrix

```python
# loading the dataset

from keras.datasets import cifar10
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

# print labels for the training set
print(train_labels)
print(train_labels.shape)

# print labels for the testing set
print(test_labels)
prnt(test_labels.shape)

# Applying the function to training set labels and testing set labels
from keras.utils import to_categorical
train_labels = to_categorical(train_labels, dtype="uint8")
test_labels = to_categorical(test_labels, dtype="uint8")

# labels after applying the function
# training set lables
print(train_labels) 
print(train_labels.shape) 
  
# Testing set labels 
print(test_labels) 
print(test_labels.shape) 
```
**Output of the Example code:**:
```python
#Labels before applying the function
#Training set labels
array([[6],
       [9],
       [9],
       ...,
       [9],
       [1],
       [1]], dtype=uint8)

#Training set labels shape
(50000, 1)

#Testing set labels
array([[3],
       [8],
       [8],
       ...,
       [5],
       [1],
       [7]], dtype=uint8)

#Testing set labels shape
(10000, 1)

#Labels after applying the function
#Training set labels
[[0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 1]
 [0 0 0 ... 0 0 1]
 ...
 [0 0 0 ... 0 0 1]
 [0 1 0 ... 0 0 0]
 [0 1 0 ... 0 0 0]]

#Training set labels shape
(50000, 10)

#Testing set labels
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 1. 0.]
 [0. 0. 0. ... 0. 1. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 1. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 1. 0. 0.]]

#Testing set labels shape
(10000, 10)

```



## numpy helper functions




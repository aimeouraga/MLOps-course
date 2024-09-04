
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.datasets import load_iris
iris=load_iris()
for keys in iris.keys() :
    print(keys)

X = iris.data
y = iris.target


print(X)






import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import random

random.seed(1)

# Einlesen des Datensatzes
data = pd.read_csv("./Dataset/train.csv").values

clf = DecisionTreeClassifier()

# Erstellung des Trainingsdatensatzes (hier: Unterteilung des "train"-Datensatzes)
xtrain = data[0:21000, 1:]
train_label = data[0:21000, 0]

# Erstellung des Test-Datensatzes (ab Eintrag 21000 des ursprünglichen "Train"-Datensatzes)
xtest = data[21000:, 1:]
actual_label = data[21000:, 0]

# Ausführen der Fit-Methode
clf.fit(xtrain, train_label)

# Berechnung der Accuracy des Decision Trees
p = clf.predict(xtest)
count = 0
for i in range(0, 21000):
    count += 1 if p[i] == actual_label[i] else 0
print("Accuracy for Decision Tree:", round(((count/21000)*100), 1))

# #Ausgabe des Bildes basierend auf dem ursprünglichen Datensatzes
d = xtest[10]  # Verwendung von Eintrag 10 des Test-Datensatzes (="2")
d.shape = (28, 28)  # Vorgabe zur Größe des Bildes
plt.imshow(255-d, cmap='gray')
print(clf.predict([xtest[10]]))
plt.show()

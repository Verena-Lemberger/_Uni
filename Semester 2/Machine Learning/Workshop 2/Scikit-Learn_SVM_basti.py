import pandas as pd
from sklearn import svm

# Einlesen des Datensatzes
data = pd.read_csv("./Dataset/train.csv").values

# Erstellung des Trainingsdatensatzes (hier: Unterteilung des "train"-Datensatzes)
xtrain = data[0:21000, 1:]
train_label = data[0:21000, 0]

# Erstellung des Test-Datensatzes (ab Eintrag 21000 des ursprünglichen "Train"-Datensatzes)
xtest = data[21000:, 1:]
actual_label = data[21000:, 0]

# SVM
clf_svm = svm.SVC(gamma=0.001, C=100)
clf_svm.fit(xtrain, train_label)

d_svm = xtest[8]  # Verwendung von Eintrag 8 des Test-Datensatzes (="3")
d_svm.shape = (28, 28)  # Vorgabe zur Größe des Bildes

# Berechnung der Accuracy des SVM
p_svm = clf_svm.predict(xtest)
count_svm = 0
for i in range(0, 21000):
    count_svm += 1if p_svm[i] == actual_label[i] else 0
print("Accuracy for SVM:", (count_svm/21000)*100)

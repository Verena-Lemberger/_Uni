# -*- coding: utf-8 -*-
import tensorflow as tf
import keras
from keras.datasets import mnist
from keras.layers import Dense
from keras.models import Sequential
# from matplotlib import pyplot as plt
from random import randint

# Preparing the dataset
# Setup train and test splits
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Making a copy before flattening for the next code-segment which displays images
x_train_drawing = x_train

image_size = 784  # 28 x 28
x_train = x_train.reshape(x_train.shape[0], image_size)
x_test = x_test.reshape(x_test.shape[0], image_size)

# Convert class vectors to binary class matrices
num_classes = 10
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

"""## So schaun die Daten aus:"""

# for i in range(64):
#     ax = plt.subplot(8, 8, i+1)
#     ax.axis('off')
#     plt.imshow(x_train_drawing[randint(0, x_train.shape[0])], cmap='Greys')

"""# Jetzt geht's los

## Modelerstellung
- über Sequential
- dann werden layer hinzugefügt wobei die units (.i. nodes) per layer mit angegeben werden
- der zweite add ist der output (daher sind es genau die 10 nodes, die den Ziffern entsprechen
- summary am Ende fürn Überblick
"""

model = Sequential()

# The input layer requires the special input_shape parameter which should match
# the shape of our training data.
model.add(Dense(units=32, activation='sigmoid', input_shape=(image_size,)))
model.add(Dense(units=num_classes, activation='softmax'))
# model.summary()

"""## Model Evaluation
- optimizer: sgd (Stochastic gradient descent)
 - wie optimiert wird
- loss function: categorical_crossentropy
 - mit welcher Methode der loss berechnet wird
- metrics: auccuracy
 - wonach optimiert werden soll

Dann wird das Modell auf train gefittet und auf test evaluiert

Darunter dann noch der plot
* NB! in der Vorlage war: ['acc'] und ['val_acc'] angegeben, was zu einem Fehler führte - acc mit accuracy ersetzen hat geholfen (der Name muss mit dem in metrics[] übereinstimmen)
"""

model.compile(optimizer="sgd", loss='categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(x_train, y_train, batch_size=128,
                    epochs=5, verbose=False, validation_split=.1)
loss, accuracy = model.evaluate(x_test, y_test, verbose=False)

# plt.plot(history.history['acc'])
# plt.plot(history.history['val_acc'])
# plt.plot(history.history['accuracy'])
# plt.plot(history.history['val_accuracy'])
# plt.title('model accuracy')
# plt.ylabel('accuracy')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='best')
# plt.show()

print(f'Test loss: {loss:.3}')
print(f'Test accuracy: {accuracy:.3}')

"""## Am Schluss das ganze noch in functions umschreiben
damit wir nachher damit rumspielen können
"""


def create_dense(layer_sizes):  # create_model
    model = Sequential()
    # Dense ist der layer - die mit add hinzugefügt werden
    model.add(
        Dense(layer_sizes[0], activation='sigmoid', input_shape=(image_size,)))

    for s in layer_sizes[1:]:
        model.add(Dense(units=s, activation='sigmoid'))

    # das ist der final layer (deswegen sind die units die classen - hier: 10)
    model.add(Dense(units=num_classes, activation='softmax'))

    return model


def evaluate(model, batch_size=128, epochs=5):
    # model.summary()
    model.compile(optimizer='sgd', loss='categorical_crossentropy',
                  metrics=['accuracy'])
    history = model.fit(x_train, y_train, batch_size=batch_size,
                        epochs=epochs, validation_split=.1, verbose=False)
    loss, accuracy = model.evaluate(x_test, y_test, verbose=False)

    # plt.plot(history.history['acc'])
    # plt.plot(history.history['val_acc'])
    # plt.plot(history.history['accuracy'])
    # plt.plot(history.history['val_accuracy'])
    # plt.title('model accuracy')
    # plt.ylabel('accuracy')
    # plt.xlabel('epoch')
    # plt.legend(['train', 'test'], loc='best')
    # plt.show()

    print()
    print(f'Test loss: {loss:.3}')
    print(f'Test accuracy: {accuracy:.3}')


"""# Playground
im Prinzip nichts anderes als an ein paar Schrauben drehen und schauen was sich verändert

NB! manche Sachen werden echt rechenintensiv

## Layer Anzahl erhöhen
"""

# jetzt können wir hergehen und mehrere hidden layer erzeugen (jeder hat 32 nodes)
# hier: 1 - 5 layers und die Evaluation von jedem
for layers in range(1, 5):
    model = create_dense([32] * layers)
    evaluate(model)

"""## Nodes per layer erhöhen"""

# jetzt erhöhen wir die nodes per layer - aber nur ein layer
for nodes in [32, 64, 128, 256, 512, 1024, 2048]:
    model = create_dense([nodes])
    evaluate(model)

"""## Mehr Layer und mehr Nodes"""

# jetzt wieder nur mit drei layers
for nodes in [32, 64, 128, 256, 512, 1024, 2048]:
    model = create_dense([nodes, nodes, nodes])
    evaluate(model)

"""## Mehrere Epochen

NB! das kann u.U. sehr lange rechnen
"""

# jetzt erhöhen wir die epochen (1024 und 2048 aus Zeitgründen entfernt)
for nodes in [32, 64, 128, 256, 512]:
    model = create_dense([nodes, nodes, nodes])
    evaluate(model, epochs=50)

# 64:  Test accuracy: 0.924
# 128: Test accuracy: 0.942
# 256: Test accuracy: 0.948
# 512: Test accuracy: 0.946

"""## Mehr Layer
gleiches wie zu Beginn, nur jetzt auch mit mehr Nodes und Epochen
"""

# zu Beginn hat eine höhere Layer Zahl die accuracy reduziert - jetzt mit mehr Nodes und epochen?
for layers in [1, 2, 3, 4, 10]:
    model = create_dense([64]*layers)
    evaluate(model, epochs=50)

# je mehr layer, desto weniger accuracy - warum?

"""## Die Sache mit dem Batch"""

# mit kleineren Batch - kann man ein schlechtes Model besser machen
# kleinerer Batch = mehr corrections
model = create_dense([32] * 5)
evaluate(model, epochs=50)

# vgl. Test accuracy: 0.179 vs. Test accuracy: 0.771

model = create_dense([32] * 5)
evaluate(model, batch_size=16, epochs=50)

"""### Batch und ein "gutes" Modell"""

# bei einem "guten" Model hat das aber keine Auswirkung:
model = create_dense([64])
evaluate(model, epochs=50)

model = create_dense([64])
evaluate(model, batch_size=16, epochs=50)

# Test accuracy: 0.943 (Batch 128)
# Test accuracy: 0.923 (Batch 16)

"""# Lessons learned
* Für + 90% accuracy reichen 64 nodes
* ab 128 Nodes (acc +94%) wird es nicht besser
* Mehrere Layer verschlechtern die accuracy
 * Warum?
* kleinerer Batch vebessert ein "schlechtes" Modell
 * "gute" Modelle werden nicht verbessert

# ToDo
was man noch weiter machen könnte

- ich hab noch nichts mit dem eigentlichen Modell angestellt (nur an den bestehenden Schrauben gedreht)
 - z.B. was passiert, wenn man statt sigmoid activation (soll ja nicht mehr ganz state of the art sein...) relu - oder andere verwendet
 - gleiches für loss function, etc.
- dann könnten wir uns auf ein "gutes" Modell festlegen und uns in weiterer Folge anschauen wie wir gelabelte Buchstaben bekommen
"""

"""mnist.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J7OUnmqKVRzfh_MciR3kDK5ICV6TqPaL

# Import and Preperation

credits where credits due:
https://colab.research.google.com/drive/1U0sRZdxVUn8LbQN9KidMaomKt2MPJ2-o#scrollTo=ARsdbx5hqLah

## Grundbegriffe machen das Leben leichter:
* *Dense* erstellt die *Layer*
* *units* sind die einzelnen Nodes
* *epochs* ist die Anzahl der Durchläufe
* *batch* die Korrekturen die durchgeührt werden (je niedriger, desto mehr)
"""

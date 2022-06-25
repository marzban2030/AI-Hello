import tensorflow as tf
from tensorflow.keras.datasets import mnist
import os

#Get working directory path.
cur_dir = os.getcwd()

#Load mnist dataset from downloaded local mnist.npz file.
(x_train, y_train), (x_test, y_test) = mnist.load_data(path=cur_dir+'/mnist.npz')

#Print shape of dataset, 
#Here are 60,000 training images with labels which each image resolution is 28×28 pixels.
#Also here are 60,000 testing images with labels.
#print(x_train.shape, y_train.shape)
#print(x_test.shape, y_test.shape)

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

x_train= x_train.reshape(-1, 28, 28, 1)
x_test= x_test.reshape(-1, 28, 28, 1)

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Conv2D(32, kernel_size= (3, 3), activation= 'relu', padding= 'same', input_shape= (28, 28, 1)))
model.add(tf.keras.layers.Conv2D(32, kernel_size= (3, 3), activation= 'relu'))
model.add(tf.keras.layers.MaxPool2D(pool_size= (2, 2)))
model.add(tf.keras.layers.Dropout(0.25))
model.add(tf.keras.layers.Conv2D(64, kernel_size= (3, 3), activation= 'relu', padding= 'same'))
model.add(tf.keras.layers.Conv2D(64, kernel_size= (3, 3), activation= 'relu'))
model.add(tf.keras.layers.MaxPool2D(pool_size= (2, 2)))
model.add(tf.keras.layers.Dropout(0.25))
model.add(tf.keras.layers.Conv2D(128, kernel_size= (3, 3), activation= 'relu', padding= 'same'))
model.add(tf.keras.layers.Conv2D(128, kernel_size= (3, 3), activation= 'relu'))
model.add(tf.keras.layers.MaxPool2D(pool_size= (2, 2)))
model.add(tf.keras.layers.Dropout(0.25))
model.add(tf.keras.layers.Flatten())
#Neurons
model.add(tf.keras.layers.Dense(512, activation='relu'))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(256, activation='relu'))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
#The 10 digits
model.add(tf.keras.layers.Dense(10, activation='softmax'))
model.compile(optimizer='Adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.save('handwritten.model')

loss, accuracy = model.evaluate(x_test, y_test)

print(loss)
print(accuracy)

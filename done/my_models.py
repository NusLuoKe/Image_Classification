# -*- coding: utf-8 -*-
# @Time    : 2018/1/28 9:40
# @File    : my_models.py
# @Author  : NusLuoKe

from keras.layers import Conv2D, MaxPool2D
from keras.layers import Dense, Activation, Flatten
from keras.models import Sequential


# model01
def cnn01(input_shape):
    model = Sequential()
    # conv1
    model.add(Conv2D(filters=64, kernel_size=3, strides=1, padding="same", input_shape=input_shape))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Activation('relu'))

    # con2
    model.add(Conv2D(filters=128, kernel_size=3, strides=1, padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Activation('relu'))

    # conv3
    model.add(Conv2D(filters=256, kernel_size=3, strides=1, padding='same'))
    model.add(MaxPool2D(pool_size=2, strides=2))
    model.add(Activation('relu'))

    # hidden
    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))

    # output
    model.add(Dense(1))
    model.add(Activation('sigmoid'))
    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
    return model




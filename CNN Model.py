from keras import backend as K
K.tensorflow_backend._get_available_gpus()
from keras.models import Sequential            #intialise the neural network
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint

classifier = Sequential()

classifier.add(Convolution2D(16, (3, 3), input_shape=(128, 128, 3), padding = 'same', activation = 'relu'))

classifier.add(MaxPooling2D(pool_size = (2,2)))

classifier.add(Convolution2D(32, (3, 3), padding = 'same', activation = 'relu'))

classifier.add(MaxPooling2D(pool_size = (2,2)))

classifier.add(Convolution2D(64, (3, 3), padding = 'same', activation = 'relu'))

classifier.add(MaxPooling2D(pool_size = (2,2)))

classifier.add(Convolution2D(128, (3, 3), padding = 'same', activation = 'relu'))

classifier.add(MaxPooling2D(pool_size = (2,2)))

classifier.add(Flatten())

classifier.add(Dense(units = 256, activation = 'relu'))

classifier.add(Dense(units = 4, activation = 'softmax'))

classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

classifier.summary()

# checkpoint
filepath="weights.best.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
                rescale = 1./255,
                shear_range = 0.2,
                zoom_range = 0.2,
                horizontal_flip = False)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                target_size = (128,128),
                                                batch_size = 32,
                                                class_mode='categorical')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (128,128),
                                            batch_size = 32,
                                            class_mode='categorical')


validation_size = 8000
batch_size = 32
classifier.fit_generator(training_set,
                         steps_per_epoch = 250,
                         epochs = 25,
                         validation_data = test_set,
                         validation_steps = 250)

#To improve accuracy we can increase the convolution layer.
#The best would be to increase the input_shape to (128,128) or even higher
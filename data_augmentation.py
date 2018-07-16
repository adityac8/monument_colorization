# Random Rotations
from keras.datasets import mnist
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
from keras import backend as K
K.set_image_data_format('channels_first')

from PIL import Image
# load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# reshape to be [samples][pixels][width][height]
X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)
# convert from int to float
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
# define data preparation
datagen = ImageDataGenerator(rotation_range=90)
# fit parameters from data
datagen.fit(X_train)
# configure batch size and retrieve one batch of images
#for X_batch, y_batch in 
j=0
from skimage.io import imsave
for i in datagen.flow(X_train, save_to_dir='images',batch_size=1, save_prefix='aug', save_format='jpg'):
    j+=1
#    im = Image.fromarray(i)
    imsave("your_file"+str(j)+".jpg",i[0][0].astype('int32'))
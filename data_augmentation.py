# Random Rotations
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
K.set_image_data_format('channels_last')
import cv2
from glob import glob
import numpy as np

x=[]
for i in glob("pisaDataset/*/*.jpg"):
    im = cv2.imread(i)
    x.append(im)
    
x=np.array(x)
x = x.astype('float32')

# define data preparation
datagen = ImageDataGenerator(rotation_range=90)
# fit parameters from data
datagen.fit(x)
# configure batch size and retrieve one batch of images
for i in datagen.flow(x, save_to_dir='images',batch_size=9, save_prefix='aug', save_format='jpg'):
    pass

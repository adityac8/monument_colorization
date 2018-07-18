# Monument Colorization

[![dep1](https://img.shields.io/badge/Python-3.6+-blue.svg)](#)
[![dep2](https://img.shields.io/badge/Keras-2.1+-red.svg)](#)
[![dep3](https://img.shields.io/badge/Tensorflow-1.4+-orange.svg)](#) 

We use the [Pisa Dataset](http://www.nmis.isti.cnr.it/falchi/pisaDataset) to perform monument colorization.
The dataset is already downloaded and saved in the `pisaDataset` directory.

We have augmented the datatset through

- Rotation
- Shifting
- Flipping

and saved them in the `images` directory.

The original images are `75x75` in dimensions.
We then read all the images and reshape them into `80x80` for easy manipulation.

The read images are split into `Xtrain` and `Xtest` with `test_size=0.05`.

We use the Lab color space (lab) instead of RGB because it is designed to approximate human vision.

We use the `generate_data` function to genrate runtime data augmentations as well.

We make 3 models:

- `model1` which can be used for learning single image features.
- `model2` which uses higher level Conv-Deconv layers but do not give good results.
- `model3` which uses the UpSampling layers

The `model3` gives good results for `1000 epochs` and with `adam` optimizer.

We present the results which we get during our execution of codes.

# tiny-cifar10-experiments
Our project attempts to explore different methods in performing image classification using a small number of training samples.

In our experiments, we use only 100 class-balanced samples from CIFAR-10.

## File Structure
Our workflow uses multiple _Google Colab_ files, as we use the platform to write all our source code.

## Challenge One Directory
The directory contains our Jupyter notebook, in which we tackle few-sample learning through the use of 100 samples only. We incorporte different techniques such as data augmentations, network architecture, regularizer, TTA, and ensemble learning.

## Challenge Two Directory
The directory contains two Jupyter notebooks, one is used to do transfer learning and the other for few-shot learning. We use five candidate nodels pretrained on ImageNet, namely VGG16, GoogleNet, Vision Transformer, ResNext50, and SE-ResNet50. In the few-shot learning notebook, we use prototypical networks to construct a metric-based meta-learning framework.

## Dataset Setup
We use several types of augmentations including classical augmentations, RICAP, and Mixup. We construct our own dataset the TinyCifar10, which has several types of classical augmentations.

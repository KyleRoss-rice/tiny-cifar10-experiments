# -*- coding: utf-8 -*-
"""TinyCIFAR10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oD6FkMoY3Mdez6bylOgGiJDZ6jj7k9EU
"""

import torch
from torch.utils.data import Dataset
import os
import torchvision
from torchvision import datasets
import matplotlib.pyplot as plt
import numpy as np

class TinyCIFAR10(Dataset):
  def __init__(self, root_dir, use_augmented = True, subset_id = 0, train = True, download = True, transform=None):      
    self.url = 'https://github.com/KyleRoss-rice/tiny-cifar10-experiments/raw/main/datasets/tiny-cifar10.tar.gz'

    aug = ''
    if use_augmented:
      aug = '-aug'

    self.training_data_filepath = f'{root_dir}/tiny-cifar10{aug}-training-data.npy'
    self.training_labels_filepath = f'{root_dir}/tiny-cifar10{aug}-training-labels.npy'
    self.validation_data_filepath = f'{root_dir}/tiny-cifar10-validation-data.npy'
    self.validation_labels_filepath = f'{root_dir}/tiny-cifar10-validation-labels.npy'

    self.subset_id = subset_id
    self.root_dir = root_dir

    self.train = train
    self.transform = transform

    if download:
      self.download(root_dir)
    self.load()
  
  def __getitem__(self, index):
    data = self.data[index]
    target = self.targets[index]

    if self.transform is not None:
      data = self.transform(data)
    
    return data, target

  def download(self, root_dir):
    if os.path.exists(f'{root_dir}/tiny-cifar10.tar.gz'):
      print('tiny-cifar10.tar.gz file already downloaded. Will not extract again')
      return
    
    if not os.path.exists(root_dir):
      os.mkdir(root_dir)
    torchvision.datasets.utils.download_and_extract_archive(self.url, self.root_dir, filename='tiny-cifar10.tar.gz')

  def load(self):
    # code needs to be cleaned a bit
    if self.train:
      with open(self.training_data_filepath, 'rb') as f:
        self.data = np.load(f)[self.subset_id]
      with open(self.training_labels_filepath, 'rb') as f:
        self.targets = np.load(f)
    else:
      with open(self.validation_data_filepath, 'rb') as f:
        self.data = np.load(f)
      with open(self.validation_labels_filepath, 'rb') as f:
        self.targets = np.load(f)

#transform = torchvision.transforms.Compose(
#    [torchvision.transforms.ToTensor(),
#     torchvision.transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
#
#dataset = TinyCIFAR10('datasets', subset_id=0, train=False, download = True, transform=transform)
#a, b = dataset[15]
#print(a.shape)
#print(b)
#
#plt.imshow(a.permute(1,2,0))
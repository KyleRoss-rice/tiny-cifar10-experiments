# -*- coding: utf-8 -*-
"""Baseline Model

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N9JKIO_pl1Abi9qTheA4d3k_njRPdciC

# Baseline model
This simple model is meant to establish a baseline, for comparisons. It is the same model provided in Dr. Belilovsky's baseline example.

![](https://raw.githubusercontent.com/KyleRoss-rice/tiny-cifar10-experiments/main/img/baseline.svg)
"""

import torch
import torch.nn as nn

class BaselineModel(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.layers = nn.ModuleList()
        
        self.layers+=[nn.Conv2d(3, 16,  kernel_size=3) , 
                      nn.ReLU(inplace=True)]
        self.layers+=[nn.Conv2d(16, 16,  kernel_size=3, stride=2), 
                      nn.ReLU(inplace=True)]
        self.layers+=[nn.Conv2d(16, 32,  kernel_size=3), 
                      nn.ReLU(inplace=True)]
        self.layers+=[nn.Conv2d(32, 32,  kernel_size=3, stride=2), 
                      nn.ReLU(inplace=True)]
        self.fc = nn.Linear(32*5*5, 10)

    def forward(self, x):
        for i in range(len(self.layers)):
          x = self.layers[i](x)
        x = x.view(-1, 32*5*5)
        x = self.fc(x)
        return x
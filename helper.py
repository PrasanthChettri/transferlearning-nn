import numpy as np
from matplotlib import pyplot as plt
import  torch.nn.functional as F
import torch
from torch import nn

#cannot normalize numpy array using standard library
#writing modular code

class img_lib:
    def __init__(self , img):
        self.img = img
        self.shape = img.shape

    def norm(self):
        mean , std = np.mean(self.img) , np.std(self.img)
        return (self.img-mean)/std

    def get_tensor(self):
        return torch.tensor(self.norm())

    def disp(self):
        plt.imshow(self.img)
        plt.show()

def gram_matrix(feature_maps):
    depth , height , width  = feature_map.shape
    feature_map = feature_map.reshape(depth , height*width)
    #normalization required
    return  (feature_map*feature_map.T)/depth*height*width

#different losses - style and content  meansquared error loss
class StyleLoss(nn.Module):
    def __init__(self, t_img):
        super().__init__()
        #Vanishing Gradient or Explosive Gradients
        #Had to debug this for two hours , still don't know why clipping the backprop did not work
        self.target =t_img.detach()

    def forward(self , i_img):
        self.loss = F.mse_loss(i_img , self.target)
        return i_img

class ContentLoss(nn.Module):
    def __init__(self, t_img):
        super().__init__()
        self.target = t_img.detach()

    def forward(self, i_img):
        self.loss = F.mse_loss(i_img , self.target)
        return i_img

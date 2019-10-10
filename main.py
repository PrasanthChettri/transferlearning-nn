import torch
from torchvision import models 
from helper import *
import cv2

class mainthang():
    def __init__(self):
        self.model = models.vgg16(pretrained =True)
        self.style_img = img_lib(cv2.imread("style.jpg",0))
        self.content_img = img_lib(cv2.imread("content.jpg", 0))
        self.contentloss = ContentLoss(self.content_img.get_tensor())
        self.styleloss = StyleLoss(self.style_img.get_tensor())
        #Feature map extraction from different layers
        self.content_layer  = ['conv_4']
        self.style_layers_default = ['conv_1','conv_2' , 'conv_3' ,'conv_4']

    def get_model(self):
        content_loss =  []
        style_loss = []
        model = nn.Sequential()

    def trainer(self):
        pass

if __name__ == "__main__":
    k = mainthang()
    k.forward()

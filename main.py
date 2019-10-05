import torch
#from torchvision import models 
from helper import *
import cv2

class mainthang():
    def __init__(self):
        #self.model = models.vgg16(pretrained =True)
        self.style_img = img_lib(cv2.imread("style.jpg",0))
        self.content_img = img_lib(cv2.imread("content.jpg", 0))
        self.contentloss = ContentLoss(self.content_img.get_tensor())
        self.styleloss = StyleLoss(self.style_img.get_tensor())
    def forward(self):
        pass

if __name__ == "__main__":
    k = mainthang()
    k.forward()

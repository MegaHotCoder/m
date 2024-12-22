import cv2
from matplotlib import pyplot as plt

img_path = "C:/Users/piosp/OneDrive/english/image.jpg"

class IIMM():
    def __init__(self):
        self.image=None

    def load_img(self,rut):
        self.image = cv2.imread(rut)
    
    def img_resize(self, width, height):
        self.image = cv2.resize(self.image,(width,height))

    def img_show(self):
        cv2.namedWindow('img')
        cv2.imshow("img",self.image)
        cv2.waitKey(0)

img = IIMM()
img.load_img(img_path)
img.img_resize(600,600)
img.img_show()



# img = cv2.imread(img_path)
# cv2.namedWindow('img')
# cv2.imshow("img",img)
# cv2.waitKey(0)
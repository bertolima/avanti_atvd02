import cv2
from matplotlib import pyplot as plt

image_path = 'image.jpg'
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


properties = [("height", image.shape[0]),
              ("width", image.shape[1]),
              ("channels", image.shape[2]),
              ("type", image.dtype),
              ("maxValue", image_gray.max()),
              ("minValue", image_gray.min()),
             ( "medValue", image_gray.mean())]

for propertie in properties:
    print(propertie[0], ": ",propertie[1], sep='')


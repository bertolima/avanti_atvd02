import cv2
from matplotlib import pyplot as plt

image_path = 'image.jpg'
image = cv2.imread(image_path)

#media
med_image = cv2.blur(image,(7,7))

#mediana
median_image = cv2.medianBlur(image, 5)

#gaussiano
gaus_image = cv2.GaussianBlur(image, (5,5), 0)

plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(med_image, cv2.COLOR_BGR2RGB))
plt.title('Filtro da Média')
plt.subplot(1,3,2)
plt.imshow(cv2.cvtColor(median_image, cv2.COLOR_BGR2RGB))
plt.title('Filtro da Mediana')
plt.subplot(1,3,3)
plt.imshow(cv2.cvtColor(gaus_image, cv2.COLOR_BGR2RGB))
plt.title('Filtro Gaussiano')
plt.show()
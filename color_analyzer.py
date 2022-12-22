import numpy as np
import cv2


def create_bar(height, width, color):
    bar = np.zeros((height, width, 3), np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    print(red, green, blue)
    return bar, (red, green, blue)

img = cv2.imread('test_image.jpg')
height, width, _ = np.shape(img)
data = np.reshape(img, (height * width, 3))
data = np.float32(data)

number_clusters = 3
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS
compactness, labels, centers = cv2.kmeans(data, number_clusters, None, criteria, 10, flags)
print('Centers: ', centers)


font = cv2.FONT_HERSHEY_DUPLEX
bars = []
rgb_values = []

for index, row in enumerate(centers):
    bar, rgb = create_bar(200, 200, row)
    bars.append(bar)
    rgb_values.append(rgb)

img_bar = np.hstack(bars)

for index, row in enumerate(rgb_values):
    image = cv2.putText(img_bar, f'{index + 1}. RGB: {row}', (5 + 200 * index, 200 -10),
        font, 0.5, (128, 128, 128), 1, cv2.LINE_AA)
    print(f'{index + 1}. RGB: {row} ')

cv2.imshow('Image', img)
cv2.imshow('Dominant colors', img_bar)
# rgb_values = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# hsl_values = cv2.cvtColor(image, cv2.COLOR_BGR2HSL)
# print('RGB values: ', rgb_values)
# print('HSL values: ', hsl_values)

cv2.waitKey(0)

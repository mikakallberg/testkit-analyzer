# from collections import Counter
# from sklearn.cluster import KMeans
# from matplotlib import colors
# import matplotlib.pyplot as plt
import numpy as np
import cv2


img = cv2.imread('test_image.jpg')
image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


cv2.imshow('Image', img)
print(image)

cv2.waitKey(0)

# def create_bar(height, width, color):
#     bar = np.zeros((height, width, 3), np.uint8)
#     bar[:] = color
#     red, green, blue = int(color[2]), int(color[1]), int(color[0])
#     print(red, green, blue)
#     return bar, (red, green, blue)


# height, width, _ = np.shape(img)
# print(height, width)
# data = np.reshape(img, (height * width, 3))
# data = np.float32(data)

# number_clusters = 3
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_MAX_ITER, 10, 1.0)
# flags = cv2.KMEANS_RANDOM_CENTERS
# compactness, labels, centers = cv2.kmeans(data, number_clusters, None, criteria, 10, flags)
# print(centers)


# font = cv2.FONT_HERSHEY_DUPLEX
# bars = []
# rgb_values = []

# for index, row in enumerate(centers):
#     bar, rgb = create_bar(200, 200, row)
#     bars.append(bar)
#     rgb_values.append(rgb)

# img_bar = np.hstack(bars)

# for index, row in enumerate(rgb_values):
#     image = cv2.putText(img_bar, f'{index + 1}. RGB: {row}', (5 + 200 * index, 200 -10),
#         font, 0.5, (128, 128, 128), 1, cv2.LINE_AA)
#     print(f'{index + 1}. RGB: {row}')


# cv2.imshow('Dominant colors', img_bar)
# plt.imshow(image)s



# def rgb_to_hex(rgb_color):
#     hex_color = "#"
#     for i in rgb_color:
#         i = int(i)
#         hex_color += ("{:02x}".format(i))
#     print(hex_color)
#     return hex_color

# def prep_image(raw_img):
#     modified_img = cv2.resize(raw_img, (900, 600), interpolation = cv2.INTER_AREA)
#     modified_img = modified_img.reshape(modified_img.shape[0]*modified_img.shape[1], 3)
#     return modified_img


# def color_analysis(img):
#     clf = KMeans(n_clusters = 5)
#     color_labels = clf.fit_predict(img)
#     center_colors = clf.cluster_centers_
#     counts = Counter(color_labels)
#     ordered_colors = [center_colors[i] for i in counts.keys()]
#     hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
#     plt.figure(figsize = (12, 8))
#     plt.pie(counts.values(), color_labels = hex_colors, colors = hex_colors)
#     print(hex_colors)

# modified_image = prep_image(image)
# color_analysis(modified_image)
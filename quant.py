import numpy as np
import cv2
import urllib.request


def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urllib.request.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
	# return the image
	return image

def find_k_colors(image, K):
	Z = image.reshape((-1,3))
	# convert to np.float32
	Z = np.float32(Z)
	
	# define criteria, number of clusters(K) and apply kmeans()
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	K = 10
	ret,label,center=cv2.kmeans(Z, K, None, criteria, 50, cv2.KMEANS_RANDOM_CENTERS)
	
	return np.uint8(center),label
	
def show_result(center, K):
	blank_image = np.zeros((K*40,200,3), np.uint8)
	i=0
	for x in center:
		blank_image[i*40:(i+1)*40,:] = x
		i = i+1	
	cv2.imshow('colors',blank_image)
	
#img = cv2.imread('test3.png')
img = url_to_image("http://dev-mam.opgtest.com/uploads/cache/1200/585/5/7/57c5a6803203a4.55147624.png")
resized = cv2.resize(img, (400, (int) (img.shape[0]*400/img.shape[1])))

# Now convert back into uint8, and make original image
center,label = find_k_colors(resized, 10)
res = center[label.flatten()]
res2 = res.reshape((resized.shape))

show_result(center, 10)

cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
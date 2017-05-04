import numpy as np
import cv2
import urllib.request

def bgrToHsv(bgr):
	norm = bgr/255.0
	b = norm[0]
	g = norm[1]
	r = norm[2]
	mx = max(b,g,r)
	mn = min(b,g,r)
	df = mx-mn
	if mx == mn:
		h = 0
	elif mx == r:
		h = 60 * (((g-b)/df)%6)
	elif mx == g:
		h = 60 * ((b-r)/df + 2)
	elif mx == b:
		h = 60 * ((r-g)/df + 4)
	if mx == 0:
		s = 0
	else:
		s = df/mx
	v = mx
	return np.array([h,s,v])

def bgrArrayToHsvArray(colors):
	res = cv2.cvtColor(np.array([colors]), cv2.COLOR_BGR2HSV)[0]
	return res

def rgbToHexString(color):
	y = np.array([[1],[256],[65536]])
	res = hex(np.matmul(color,y)[0])
	return res

def colorsToString(colors):
	res = []
	for color in colors:
		res.append(rgbToHexString(color))
	return res

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
	ret,label,center=cv2.kmeans(Z, K, None, criteria, 50, cv2.KMEANS_RANDOM_CENTERS)

	return np.uint8(center)

def show_result(center, K, name):
	blank_image = np.zeros((K*40,200,3), np.uint8)
	i=0
	for x in center:
		blank_image[i*40:(i+1)*40,:] = x
		i = i+1
	cv2.imshow(name,blank_image)

def get_colors(url, K):
	img = url_to_image(url)
	resized = cv2.resize(img, (400, (int) (img.shape[0]*400/img.shape[1])))
	center = find_k_colors(resized, K)
	return center

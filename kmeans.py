import numpy as np
import cv2

import numpy as np
 
def cluster_points(X, mu):
    clusters  = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                    for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters
 
def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis = 0))
    return newmu
 
def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))
 
import numpy as np
 
def cluster_points(X, mu):
    clusters  = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                    for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters
 
def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis = 0))
    return newmu
 
def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))
 
def find_centers(X, K):
    # Initialize to K random centers
    oldmu = random.sample(X, K)
    mu = random.sample(X, K)
    while not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(oldmu, clusters)
    return(mu, clusters)

def f1(i,j):
	return random.randint(0, 255) + j*i*0

def print_image(n):
	test = cv2.imread("test2.png", 1)
	output = test.copy()
	#resized = output
	resized = cv2.resize(output, (200, (int) (output.shape[0]*200/output.shape[1])))
	arr = np.random.randint(256, size=(3,n))
	#print(arr)
	print ("foreach")
	for x in resized:
		print(x)
	for i in range (resized.shape[1]-1):
		for j in range (resized.shape[0]-1):
			y = resized[j,i]
			min = 3*255**2
			key = y
			for x in np.nditer(arr, flags=['external_loop'], order='F'):
				div = (y[0] - x[0])**2 + (y[1] - x[1])**2 + (y[2] - x[2])**2
				if (div < min):
					min = div
					key = x
			resized[j,i] = key

	cv2.imshow("TEST", test)
	cv2.imshow("SMALL", resized)
	cv2.waitKey(0)

print_image(5)

cv2.destroyAllWindows()
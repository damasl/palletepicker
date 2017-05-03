import quant
import cv2
import numpy as np

center = quant.get_colors("http://autosalon.by/assets/images/news/20151/targa/31.jpg", 4)
y = np.array([[65536],[256],[1]])
for x in center:
    print(x)
    print(hex(np.matmul(x,y)[0]))

    print(quant.rgbToHexString(x))
quant.show_result(center,4)
cv2.waitKey(0)
cv2.destroyAllWindows()

import quant
import cv2
import numpy as np

center = quant.get_colors("https://s00.yaplakal.com/pics/pics_original/9/2/3/8037329.jpg", 4)
colors = center.copy()
colors = np.apply_along_axis(quant.bgrToHsv,1,colors)
quant.show_result(center,4,"res1")
print(colors)

print('\n')
print(center)
for x in center:
    #print(x)
    print(quant.rgbToHexString(x))

quant.show_result(center[np.argsort(colors[:,2])],4,"res2")
quant.show_result(center[np.argsort(colors[:,1])],4,"res3")
quant.show_result(center[np.argsort(colors[:,0])],4,"res4")
cv2.waitKey(0)
cv2.destroyAllWindows()

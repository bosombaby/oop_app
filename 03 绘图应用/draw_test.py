import numpy as np
from PIL import Image

data = np.zeros((20, 20, 3), dtype=np.uint8)
data[:] = [255, 255, 0]

# 二次绘图
data[0:4] = [255, 0, 0]
data[5:10, 5:10] = [0, 255, 0]
data[10:15:2, 15:20:2] = [0, 0,255]

# 翻转数组
data = data[::-1]
img = Image.fromarray(data, 'RGB')
img.save('canvas.png')

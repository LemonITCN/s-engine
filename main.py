import cv2
import numpy as np
import plotCVImg

# 是否查看中间过程
DEBUG = 1
# 标准方格大小
GRID_WIDTH = 40
GRID_HEIGHT = 40
# 标准数字大小
NUM_WIDTH = 20
NUM_HEIGHT = 20
# 数独尺寸
SUDOKU_SIZE = 9

# 存储题目的数组 shape=(9*9, 20*20)
sudoku = np.zeros(shape=(9 * 9, NUM_WIDTH * NUM_HEIGHT))

# 读取图片 read image
img_original = cv2.imread('./questions/01.png')
if DEBUG:
    plotCVImg.plotImg(img_original, "original")

# img_original = cv2.imread('./questions/01.png')
# img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
# img_Blur = cv2.medianBlur(img_gray, 3)
# img_Blur = cv2.GaussianBlur(img_Blur, (3, 3), 0)
import torch
import numpy as np
import cv2

data = cv2.imread("liuhua101.jpg")
cv2.imshow("test1", data)
# 弹出对话框，类似于一直执行，等待手动关闭的exec。
# cv2.waitKey(0)

out = torch.from_numpy(data)
# 将tensor挪到GPU上
out = out.to(torch.device("cuda"))

print("out.is_cuda: ", out.is_cuda)

# 图片翻转
out = torch.flip(out, dims=[0])
# 将张量挪回CPU上，在cpu上才能执行tensor到numpy的转换
out = out.to(torch.device("cpu"))

print("out.is_cuda: ", out.is_cuda)

data = out.numpy()

cv2.imshow("test2", data)

cv2.waitKey(0)
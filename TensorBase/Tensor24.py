import torch

a = torch.rand(2, 2) * 10
print(a)
# 裁剪，值约束, m<= a <=n
a = a.clamp(2, 5)
print(a)
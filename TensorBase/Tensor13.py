import torch

# 广播机制
a = torch.rand(2, 3)
b = torch.rand(3)
c = a + b
print(a)
print(b)
print(c)
print(c.shape)

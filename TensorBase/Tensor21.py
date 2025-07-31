import torch

a = torch.rand(2, 3)
b = torch.rand(2, 3)

print(a, b)
print(torch.dist(a, b, p=1))
print(torch.dist(a, b, p=2))
print(torch.dist(a, b, p=3))
# 范数
print(torch.norm(a))
print(torch.norm(a, p=2))
print(torch.norm(a, p="fro"))
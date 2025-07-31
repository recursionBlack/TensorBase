import torch

a = torch.zeros((2, 4))
b = torch.ones((2, 4))

# 拼接
out = torch.cat((a, b), dim=0)
print(out)
out = torch.cat((a, b), dim=1)
print(out)

# stack

a = torch.linspace(1, 6, 6).view(2, 3)
b = torch.linspace(7, 12, 6).view(2, 3)
print(a, b)
out = torch.stack((a, b), dim=0)
print(out, out.shape)
out = torch.stack((a, b), dim=1)
print(out, out.shape)
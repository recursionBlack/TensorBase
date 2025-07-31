import torch

a = torch.rand((3, 4))
print(a)
# 平分切
out = torch.chunk(a, 2, dim=0)
print(out[0], out[0].shape)
print(out[1], out[1].shape)

print("split")
a = torch.rand((10, 4))
print(a)
# 固定步长切
out = torch.split(a, 3, dim=0)
print(out)
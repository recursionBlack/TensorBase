import torch

a = torch.rand(2, 3)

print(a)

out = torch.reshape(a, (3, 2))

print(out)
# 转置
print(torch.t(out))
# 交换两个维度
print(torch.transpose(out, 0, 1))

a = torch.rand(1, 2, 3)
print(a)
out = torch.transpose(a, 0, 1)
print(out)
print(out.shape)

# 去除维度大小为1的维度
out = torch.squeeze(a)
print(out)
print(out.shape)
# 在最后一个维度上进行扩展
out = torch.unsqueeze(a, -1)
print(out.shape)

# 删除一个维度
out = torch.unbind(a, dim=1)

print(out)

print("flip")
print(a)
print(torch.flip(a, dims=[1, 2]))

# 旋转90度
print("rot90")
print(a)
out = torch.rot90(a)
print(out)
print(out.shape)
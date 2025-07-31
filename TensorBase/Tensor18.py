import torch

a = torch.rand(2, 2)
print(a)
# 统计学方法
print(torch.mean(a, dim=0))
print(torch.sum(a, dim=0))
print(torch.prod(a, dim=0))

print(torch.argmax(a, dim=0))
print(torch.argmin(a, dim=0))

# 标准差，方差
print(torch.std(a))
print(torch.var(a))

# 中位数，众数
print(torch.median(a))
print(torch.mode(a))

# 直方图
a = torch.rand(2, 2) * 10
print(a)
print(torch.histc(a, 6, 0, 0))

a = torch.randint(0, 10, [10])
print(a)
# bincount只能用来处理一维的Tensor
print(torch.bincount(a))

# 统计某一类别样本的个数
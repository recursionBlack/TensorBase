import torch

# 比较
# a = torch.rand(2, 3)
# b = torch.rand(2, 3)
# print(a)
# print(b)
#
# print(torch.eq(a, b))
# print(torch.equal(a, b))
#
# print(torch.ge(a, b))
# print(torch.gt(a, b))
# print(torch.le(a, b))
# print(torch.lt(a, b))

### 排序
# sort
# a = torch.tensor([[1, 4, 4, 3, 5],
#                   [2, 3, 1, 3, 5]])
# print(torch.sort(a, dim=0, descending=False))

# topk
# a = torch.tensor([[2, 4, 3, 1, 5],
#                   [2, 3, 5, 1, 4]])
# print(a.shape)
#
# print(torch.topk(a, k=1, dim=1))
#
# print(torch.kthvalue(a, k=2, dim=0))

# 有界性判断
a = torch.rand(2, 3)
print(a)
print(a/0)
print(torch.isfinite(a))
print(torch.isfinite(a/0))
print(torch.isinf(a/0))
print(torch.isnan(a))

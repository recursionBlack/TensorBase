import torch

# where
a = torch.rand(4, 4)
b = torch.rand(4, 4)
print(a)
print(b)

out = torch.where(a > 0.5, a, b)

print(out)

# index_select
print("index_select")
a = torch.rand(4, 4)
print(a)
# 取了a的第0，3，2行，组成一个新的Tensor
out = torch.index_select(a, dim=0,
                         index=torch.tensor([0, 3, 2]))

print(out, out.shape)

# gather
print("gather")
a = torch.linspace(1, 16, 16).view(4, 4)

print(a)
# 拿到具体某一维度的某个值
# dim=0, out[i, j, k] = input[index[i, j, k], j, k]
# dim=1, out[i, j, k] = input[i, index[i, j, k], k]
# dim=2, out[i, j, k] = input[i, j, index[i, j, k]]
out = torch.gather(a, dim=0, index=torch.tensor([[0, 1, 1, 1],
                                           [0, 1, 2, 2],                                         [0, 1, 3, 3]]))
print(out, out.shape)

# masked_index
print("masked_index")
a = torch.linspace(1, 16, 16).view(4, 4)
mask = torch.gt(a, 8)
print(a)
print(mask)
out = torch.masked_select(a, mask)
print(out, out.shape)

# take
print("take")
a = torch.linspace(1, 16, 16).view(4, 4)

out = torch.take(a, index=torch.tensor([0, 15, 13, 10]))

print(out)

# nonzero
print("nonzero")
a = torch.tensor([[0, 1, 2, 0],
                  [2, 3, 0, 1]])

# 稀疏表示，更加的节省空间
out = torch.nonzero(a)
print(out)
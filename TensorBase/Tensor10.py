import torch

# 获取到当前的设备
# dev = torch.device("cpu")
# 指向我的第一块显卡
dev = torch.device("cuda:0")

a = torch.tensor([2, 2], dtype=torch.float32,
                 device=dev)
print(a)

# 定义一个稀疏的张量
i = torch.tensor([[0, 1, 2], [0, 1, 2]])
v = torch.tensor([1, 2, 3])
sp = torch.sparse_coo_tensor(i, v, (4, 4),
                             dtype=torch.float32,
                             device=dev)
print(sp)

# 转为稠密的张量
td = sp.to_dense()
print(td)
import torch

a = torch.Tensor([[1, 2], [3, 4]])
print(a)
print(type(a))

""" 几种特殊的Tensor """
# 定义维度大小，内容全部为0
b = torch.Tensor(2, 3)
print(b)
print(b.type())

# 全1
c = torch.ones(2, 2)
print(c)
print(c.type())

# 单位矩阵
d = torch.eye(2, 2)
print(d)
print(d.type())

# 全0
e = torch.zeros(2, 2)
print(e)
print(e.type())

# 维度拷贝，但值全零
f = torch.zeros_like(b)
print(f)
print(f.type())

# 维度拷贝，但值全为1
g = torch.ones_like(b)
print(g)
print(g.type())

''' 随机的'''
r1 = torch.rand(2, 2)
print(r1)
print(r1.type())

# 正态分布的
rn = torch.normal(mean=0.0, std=torch.rand(5))
print(rn)
print(rn.type())

# 均匀分布
rj = torch.Tensor(2, 2).uniform_(-1, 1)
print(rj)
print(rj.type())

'''序列'''
# 按步长切片
sa = torch.arange(0, 11, 2)
print(sa)
print(sa.type())

# 等间距，最后一个参数表示要生成几个数
# 拿到等间隔的n个数字
sl = torch.linspace(2, 10, 4)
print(sl)
print(sl.type())

# 生成的是打乱的序列
sr = torch.randperm(10)
print(sr)
print(sr.type())


'''torch对比numpy'''
import numpy as np
na = np.array([[1, 2], [3, 4]])
print(na)

# tensor与numpy有很高的相似性

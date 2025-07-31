import torch
# 随机抽样，通过定义随机种子，保证每次随机生成的结果是一致的
torch.manual_seed(1)

mean = torch.rand(1, 2)
std = torch.rand(1, 2)
print(torch.normal(mean, std))
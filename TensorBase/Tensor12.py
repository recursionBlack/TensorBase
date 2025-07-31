import torch

a = torch.rand(2, 3)
b = torch.rand(2, 3)
print(a)
print(b)

# ## add
# print(a + b)
# print(a.add(b))
# print(torch.add(a, b))
# # add_ 等于+=，会修改a的值
# print(a)
# print(a.add_(b))
# print(a)
#
# # sub
# print(a - b)
# print(torch.sub(a, b))
# print(a.sub(b))
# # sub_ 等于-=，会修改a的值
# print(a)
# print(a.sub_(b))
# print(a)

# # mul
# print("===== mul =====")
# print(a * b)
# print(torch.mul(a, b))
# print(a.mul(b))
# print(a)
# print(a.mul_(b))
# print(a)

# # div
# print("=== div ===")
# print(a/b)
# print(torch.div(a, b))
# print(a.div(b))
# print(a.div_(b))
# print(a)

### matmul

# a = torch.ones(2, 1)
# b = torch.ones(1, 2)
#
# print(a @ b)
# print(a.matmul(b))
# print(torch.matmul(a, b))
# print(torch.mm(a, b))
# print(a.matmul(b))
# print(a.mm(b))

## 高维tensor
# 必须保证最后两个维度可以进行矩阵运算，且前面的维度数字必须一致
# 否则就会报错
# a = torch.ones(1, 2, 3, 4)
# b = torch.ones(1, 2, 4, 3)
# print(a.matmul(b))
# print(a.matmul(b).shape)

## pow幂运算
# a = torch.tensor([1, 2])
# print(torch.pow(a, 3))
# print(a.pow(3))
# print(a**3)
# print(a.pow_(3))

## exp
# a = torch.tensor([1, 2], dtype=torch.float32)
# print(a.type())
# print(torch.exp(a))
# print(torch.exp_(a))
# print(a.exp())
# print(a.exp_())

## log 直接用是以自然常数e为底
# a = torch.tensor([10, 2], dtype=torch.float32)
# print(torch.log(a))
# print(torch.log_(a))
# print(a.log())
# print(a.log_())

## sqrt
a = torch.tensor([10, 2], dtype=torch.float32)
print(torch.sqrt(a))
print(torch.sqrt_(a))
print(a.sqrt())
print(a.sqrt_())
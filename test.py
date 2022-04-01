import torch
import numpy as np
from print_tensor import print_shape as prints

a = torch.tensor([1,2,3])  # single tensor
prints("==>> type(a):\n", type(a))
prints("==>> a:\n", a)
prints("==>> a.shape:\n", a.shape)
# b = [torch.rand(2,3) for i in range(5)]  # list of tensor
# c = (torch.rand(3,4) for i in range(5))  # generator of tensor
# d = {1:torch.randn(4,5), 2:torch.rand(5,6)}  # dict of tensor
# e = (np.array([6,7]) for i in range(5))  # generator of numpy ndarray
# f = (0,1,2,3,4)  # normal variable
# g = torch.tensor([100000])  # one value tensor

# # support following recognizable prefix string
# prints("==>> a.shape: ", a)
# prints("==>> b.shape: ", b)
# prints("==>> c.shape: ", c)
# prints("==>> d.shape: ", d)
# prints("==>> e.shape: ", e)
# prints("==>> f.shape: ", f)
# prints("==>> g.shape: ", g)
# print("".center(50, "-"))
# prints("==>> a: ", a)
# prints("==>> b: ", b)
# prints("==>> c: ", c)
# prints("==>> d: ", d)
# prints("==>> e: ", e)
# prints("==>> f: ", f)
# prints("==>> g: ", g)
# print("".center(50, "-"))
# prints("a:", a)
# prints("b:", b)
# prints("c:", c)
# prints("d:", d)
# prints("e:", e)
# prints("f:", f)
# prints("g:", g)
# print("".center(50, "-"))
# prints("a", a)
# prints("b", b)
# prints("c", c)
# prints("d", d)
# prints("e", e)
# prints("f", f)
# prints("g", g)
# print("".center(50, "-"))
# # You can also just pass in variable
# prints(a)
# prints(b)
# prints(c)
# prints(d)
# prints(e)
# prints(f)
# prints(g)
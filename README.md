# Intro
This package's main propose is to uppack those tensors inside list, tuple, dict, generator, then print their tensor shape, but it can also print a single tensor shape and normal variable. If the tensor has only one value, it will directly print this value.

Currently it only support print the tensor shape of pytorch and numpy. If you are using other deep learning framework, you can go the source code, and modify it locally to fit your needs. Also, it is hard to cover all of cases, if you find this package has bugs, you can directly go the source code to modify it, because the source code is very short and easy to modify...

I also developed an VSCode extension called [Quick-Python-Print](https://github.com/wwdok/Quick-Python-Print) to handle insert, comment, uncomment, delete of print statement, when you can not print nested tentor shape with "Quick-Python-Print", then you can integrate it with "printensor", you just need to replace `print` with `prints`, and remove the `.shape` attribute if it has.

# Usage

1. install
```
pip install printensor
```
2. import
```
(Due to some reason, the installed package name is not same with imported package name, but it is OK.)
from print_tensor import print_shape as prints
```
3. example
```python
import torch
import numpy as np
from print_tensor import print_shape as prints

a = torch.tensor([1,2,3])  # single tensor
b = [torch.rand(2,3) for i in range(5)]  # list of tensor
c = (torch.rand(3,4) for i in range(5))  # generator of tensor
d = {1:torch.randn(4,5), 2:torch.rand(5,6)}  # dict of tensor
e = (np.array([6,7]) for i in range(5))  # generator of numpy ndarray
f = (0,1,2,3,4)  # normal variable
g = torch.tensor([100000])  # one value tensor

# support following recognizable prefix string
prints("==>> a.shape: ", a)
prints("==>> b.shape: ", b)
prints("==>> c.shape: ", c)
prints("==>> d.shape: ", d)
prints("==>> e.shape: ", e)
prints("==>> f.shape: ", f)
prints("==>> g.shape: ", g)
print("".center(50, "-"))
prints("==>> a: ", a)
prints("==>> b: ", b)
prints("==>> c: ", c)
prints("==>> d: ", d)
prints("==>> e: ", e)
prints("==>> f: ", f)
prints("==>> g: ", g)
print("".center(50, "-"))
prints("a:", a)
prints("b:", b)
prints("c:", c)
prints("d:", d)
prints("e:", e)
prints("f:", f)
prints("g:", g)
print("".center(50, "-"))
prints("a", a)
prints("b", b)
prints("c", c)
prints("d", d)
prints("e", e)
prints("f", f)
prints("g", g)
print("".center(50, "-"))
# You can also just pass in variable
prints(a)
prints(b)
prints(c)
prints(d)
prints(e)
prints(f)
prints(g)
```

It will output:
```text
==>> a shape: torch.Size([3])
==>> b[0] shape: torch.Size([2, 3])    
==>> b[1] shape: torch.Size([2, 3])    
==>> b[2] shape: torch.Size([2, 3])    
==>> b[3] shape: torch.Size([2, 3])    
==>> b[4] shape: torch.Size([2, 3])    
==>> c shape: torch.Size([3, 4])       
==>> c shape: torch.Size([3, 4])       
==>> c shape: torch.Size([3, 4])       
==>> c shape: torch.Size([3, 4])       
==>> c shape: torch.Size([3, 4])       
==>> d(key:1) shape: torch.Size([4, 5])
==>> d(key:2) shape: torch.Size([5, 6])
==>> e shape: (2,)
==>> e shape: (2,)
==>> e shape: (2,)
==>> e shape: (2,)
==>> e shape: (2,)
==>> f: (0, 1, 2, 3, 4)
==>> g: tensor([100000])
--------------------------------------------------
==>> a shape: torch.Size([3])
==>> b[0] shape: torch.Size([2, 3])
==>> b[1] shape: torch.Size([2, 3])
==>> b[2] shape: torch.Size([2, 3])
==>> b[3] shape: torch.Size([2, 3])
==>> b[4] shape: torch.Size([2, 3])
==>> d(key:1) shape: torch.Size([4, 5])
==>> d(key:2) shape: torch.Size([5, 6])
==>> f: (0, 1, 2, 3, 4)
==>> g: tensor([100000])
--------------------------------------------------
==>> a shape: torch.Size([3])
==>> b[0] shape: torch.Size([2, 3])
==>> b[1] shape: torch.Size([2, 3])
==>> b[2] shape: torch.Size([2, 3])
==>> b[3] shape: torch.Size([2, 3])
==>> b[4] shape: torch.Size([2, 3])
==>> d(key:1) shape: torch.Size([4, 5])
==>> d(key:2) shape: torch.Size([5, 6])
==>> g: tensor([100000])
--------------------------------------------------
==>> a shape: torch.Size([3])
==>> b[0] shape: torch.Size([2, 3])
==>> b[1] shape: torch.Size([2, 3])
==>> b[2] shape: torch.Size([2, 3])
==>> b[3] shape: torch.Size([2, 3])
==>> b[4] shape: torch.Size([2, 3])
==>> d(key:1) shape: torch.Size([4, 5])
==>> d(key:2) shape: torch.Size([5, 6])
==>> f: (0, 1, 2, 3, 4)
==>> g: tensor([100000])
--------------------------------------------------
==>>  shape: torch.Size([3])
==>> [0] shape: torch.Size([2, 3])
==>> [1] shape: torch.Size([2, 3])
==>> [2] shape: torch.Size([2, 3])
==>> [3] shape: torch.Size([2, 3])
==>> [4] shape: torch.Size([2, 3])
==>> (key:1) shape: torch.Size([4, 5])
==>> (key:2) shape: torch.Size([5, 6])
==>> : (0, 1, 2, 3, 4)
==>> : tensor([100000])
```

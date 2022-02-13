# Intro
This package's main propose is to uppack those tensors inside list, tuple, dict, generator, then print their tensor shape, but it can also print a single tensor shape and normal variable. If the tensor has only one value, it will directly print this value.
Currently it only support print the tensor shape of pytorch and numpy. If you are using other deep learning framework, you can go the source code, and modify it locally to fit your needs.

# Usage

1. install
```
pip install printensor
```
1. import
```
(Due to some reason, the installed package name is not same with imported package name, but it is OK.)
from print_tensor import print_shape as prints
```
2. example
```python
import torch
import numpy as np
from print_tensor import print_shape as prints

a = torch.tensor([1,2,3])  # single tensor
b = [torch.rand(2,3) for i in range(5)]  # list of tensor
c = (torch.rand(3,4) for i in range(5))  # generator of tensor
d = {1:torch.randn(4,5), 2:torch.rand(5,6)}  # dict of tensor
e = (np.array([6,7]) for i in range(5))  # numpy ndarray
f = (0,1,2,3,4)  # normal variable
g = torch.tensor([100000])  # one value tensor

prints("a:", a)
prints("b:", b)
prints("c:", c)
prints("d:", d)
prints("e:", e)
prints("f:", f)
prints("g:", g)
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
```

## More
I also develop a VSCode extension called [Quick-Python-Print](https://github.com/wwdok/Quick-Python-Print), to intergrate them, you can replace `print(` with `prints(`.
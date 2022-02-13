import torch
import numpy as np
from typing import Generator

def print_shape(dataname, data):
    prefix = "==>> "  # you can change this prefix to your preference
    dataname = dataname[::-1].replace(":", "", 1)  #  reverse string and remove last ":"
    if type(data) == torch.Tensor or type(data) == np.ndarray:
        if data.shape in [torch.Size([]), torch.Size([1]), (), (1,)]:
            # if the tensor only has one value, directly print it out.
            print(f"{prefix}{dataname}: {data}")
        else:
            print(f"{prefix}{dataname} shape: {data.shape}")
    elif (type(data) == list or type(data) == tuple) and (type(data[0]) == torch.Tensor or type(data[0]) == np.ndarray):
        for i, d in enumerate(data):
            if d.shape in [torch.Size([]), torch.Size([1]), (), (1,)]:
                print(f"{prefix}{dataname}: {d}")
            else:
                print(f"{prefix}{dataname}[{i}] shape: {d.shape}")
    elif type(data) == dict and (type(data[list(data.keys())[0]]) == torch.Tensor or type(data[list(data.keys())[0]]) == np.ndarray):
        for k, d in data.items():
            if d.shape in [torch.Size([]), torch.Size([1]), (), (1,)]:
                print(f"{prefix}{dataname}(key:{k}): {d}")
            else:
                print(f"{prefix}{dataname}(key:{k}) shape: {d.shape}")
    elif isinstance(data, Generator):
        for d in data:
            if (type(d) == torch.Tensor or type(d) == np.ndarray):
                if d.shape in [torch.Size([]), torch.Size([1]), (), (1,)]:
                    print(f"{prefix}{dataname}: {d}")
                else:
                    print(f"{prefix}{dataname} shape: {d.shape}")
    else:
        # if the data is not related to tensor, directly print it out.
        print(f"{prefix}{dataname}: {data}")

if __name__ == "__main__":
    # for testing
    import torch
    import numpy as np
    a = torch.tensor([1,2,3])  # single tensor
    b = [torch.rand(2,3) for i in range(5)]  # list of tensor
    c = (torch.rand(3,4) for i in range(5))  # generator of tensor
    d = {1:torch.randn(4,5), 2:torch.rand(5,6)}  # dict of tensor
    e = (np.array([6,7]) for i in range(5))  # numpy ndarray
    f = (0,1,2,3,4)  # normal variable
    g = torch.tensor([100000])  # one value tensor

    print_shape("a:", a)
    print_shape("b:", b)
    print_shape("c:", c)
    print_shape("d:", d)
    print_shape("e:", e)
    print_shape("f:", f)
    print_shape("g:", g)
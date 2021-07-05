> * torch max vs numpy max
```shell
import numpy as np
a = np.arange(4).reshape((2,2))
a.max(dim=(0,1))
import torch 
b = torch.from_numpy(a)
b.max(dim=-1)[0].max(dim=-1)[0]
```


> * torch tensor data type convert
```shell
import numpy as np
import torch

a = numpy.random.rand(1, 127) # shape (1, 127)
a = torch.from_numpy(a)

a=a.type(torch.float32)
a=a.float()
```


> * conv
```
output_size = (input_size - kernel_size + 2 * padding) / stride + 1
params = channel_in * channel_out * kernel_size * kernel_size
flops = 2 * channel_in * channel_out * kernel_size * kernel_size * H_output * W_output
```

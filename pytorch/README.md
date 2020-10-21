> * torch max vs numpy max
```shell
import numpy as np
a = np.arange(4).reshape((2,2))
a.max(dim=(0,1))
import torch 
b = torch.from_numpy(a)
b.max(dim=-1)[0].max(dim=-1)[0]
```

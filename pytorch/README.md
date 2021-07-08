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
params = channel_in * channel_out * kernel_size * kernel_size + channel_out(bias)
flops = 2 * channel_in * channel_out * kernel_size * kernel_size * H_output * W_output
```

> * fc
```
params = (channel_in + 1) * channel_out
flops = 2 * channel_in * channel_out
```


> * GIOU
```
IoU = Intersection / Union
GIoU = IoU - (MinAreaRect - Union) / MinAreaRect
```

> * SSIM loss
```
S(x, y) = f(l(x,y), c(x,y), s(x,y)), x stands for prediction, y stands for ground truth.
l stands for luminance, average pixel value.
c stands for contrast, standard deviation.
s stands for structure, (x - average pixel value) / standard deviation and compare similarity.

using sliding window to create different patches
```

> * MAP
```
precision = true positive / (true positive + false positive)
recall = true positive / (true positive + true negative)
f1 score = 2 * precision * recall / (precision + recall)

sort all pred, and calculate precision and recall, calculate the area included
```

> * AUC
```
true positive rate = ture positive / (true positive + false negative)
false positive rate = false positive / (false positive + true negative)

area under curve
```

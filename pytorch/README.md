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

> * res2net
```
1. 1x1 conv to reduce channel;
2. split feature map by scale through channel dimension;
3. y1 = x1; y2 = x2 * (3 x 3); y3 = (x3 + y2) * (3 x 3); y4 = (x4 + y3) * (3 x 3); the latter will get wider receptive field;
4. 1 * 1 conv to recover channel;
5. se block to add weights to different channel.
```

> * rpn
```
1. rpn takes the final convolution layer as input and is used to calculate the objectness scores and the relative offsets. 
2. the dimension is k*2 and K*4
```

> * roi pooling
```
1. the dimension is K*num_channels*fixed_size*fixed_size, num_channels is the final conv layer channel
```

> * yolov5 best possible recall && anchors above threshold
```
thr is defined in hyp['anchor_t'], the default value is 4, k is the default anchors(defined in yaml), wh is the gt bbox in (640 * 360 scale)
def metric(k):  # compute metric k shape (9,2) wh shape (N, 2)
    r = wh[:, None] / k[None] # shape (N,9,2)
    x = torch.min(r, 1. / r).min(2)[0]  # ratio metric shape (N,9)
    best = x.max(1)[0]  # best_x select best matched anchor from the default anchors shape (N)
    aat = (x > 1. / thr).float().sum(1).mean()  # anchors above threshold
    bpr = (best > 1. / thr).float().mean()  # best possible recall
    return bpr, aat
```
> * check if is module
```
isinstance(m, torch.nn.Module)
```

> * lazy module
```
lazy module only needs to set output channel, the input channle is inferrd from input
```

> * pytorch to onnx with multi inputs
```
model = TwoInputModel()

dummy_input_1 = torch.randn(10, 3, 224, 224)
dummy_input_2 = torch.randn(10, 3, 100)

# This is how we would call the PyTorch model
example_output = model(dummy_input_1, dummy_input_2)

# This is how to export it with multiple inputs
torch.onnx.export(model,
        args=(dummy_input_1, dummy_input_2),
        f="alexnet.onnx",
        input_names=["input_1", "input_2"],
        output_names=["output1"])
```


> * shufflenet
```
def channel_shuffle(x: Tensor, groups: int) -> Tensor:
    N, C, H, W = x.shape
    
    # reshape
    x = x.view(N, groups, -1, H, W)

    x = torch.transpose(x, 1, 2).contiguous()

    # flatten
    x = x.view(N, -1, H, W)

    return x
```

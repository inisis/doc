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

> * named_children vs named_modules
```
named_children() Returns an iterator over immediate children modules, yielding both the name of the module as well as the module itself.
named_modules() Returns an iterator over all modules in the network, yielding both the name of the module as well as the module itself.

modules in model should not be identical, or identical module will only show once

import torch.nn as nn

activation = nn.ReLU()

def model(act=activation):
    backbone = []
    for i in range(3):
        backbone.append(activation) # activation # nn.ReLU()

    return nn.Sequential(*backbone)
    

model = model()
for name, module in model.named_modules():
    print(name, module) # 0 ReLU() # 0 ReLU() 1 ReLU() 2 ReLU()

```
> * replace bn
```
class FloatBN(nn.Module):
    def __init__(self, running_mean, running_var, weight, bias, num_batches_tracked): 
        super().__init__()
        self.running_mean = nn.parameter.Parameter(running_mean, requires_grad=False ) 
        self.running_var = nn.parameter.Parameter(running_var, requires_grad=False )
        self.weight = weight
        self.bias = bias
        self.num_batches_tracked = nn.parameter.Parameter(num_batches_tracked, requires_grad=False)

    def forward(self, x):
        x = F.batch_norm(x, self.running_mean, self.running_var, self.weight, self.bias)

        return x
```

> * LayerNorm vs GroupNorm
```
import torch
import torch.nn as nn

channel = 3
input = torch.randn(2, 2, 6, channel)
ln = nn.LayerNorm(channel)

b = input.reshape(-1, channel, 1, 1)
m = nn.GroupNorm(1, channel)

print(m(b).reshape(2, 2, 6, channel))
print(ln(input))
```

> * tensor dtype
```
tensor.type()
```

> * scipy entropy in numpy
```
import numpy as np
from scipy.stats import entropy

p = np.array([1e-4,1e-4,1e-4,1e-4,1e-4,1])
q = np.array([1e-4,1e-4,1e-4,1e-4,1e-4,1e-4])
print("Scipy: ",entropy(p, q))

def KL(a, b):
    a = 1.0*a / np.sum(a, axis=0)
    b = 1.0*b / np.sum(b, axis=0)
    return np.sum(np.where(a != 0, a * np.log(a / b), 0))

print("KL: ", KL(p, q))

def entropy_numpy(a):
    a = 1.0*a / np.sum(a, axis=0)
    sum_ = 0
    for each in a:
        sum_ -= each * np.log(each) / np.log(e)
    return sum_

print("single: ", entropy(p))
print("numpy: ", entropy_numpy(p))
```

> * torch.allclose
```
torch.allclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)
∣input−other∣≤atol+rtol×∣other∣
```

> * calculate flops and params
```
import torch
import torchvision
from thop import profile

model = torchvision.models.resnet50(pretrained=False)

input = torch.randn(1, 3, 224, 224)
flops, params = profile(model, (input,))

print("flops: {:.2f} M, params: {:.2f} M".format(flops / 1e6,  params / (1024*1024)))
```

>* torch fx trace custom function (custom modules cannot be wrapped)
```
import torch
import torch.fx

@torch.fx.wrap
def my_custom_function(x, y):
    return x * x + y * y

def fn_to_be_traced(x, y):
    # When symbolic tracing, the below call to my_custom_function will be inserted into
    # the graph rather than tracing it.
    return my_custom_function(x, y)

f = torch.fx.symbolic_trace(fn_to_be_traced) 
```

> * fb llama
```
wget https://ipfs.io/ipfs/Qmb9y5GCkTG7ZzbBWMu2BXwMkzyCKcUjtEKPpgdZ7GEFKm/65B/consolidated.00.pth
wget https://ipfs.io/ipfs/Qmb9y5GCkTG7ZzbBWMu2BXwMkzyCKcUjtEKPpgdZ7GEFKm/65B/consolidated.01.pth
wget https://ipfs.io/ipfs/Qmb9y5GCkTG7ZzbBWMu2BXwMkzyCKcUjtEKPpgdZ7GEFKm/65B/consolidated.02.pth
wget https://ipfs.io/ipfs/Qmb9y5GCkTG7ZzbBWMu2BXwMkzyCKcUjtEKPpgdZ7GEFKm/65B/consolidated.03.pth
wget https://ipfs.io/ipfs/Qmb9y5GCkTG7ZzbBWMu2BXwMkzyCKcUjtEKPpgdZ7GEFKm/65B/consolidated.04.pth
wget https://ipfs.io/ipfs/Qmb9y5GCkTG7ZzbBWMu2BXwMkzyCKcUjtEKPpgdZ7GEFKm/65B/consolidated.05.pth
wget https://ipfs.io/ipfs/Qmb9y5GCkTG7ZzbBWMu2BXwMkzyCKcUjtEKPpgdZ7GEFKm/65B/consolidated.06.pth
wget https://ipfs.io/ipfs/Qmb9y5GCkTG7ZzbBWMu2BXwMkzyCKcUjtEKPpgdZ7GEFKm/65B/consolidated.07.pth
wget https://ipfs.io/ipfs/Qmb9y5GCkTG7ZzbBWMu2BXwMkzyCKcUjtEKPpgdZ7GEFKm/65B/checklist.chk
wget https://ipfs.io/ipfs/Qmb9y5GCkTG7ZzbBWMu2BXwMkzyCKcUjtEKPpgdZ7GEFKm/65B/params.json
```

> * A100 ddp hang
```
export NCCL_P2P_DISABLE=1
```

> * torch reshape vs view
```
torch reshape will copy tensor
torch view will not, so call contiguous before view
```

> * torch round
```
torch.trunc(), which rounds towards zero, which euals to x.to(torch.int32)
torch.floor(), which rounds down.
torch.ceil(), which rounds up.
torch.round(), this function implements the “round half to even” to break ties when a number is equidistant from two integers (e.g. round(2.5) is 2).
```

> * torch freeze model
```
for name, param in model.named_parameters():
    if not "observer" in name:
        param.requires_grad = False

optimizer = torch.optim.SGD(filter(lambda p: p.requires_grad, model.parameters()),
                            lr=0.01, momentum=0.9, weight_decay=0.0001
)
```

> * mpi run ddp
```
mpirun -np 4 -H 192.168.0.254:2,192.168.0.253:2 -x MASTER_ADDR=192.168.0.254 -x MASTER_PORT=1234 -x PATH -bind-to none -map-by slot -mca pml ob1 -mca btl ^openib python3 main.py --backend=nccl
```

> * nccl rdma setting
```
NCCL_IB_HCA=mlx5_1:1,mlx5_2:1,mlx5_3:1,mlx5_4:1
NCCL_IB_DISABLE=0
NCCL_SOCKET_IFNAME=eth0
NCCL_IB_GID_INDEX=3
NCCL_NET_GDR_LEVEL=1
NCCL_IB_TIMEOUT=23
NCCL_IB_RETRY_CNT=7
```

> * grpc server c++ link lib
```

```

> * instancenorm vs groupnorm vs layernorm
```

```

> * transform ToTensor vs PILToTensor
```
ToTensor will normalize but PILToTensor won't
```

> * pytorch qdq
```
use graphsurgeon instead to optimize it
```

> * 
```

```

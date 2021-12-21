import torch
inputs = torch.tensor([[[[1., 2.],
                         [3., 4.]]]])
print(inputs.shape)                        
fc = torch.nn.Linear(4, 2)

weights = torch.tensor([[1.1, 1.2, 1.3, 1.4],
                        [1.5, 1.6, 1.7, 1.8]])
bias = torch.tensor([1.9, 2.0])
fc.weight.data = weights
fc.bias.data = bias

conv = torch.nn.Conv2d(in_channels=1,
                       out_channels=2,
                       kernel_size=(1, 1))
print(conv.weight.data.shape)                       
conv.weight.data = weights.view(2, 1, 2, 2)
conv.bias.data = bias
print(conv(inputs))
print(conv(inputs).shape)



print(fc(inputs.view(-1, 4)))
print(fc(inputs.view(-1, 4)).shape)

conv = torch.nn.Conv2d(in_channels=1,
                       out_channels=2,
                       kernel_size=inputs.squeeze(dim=(0)).squeeze(dim=(0)).size())
conv.weight.data = weights.view(2, 1, 2, 2)
conv.bias.data = bias
print(conv(inputs))
print(conv(inputs).shape)
> * caffe modify model weights
```
net.params['conv1'][0].data[...] = np.ones((16, 32, 3, 3))
```

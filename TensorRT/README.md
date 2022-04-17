> * TensorRT hackthon
```
polygraphy run ModifyEncoder.onnx --trt --onnxrt --verbose --workspace=12G --trt-min-shapes speech:[1,16,80] speech_lengths:[1] --trt-opt-shapes speech:[4,256,80] speech_lengths:[4] --trt-max-shapes speech:[16,256,80] speech_lengths:[16]
```

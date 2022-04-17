> * TensorRT hackthon wenet encoder
```
polygraphy run ModifyEncoder.onnx --trt --onnxrt --verbose --workspace=12G --trt-min-shapes speech:[1,16,80] speech_lengths:[1] --trt-opt-shapes speech:[4,256,80] speech_lengths:[4] --trt-max-shapes speech:[64,256,80] speech_lengths:[64] --input-shapes speech:[64,256,80] speech_lengths:[64] --save-engine encoder.plan
```

> * TensorRT hackthon wenet encoder
```
polygraphy run ModifyEncoder.onnx --trt --onnxrt --verbose --workspace=24G --fp16 --trt-min-shapes speech:[1,16,80] speech_lengths:[1] --trt-opt-shapes speech:[4,256,80] speech_lengths:[4] --trt-max-shapes speech:[64,256,80] speech_lengths:[64] --input-shapes speech:[64,256,80] speech_lengths:[64] --save-engine encoder.plan
```

> * TensorRT hackthon wenet decoder
```
polygraphy run decoder.onnx --onnxrt --trt --workspace 24G --fp16 --save-engine=/target/decoder.plan --data-loader-script data_loader.py --atol 1e-3 --rtol 1e-3 --verbose --trt-min-shapes encoder_out:[1,16,256] encoder_out_lens:[1] hyps_pad_sos_eos:[1,10,64] hyps_lens_sos:[1,10] ctc_score:[1,10] --trt-opt-shapes encoder_out:[64,16,256] encoder_out_lens:[64] hyps_pad_sos_eos:[64,10,64] hyps_lens_sos:[64,10] ctc_score:[64,10] --trt-max-shapes encoder_out:[64,256,256] encoder_out_lens:[64] hyps_pad_sos_eos:[64,10,64] hyps_lens_sos:[64,10] ctc_score:[64,10]
```

> * custom data_loader, data_loader.py
```
import numpy as np

def load_data():
    ioData = np.load('/workspace/data/decoder-1-256.npz')
    return [ioData]
```

> * nsys profile python
```
nsys profile -w true -t cuda,nvtx,osrt,cudnn,cublas -s none -o nsight_report -f true -x true python /workspace/testEncoderAndDecoder.py
```

> * int8 calibrator
```
import os
import numpy as np
from cuda import cudart
import tensorrt as trt

class MyCalibrator(trt.IInt8EntropyCalibrator2):

    def __init__(self, calibrationCount, inputShape, cacheFile):
        trt.IInt8EntropyCalibrator2.__init__(self)
        self.calibrationCount = calibrationCount
        self.shape = inputShape
        self.buffeSize = trt.volume(inputShape) * trt.float32.itemsize
        self.cacheFile = cacheFile
        _, self.dIn = cudart.cudaMalloc(self.buffeSize)
        self.count = 0

    def __del__(self):
        cudart.cudaFree(self.dIn)

    def get_batch_size(self):  # do NOT change name
        return self.shape[0]

    def get_batch(self, nameList=None, inputNodeName=None):  # do NOT change name
        if self.count < self.calibrationCount:
            self.count += 1
            data = np.ascontiguousarray(np.random.rand(np.prod(self.shape)).astype(np.float32).reshape(*self.shape)*200-100)
            cudart.cudaMemcpy(self.dIn, data.ctypes.data, self.buffeSize, cudart.cudaMemcpyKind.cudaMemcpyHostToDevice)
            return [int(self.dIn)]
        else:
            return None

    def read_calibration_cache(self):  # do NOT change name
        if os.path.exists(self.cacheFile):
            print("Succeed finding cahce file: %s" % (self.cacheFile))
            with open(self.cacheFile, "rb") as f:
                cache = f.read()
                return cache
        else:
            print("Failed finding int8 cache!")
            return

    def write_calibration_cache(self, cache):  # do NOT change name
        with open(self.cacheFile, "wb") as f:
            f.write(cache)
        print("Succeed saving int8 cache!")

if __name__ == "__main__":
    cudart.cudaDeviceSynchronize()
    m = MyCalibrator(5, (1, 1, 28, 28), "./int8.cache")
    m.get_batch("FakeNameList")
```

> * supportsFormatCombination
```
return ((inOut[pos].type == nvinfer1::DataType::kHALF) && (inOut[pos].format == nvinfer1::PluginFormat::kLINEAR)); # fp16 and NCHW
```

> * save onnx output
```
polygraphy run /workspace/encoder.onnx --onnxrt --verbose --workspace=12G --trt-min-shapes speech:[1,16,80] speech_lengths:[1] --trt-opt-shapes speech:[4,256,80] speech_lengths:[4] --trt-max-shapes speech:[64,256,80] speech_lengths:[64] --input-shapes speech:[64,256,80] speech_lengths:[64] --save-engine encoder.plan --onnx-outputs 646 613 603 --save-outputs output.txt --seed 0
```

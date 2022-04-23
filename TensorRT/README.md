> * TensorRT hackthon wenet encoder
```
polygraphy run ModifyEncoder.onnx --trt --onnxrt --verbose --workspace=24G --tf32 --trt-min-shapes speech:[1,16,80] speech_lengths:[1] --trt-opt-shapes speech:[4,256,80] speech_lengths:[4] --trt-max-shapes speech:[64,256,80] speech_lengths:[64] --input-shapes speech:[64,256,80] speech_lengths:[64] --save-engine encoder.plan
```

> * TensorRT hackthon wenet decoder
```
polygraphy run decoder.onnx --onnxrt --trt --workspace 24G --tf32 --save-engine=/target/decoder.plan --data-loader-script data_loader.py --atol 1e-3 --rtol 1e-3 --verbose --trt-min-shapes encoder_out:[1,16,256] encoder_out_lens:[1] hyps_pad_sos_eos:[1,10,64] hyps_lens_sos:[1,10] ctc_score:[1,10] --trt-opt-shapes encoder_out:[64,16,256] encoder_out_lens:[64] hyps_pad_sos_eos:[64,10,64] hyps_lens_sos:[64,10] ctc_score:[64,10] --trt-max-shapes encoder_out:[64,256,256] encoder_out_lens:[64] hyps_pad_sos_eos:[64,10,64] hyps_lens_sos:[64,10] ctc_score:[64,10]
```

> * custom data_loader, data_loader.py
```
import numpy as np

def load_data():
    ioData = np.load('/workspace/data/decoder-1-256.npz')
    return [ioData]
```

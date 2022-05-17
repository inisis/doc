> * change onnx input shape
```
import onnx
model = onnx.load('./encoder.onnx' )
dim_proto_0 = model.graph.input[0].type.tensor_type.shape.dim[0]
dim_proto_0.dim_param = '1'
onnx.save(model, './encder_sim.onnx')
```

> * onnx datatype
```
  483 message TensorProto {
  484   enum DataType {
  485     UNDEFINED = 0;
  486     // Basic types.
  487     FLOAT = 1;   // float
  488     UINT8 = 2;   // uint8_t
  489     INT8 = 3;    // int8_t
  490     UINT16 = 4;  // uint16_t
  491     INT16 = 5;   // int16_t
  492     INT32 = 6;   // int32_t
  493     INT64 = 7;   // int64_t
  494     STRING = 8;  // string
  495     BOOL = 9;    // bool
  496 
  497     // IEEE754 half-precision floating-point format (16 bits wide).
  498     // This format has 1 sign bit, 5 exponent bits, and 10 mantissa bits.
  499     FLOAT16 = 10;
  500 
  501     DOUBLE = 11;
  502     UINT32 = 12;
  503     UINT64 = 13;
  504     COMPLEX64 = 14;     // complex with float32 real and imaginary components
  505     COMPLEX128 = 15;    // complex with float64 real and imaginary components
  506 
  507     // Non-IEEE floating-point format based on IEEE754 single-precision
  508     // floating-point number truncated to 16 bits.
  509     // This format has 1 sign bit, 8 exponent bits, and 7 mantissa bits.
  510     BFLOAT16 = 16;
  511 
  512     // Future extensions go here.
  513   }
```

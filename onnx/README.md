> * change onnx input shape
```
import onnx
model = onnx.load('./encoder.onnx' )
dim_proto_0 = model.graph.input[0].type.tensor_type.shape.dim[0]
dim_proto_0.dim_param = '1'
onnx.save(model, './encder_sim.onnx')
```

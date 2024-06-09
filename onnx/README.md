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
 0: onnx.TensorProto.UNDEFINED
 1: onnx.TensorProto.FLOAT
 2: onnx.TensorProto.UINT8
 3: onnx.TensorProto.INT8
 4: onnx.TensorProto.UINT16
 5: onnx.TensorProto.INT16
 6: onnx.TensorProto.INT32
 7: onnx.TensorProto.INT64
 8: onnx.TensorProto.STRING
 9: onnx.TensorProto.BOOL
10: onnx.TensorProto.FLOAT16
11: onnx.TensorProto.DOUBLE
12: onnx.TensorProto.UINT32
13: onnx.TensorProto.UINT64
14: onnx.TensorProto.COMPLEX64
15: onnx.TensorProto.COMPLEX128
16: onnx.TensorProto.BFLOAT16
17: onnx.TensorProto.FLOAT8E4M3FN
18: onnx.TensorProto.FLOAT8E4M3FNUZ
19: onnx.TensorProto.FLOAT8E5M2
20: onnx.TensorProto.FLOAT8E5M2FNUZ
21: onnx.TensorProto.UINT4
22: onnx.TensorProto.INT4
```

> * onnx runtime extension
```
pip install onnxruntime-extensions
```

> * compare onnx model
```
import onnx
import argparse

def extract_ops(model, op_type):
    """Extract operation names of a given type from an ONNX model."""
    ops = set()
    for node in model.graph.node:
        if node.op_type == op_type:
            ops.add(node.name)
    return ops

def compare_ops(model_path1, model_path2, op_type):
    """Compare operations of a given type between two ONNX models."""
    # Load the ONNX models
    model1 = onnx.load(model_path1)
    model2 = onnx.load(model_path2)

    # Extract operations
    ops1 = extract_ops(model1, op_type)
    ops2 = extract_ops(model2, op_type)

    # Find intersection and differences
    intersection = ops1.intersection(ops2)
    only_in_model1 = ops1 - ops2
    only_in_model2 = ops2 - ops1

    # Print the summary
    print(f"Intersection of {op_type} operations:")
    for op in intersection:
        print(op)

    print(f"\n{op_type} operations only in model 1:")
    for op in only_in_model1:
        print(op)

    print(f"\n{op_type} operations only in model 2:")
    for op in only_in_model2:
        print(op)

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Compare specific operations in two ONNX models.')
    parser.add_argument('model1', type=str, help='Path to the first ONNX model')
    parser.add_argument('model2', type=str, help='Path to the second ONNX model')
    parser.add_argument('--op_type', type=str, default='Conv', help='Type of operation to compare (default: Conv)')
    
    args = parser.parse_args()

    # Compare the operations
    compare_ops(args.model1, args.model2, args.op_type)

```

> * onnx common subexpression elimination
```

```

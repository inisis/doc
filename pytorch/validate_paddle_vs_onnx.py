import argparse
import numpy as np

import paddle
import paddle.fluid as fluid
import onnx

import onnxruntime as rt

paddle.enable_static()

def parse_args():
    # Read arguments: path to model.
    parser = argparse.ArgumentParser("Use dummy data in the interval [a, b] "
                                     "as inputs to verify the conversion.")
    parser.add_argument(
        "--model_dir",
        required=True,
        help="The path to PaddlePaddle Fluid model.")
    parser.add_argument(
        "--model_filename",
        required=True,
        help="The path to PaddlePaddle Fluid model.")
    parser.add_argument(
        "--params_filename",
        required=True,
        help="The path to PaddlePaddle Fluid model.")
    parser.add_argument(
        "--onnx_model", required=True, help="The path to ONNX model.")
    parser.add_argument(
        "--a",
        type=float,
        default=0.0,
        help="Left boundary of dummy data. (default: %(default)f)")
    parser.add_argument(
        "--b",
        type=float,
        default=1.0,
        help="Right boundary of dummy data. (default: %(default)f)")
    parser.add_argument(
        "--batch_size",
        type=int,
        default=1,
        help="Batch size. (default: %(default)d)")
    parser.add_argument(
        "--expected_decimal",
        type=int,
        default=5,
        help="The expected decimal accuracy. (default: %(default)d)")
    parser.add_argument(
        "--backend",
        type=str,
        choices=['caffe2', 'tensorrt'],
        default='caffe2',
        help="The ONNX backend used for validation. (default: %(default)s)")
    args = parser.parse_args()
    return args

def freeze(model_def):
    inputs = model_def.graph.input
    name_to_input = {}
    for input in inputs:
        name_to_input[input.name] = input

    for initializer in model_def.graph.initializer:
        if initializer.name in name_to_input:
            inputs.remove(name_to_input[initializer.name])
    
    return model_def

def validate(args):
    place = fluid.CPUPlace()
    exe = fluid.Executor(place)

    [program, feed_var_names, fetch_vars] = fluid.io.load_inference_model(
        args.model_dir,
        exe,
        model_filename=args.model_filename,
        params_filename=args.params_filename)

    input_shapes = [
        program.global_block().var(var_name).shape
        for var_name in feed_var_names
    ]
    input_shapes = [
        shape if shape[0] > 0 else (args.batch_size, ) + shape[1:]
        for shape in input_shapes
    ]
    # Generate dummy data as inputs
    inputs = [
        np.random.random(shape).astype("float32")
        for shape in input_shapes
    ]

    # Fluid inference 
    fluid_results = exe.run(program,
                            feed=dict(zip(feed_var_names, inputs)),
                            fetch_list=fetch_vars)

    # Remove these prints some day
    print("Inference results for fluid model:")
    print(fluid_results)
    print('\n')

    # ONNX inference, using caffe2 as the backend
    onnx_model = onnx.load(args.onnx_model)
    onnx_model = freeze(onnx_model)
    onnx.save(onnx_model, args.onnx_model)
    sess = rt.InferenceSession(onnx_model.SerializeToString())
    onnx_outname = [output.name for output in sess.get_outputs()]
    onnx_rt_dict = {}
    for input_name in sess.get_inputs():
        onnx_rt_dict['x'] = inputs[0]
    res = sess.run(onnx_outname, onnx_rt_dict)

    print("Inference results for ONNX model:")
    print(res)
    print('\n')

    for ref, hyp in zip(fluid_results, res):
        np.testing.assert_almost_equal(ref, hyp, decimal=args.expected_decimal)
    print("The exported model achieves {}-decimal precision.".format(
        args.expected_decimal))


if __name__ == "__main__":
    args = parse_args()
    validate(args)

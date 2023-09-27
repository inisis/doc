> * print numpy array without scientific notation
```
np.set_printoptions(suppress=True)
```

> * numpy store int32 sum with fp32 will lead to precision loss
```
import numpy as np

# 定义int32变量
a = np.int32(2147483647)  # 最大的int32值
b = np.int32(1000000000)  # 一个较大的int32值

# 计算和并将结果存储在fp32变量中
sum_int32 = a + b
sum_fp32 = np.float32(sum_int32)
sum_fp64 = np.float64(sum_int32)

# 输出结果
print("int32 sum:", sum_int32)
print("fp32 sum:", sum_fp32)
print("fp64 sum:", sum_fp64)
```

>

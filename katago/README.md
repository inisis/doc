> * katago weights
```
kata1-b40c256-s10545697536-d2570360618, b means blocks and c means channel
```

> * How to build
```
wget https://github.com/Kitware/CMake/releases/download/v3.18.2/cmake-3.18.2-Linux-x86_64.tar.gz
tar zxvf cmake-3.18.2-Linux-x86_64.tar.gz
mv cmake-3.18.2-Linux-x86_64 /opt/cmake-3.18.2
ln -sf /opt/cmake-3.18.2/bin/* /usr/bin/

apt update && apt-get install libzip-dev git -y
unzip KataGo.zip
cd KataGo/cpp
tar zxvf cmake-3.18.2-Linux-x86_64.tar.gz
mv cmake-3.18.2-Linux-x86_64 /opt/cmake-3.18.2
ln -sf /opt/cmake-3.18.2/bin/* /usr/bin/
tar zxvf TensorRT-8.0.0.3.Linux.x86_64-gnu.cuda-11.0.cudnn8.2.tar.gz 
cp -rf TensorRT-8.0.0.3/include/* /usr/local/cuda/include/
cp -rf TensorRT-8.0.0.3/lib/* /usr/local/cuda/lib64/
mkdir build_cuda; cd build_cuda
cmake .. -DUSE_BACKEND=CUDA
make -j32
./katago benchmark -config ../configs/match_example.cfg -model ../tests/models/g170-b6c96-s175395328-d26788732.bin.gz -v 5000 -t 32,48,64,80,96,112,128

mkdir build_trt; cd build_trt
cmake .. -DUSE_BACKEND=TENSORRT
make -j32
./katago benchmark -config ../configs/match_example.cfg -model ../tests/models/g170-b6c96-s175395328-d26788732.bin.gz -v 5000 -t 32,48,64,80,96,112,128

cd ~/work/data/bins/katago-1.9.1/
./katago benchmark -config ../../configs/default_gtp.cfg  -model ../../weights/40b.bin.gz -v 5000 -t 32,48,64,80,96,112,128
```
> * How to use certain kata-weight
```
--kata-weight
```

> * docker run
```
docker run -it --name=KATAGO --gpus all -v /mnt/weights:/katago/data/weights -e USER_NAME=desmond -e USER_PASSWORD=12345678 -e BACKEND=TENSORRT -e WEIGHTS=kata1-b60c320-s7010139136-d3130207575.bin.gz -e NUMSEARCHTHREADS=32 -e LD_LIBRARY_PATH=/usr/local/cuda/lib64 --entrypoint /etc/entrypoint.sh katago:11.8-cudnn8-runtime-ubuntu18.04-tenosrrt8.6-nopencl-stable
```

> * gen trt cache for different GPUs
```
weights=$(find /katago/data/weights -type f)
GPU_NAME=$(nvidia-smi -q | grep "Product Name" | head -n 1 | cut -d":" -f2 | xargs)
echo $GPU_NAME

if [[ "$GPU_NAME" == *"NVIDIA GeForce RTX 3090"* ]]
then
        base=96
elif [[ "$GPU_NAME" == *"NVIDIA A100-PCIE-40GB"* ]]
then
        base=80
else
        echo unsuported gpu card: $GPU_NAME
        exit -1
fi

for weight in ${weights};
do
    for i in 1 2 4 8;
        do
            echo /usr/bin/katago_trt benchmark -config /configs/$i/default_gtp.cfg  -model $weight -v 5000 -t $((i * base))
            /usr/bin/katago_trt benchmark -config /configs/$i/default_gtp.cfg  -model $weight -v 5000 -t $((i * base))
        done
done
```

> * centos7 install gcc 7
```
yum install centos-release-scl
yum install devtoolset-7-gcc-c++

scl enable devtoolset-7 bash
```

![image](https://github.com/user-attachments/assets/b735e902-cdad-4cc6-ae45-21442c4705d7)> * show gpu vendor
```shell
lspci -vnn | grep VGA -A 12
```

> * set gpu power limit
```shell
nvidia-smi -i 2 -pl 125
```

> * get gpu power info
```shell
nvidia-smi -q -d POWER
```
> * ppa china mirror
```shell
replace http://ppa.launchpad.net/graphics-drivers/ppa/ubuntu with https://launchpad.proxy.ustclug.org/graphics-drivers/ppa/ubuntu
```
> * install nvidia gpu driver
```
1. download nvidia driver(.run appendix)

2. Ctrl+Alt+F1

3. sudo service lightdm stop

4. sudo bash ×××.run

5. sudo modprobe -r nvidia

6. lsof /dev/nvidia*

sudo vim /etc/modprobe.d/blacklist.conf

blacklist nouveau

sudo update-initramfs -u
```
> * find gpu process
```shell
sudo fuser -v /dev/nvidia*
```
> * uninstall nvidia
```shell
nvidia-uninstall
```
> * kill gnome-shell autorestart
```
(base) vipuser@ubuntu1804:~$ sudo lsof -n -w  /dev/nvidia*
COMMAND     PID USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
gnome-she 11861  gdm   12u   CHR 195,255      0t0  457 /dev/nvidiactl
gnome-she 11861  gdm   13u   CHR   195,0      0t0  458 /dev/nvidia0
gnome-she 11861  gdm   14u   CHR   195,0      0t0  458 /dev/nvidia0

sudo service gdm stop
```

> * check nvidia device
```
lspci | grep -i nvidia
```

> * CUDA_HOME
```
export CUDA_HOME=/usr/local/cuda
export PATH=${CUDA_HOME}/bin:${PATH}
export LD_LIBRARY_PATH=${CUDA_HOME}/lib64:$LD_LIBRARY_PATH
```

> * device order
```
export CUDA_DEVICE_ORDER=PCI_BUS_ID
```

> * A100 Nvlink
```
sudo apt install nvidia-driver-535-server
sudo apt install cuda-drivers-fabricmanager-535
sudo service nvidia-fabricmanager restart
sudo nvidia-smi -pm 1
sudo nvidia-smi -mig 0
sudo systemctl status nvidia-fabricmanager
sudo nvidia-smi topo -m
```

> * nsys-ui in docker
```
sudo apt-get install libxcb-xinerama0
sudo apt-get install libxkbcommon-x11-0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-xinerama0 libxcb-xfixes0 libegl1-mesa
sudo apt install openjdk-8-jre
```

> * A100-40GB set clock
```
sudo nvidia-smi -q -d SUPPORTED_CLOCKS
sudo nvidia-smi -pm 1 && sudo nvidia-smi -ac 1215,1410
```

> * nvidia lock memory clock and graph clock
```
nvidia-smi -lmc 10501
nvidia-smi -lgc 3105
```

> * query pcie
```
nvidia-smi  --format=csv --query-gpu=pcie.link.gen.current,pcie.link.width.current
```

> * nv profile
```
nsys ncu
```

> * GPU benchmark using torch
```
import torch
import time

def stress_test_matmul(
    size=8192,
    iterations=100,
    dtype=torch.float16,
    use_streams=False,
):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")
    print(f"Tensor size: {size}x{size}, dtype: {dtype}, iterations: {iterations}")

    # Allocate large tensors on pinned host memory
    a_cpu = torch.randn(size, size, dtype=dtype).pin_memory()
    b_cpu = torch.randn(size, size, dtype=dtype).pin_memory()

    # Move to GPU
    a = a_cpu.to(device, non_blocking=True)
    b = b_cpu.to(device, non_blocking=True)

    torch.cuda.empty_cache()
    torch.cuda.reset_peak_memory_stats(device)

    # Optional: prepare CUDA streams
    streams = [torch.cuda.Stream(device=device) for _ in range(4)] if use_streams else [None]

    total_time = 0.0
    while(1):
        stream = streams[0]
        if stream:
            with torch.cuda.stream(stream):
                start = torch.cuda.Event(enable_timing=True)
                end = torch.cuda.Event(enable_timing=True)
                start.record()
                _ = torch.matmul(a, b)
                end.record()
                stream.synchronize()
        else:
            start = torch.cuda.Event(enable_timing=True)
            end = torch.cuda.Event(enable_timing=True)
            start.record()
            _ = torch.matmul(a, b)
            end.record()
            torch.cuda.synchronize()
        elapsed = start.elapsed_time(end)  # ms
        total_time += elapsed

    # Show peak memory usage
    peak_mem = torch.cuda.max_memory_allocated(device) / 1024**2
    print(f"\nAverage time per matmul: {total_time / iterations:.2f} ms")
    print(f"Peak memory allocated: {peak_mem:.2f} MB")

if __name__ == "__main__":
    stress_test_matmul(
        size=8192,           # Matrix size
        iterations=100,      # Number of iterations
        dtype=torch.float16, # Use float16 to enable Tensor Cores
        use_streams=True     # Stress test with CUDA streams
    )
```

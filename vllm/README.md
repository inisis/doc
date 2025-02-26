> * Deepseek R1
```
Master
bash run_cluster.sh  vllm/vllm-openai 10.10.40.217 --head /data/LM/hf/DeepSeek-R1-bf16/ -e TP_SOCKET_IFNAME=bond0.45 -e GLOO_SOCKET_IFNAME=bond0.45 -e NCCL_SOCKET_IFNAME=bond0.45 -e VLLM_HOST_IP=10.10.40.217 

Slave
bash run_cluster.sh  vllm/vllm-openai 10.10.40.217 --worker /data/LM/hf/DeepSeek-R1-bf16/ -e TP_SOCKET_IFNAME=bond0.45 -e GLOO_SOCKET_IFNAME=bond0.45 -e NCCL_SOCKET_IFNAME=bond0.45 -e VLLM_HOST_IP=10.10.40.210
bash run_cluster.sh  vllm/vllm-openai 10.10.40.217 --worker /data/LM/hf/DeepSeek-R1-bf16/ -e TP_SOCKET_IFNAME=bond0.45 -e GLOO_SOCKET_IFNAME=bond0.45 -e NCCL_SOCKET_IFNAME=bond0.45 -e VLLM_HOST_IP=10.10.40.209
bash run_cluster.sh  vllm/vllm-openai 10.10.40.217 --worker /data/LM/hf/DeepSeek-R1-bf16/ -e TP_SOCKET_IFNAME=bond0.45 -e GLOO_SOCKET_IFNAME=bond0.45 -e NCCL_SOCKET_IFNAME=bond0.45 -e VLLM_HOST_IP=10.10.40.131
```

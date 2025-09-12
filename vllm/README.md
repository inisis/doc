> * Deepseek R1
```
Master
bash run_cluster.sh  vllm/vllm-openai 10.10.40.217 --head /data/LM/hf/DeepSeek-R1-bf16/ -e TP_SOCKET_IFNAME=bond0.45 -e GLOO_SOCKET_IFNAME=bond0.45 -e NCCL_SOCKET_IFNAME=bond0.45 -e VLLM_HOST_IP=10.10.40.217 

Slave
bash run_cluster.sh  vllm/vllm-openai 10.10.40.217 --worker /data/LM/hf/DeepSeek-R1-bf16/ -e TP_SOCKET_IFNAME=bond0.45 -e GLOO_SOCKET_IFNAME=bond0.45 -e NCCL_SOCKET_IFNAME=bond0.45 -e VLLM_HOST_IP=10.10.40.210
bash run_cluster.sh  vllm/vllm-openai 10.10.40.217 --worker /data/LM/hf/DeepSeek-R1-bf16/ -e TP_SOCKET_IFNAME=bond0.45 -e GLOO_SOCKET_IFNAME=bond0.45 -e NCCL_SOCKET_IFNAME=bond0.45 -e VLLM_HOST_IP=10.10.40.209
bash run_cluster.sh  vllm/vllm-openai 10.10.40.217 --worker /data/LM/hf/DeepSeek-R1-bf16/ -e TP_SOCKET_IFNAME=bond0.45 -e GLOO_SOCKET_IFNAME=bond0.45 -e NCCL_SOCKET_IFNAME=bond0.45 -e VLLM_HOST_IP=10.10.40.131
```

> * lmeval
```
git clone https://github.com/EleutherAI/lm-evaluation-harness.git
cd lm-evaluation-harness; pip install .

lm_eval --model vllm --model_args pretrained=/root/.cache/huggingface/,trust_remote_code=True,tensor_parallel_size=16,enforce_eager=True,max_length=2048,gpu_memory_utilization=0.7 --task arc_challenge --output_path output/ --log_samples

lm_eval --model vllm --model_args pretrained=/data/LM/hf/DeepSeek-R1-bf16,trust_remote_code=True,tensor_parallel_size=32,enforce_eager=True,max_length=2048,gpu_memory_utilization=0.7 --task arc_challenge --output_path output/ --log_samples
```

> * vllm infer with logits
```
return llm.generate(
    prompt_token_ids=requests,
    sampling_params=sampling_params,
    lora_request=lora_request,
)
```

> * RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method
```
export VLLM_WORKER_MULTIPROC_METHOD=spawn

and wrap VLLM code with

if __name__ == "__main__":
```

> * custom model inference
```
model registration
operator implementation
```

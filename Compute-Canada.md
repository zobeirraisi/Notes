### Run an interactive job:
`salloc --account=def-jzelek --gres=gpu:1 --cpus-per-task=6 --mem=32000M --time=5:00`

### exmaple: 2 node, 8 GPUs per node (16GPUs)
`python -m torch.distributed.launch \
    --nproc_per_node=8 \
    --nnodes=2 \
    --node_rank=0 \
    --master_addr="10.198.189.10" \
    --master_port=22222 \
    mnmc_ddp_launch.py`

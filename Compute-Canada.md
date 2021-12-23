### Run an interactive job:
`salloc --account=def-jzelek --gres=gpu:1 --cpus-per-task=6 --mem=32000M --time=5:00`

### exmaple: 2 node, 4 GPUs per node (16GPUs)
`python -m torch.distributed.launch --nproc_per_node=4 --nnodes=2 --node_rank=0 --master_addr="10.198.189.10" --master_port=22222  mnmc_ddp_launch.py`

### ssh jupyter-lab
`echo -e '#!/bin/bash\nunset XDG_RUNTIME_DIR\njupyter-lab --ip $(hostname -f) --no-browser' > $VIRTUAL_ENV/bin/notebook.sh`

`chmod u+x $VIRTUAL_ENV/bin/notebook.sh`

`salloc --time=1:0:0 --ntasks=1 --cpus-per-task=6 --mem-per-cpu=16000M --gres=gpu:2 --account=def-jzelek srun $VIRTUAL_ENV/bin/notebook.sh`

`sshuttle --dns -Nr zobeir@beluga.computecanada.ca`


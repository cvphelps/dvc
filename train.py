import wandb
import random

wandb.init(project="dvc")
for step in range(10):
    wandb.log({"acc": random.random()})

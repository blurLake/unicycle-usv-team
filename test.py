import os
import gym
import unicycle_usv

from stable_baselines.common.env_checker import check_env, VecCheckNan
from stable_baselines.bench import Monitor

log_dir = "sac_logger/"
os.makedirs(log_dir, exist_ok=True)

env = gym.make('unicycle_usv:unicycle-v0')
env = Monitor(env, log_dir)

# It will check your custom environment and output additional warnings if needed
check_env(env)
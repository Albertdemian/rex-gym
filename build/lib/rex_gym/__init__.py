from rex_gym.agents import ppo, tools, scripts
from rex_gym.envs import gym, rex_gym_env
from rex_gym.model import motor, rex
from rex_gym.util import pybullet_data, bullet_client
from gym.envs.registration import register

register(
id='RexGym2-v0',
entry_point='rex_gym.envs.rex_gym_env:RexGymEnv',)
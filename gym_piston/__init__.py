import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id = 'Piston-v0',
    entry_point = 'gym_piston.envs:PistonEnv',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)
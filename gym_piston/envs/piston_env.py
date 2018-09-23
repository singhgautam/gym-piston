import os
import copy
import logging
import numpy as np
from gym import spaces
from gym.envs.mujoco import MujocoEnv

logger = logging.getLogger(__name__)

class PistonEnv(MujocoEnv):


    MODEL_FILE = "piston_arena.xml"
    FRAME_SKIP = 100

    def __init__(self):
        fullpath = os.path.join(os.path.dirname(__file__), "xmls", self.MODEL_FILE)
        super(PistonEnv, self).__init__(fullpath,
                                        self.FRAME_SKIP)
        self.action_space = spaces.MultiDiscrete([2]*9)

    def reset_model(self):
        pass

    def step(self, action):
        # push pistons
        observation = None
        for i in range(self.frame_skip):
            self.do_simulation(action * 10, 1)
            if observation is None:
                observation = copy.deepcopy(self.sim.data.sensordata)
            else:
                observation += copy.deepcopy(self.sim.data.sensordata)
        observation /= self.frame_skip

        # release pistons
        restoring_action = np.zeros(len(action))
        self.do_simulation(restoring_action, self.frame_skip)

        return observation, 0.0, False, {}


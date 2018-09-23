import gym
import time
from gym.envs.registration import register

register(
    id = 'Piston-v0',
    entry_point = 'gym_piston.envs:PistonEnv',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)


env = gym.make('Piston-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(200):
        env.render()
        action = env.action_space.sample()
        print('action',action)
        observation, reward, done, info = env.step(action)
        print('observation', observation)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
        time.sleep(0.03)
import gym
import time
import gym_piston


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
import gym
import tflearn as tf
import numpy as np

 env = gym.make('MountainCar-v0')

env = gym.make('mountaincar-v1')

for i_episode in range(10):
    observation = env.reset()
    for t in range(100):
        env.render()
        #print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Game " + str(i_episode) + " lasted " + str(t) + "steps")
            #print(env.observation_space.high)
            break
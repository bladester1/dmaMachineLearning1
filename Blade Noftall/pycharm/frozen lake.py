import gym

env = gym.make('FrozenLake-v0')

env.reset()
score = 0
print(env.observation_space)
print(env.action_space)

#obs, rew, done, info = env.step(env.action_space.sample())

def PlayGame():

for g in range(numSteps)
    env.reset()
    PlayGame()


    for i in range(numSteps):
        obs, rew, done, info = env.step(1)
        env.render()
        if done:
            score += rew
            break

for g in range(numGames)
    env.reset()
    PlayGame()

print(score)

numGames = 1000
numsteps = 10
env.reset()
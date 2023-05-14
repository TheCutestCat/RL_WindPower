from stable_baselines3 import dqn
from WindPowerSimulation.FlorisEnv import FlorisEnv

env = FlorisEnv()

obs = env.reset()
done = False
while not done:
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    # env.render()
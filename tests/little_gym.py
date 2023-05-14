import gym
from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.vec_env import VecFrameStack


# 创建一个单进程的VecEnv对象
env = make_vec_env('CartPole-v0', n_envs=1)

# 对状态进行预处理
env = VecFrameStack(env, n_stack=4) #对应的动态帧

# 定义DQN模型
model = DQN("MlpPolicy", env, verbose=1)

# 使用环境进行训练
model.learn(total_timesteps=10000)

# 对模型进行评估
mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10)

print(f"Mean reward:{mean_reward:.2f} +/- {std_reward:.2f}")

# 使用模型进行预测
obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, dones, info = env.step(action)
    # env.render()
    if dones:
        break

env.close()
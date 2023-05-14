from FlorisEnv import FlorisEnv
import gym
from gym import spaces
import numpy as np


class WindTurbineEnv(gym.Env):
    def __init__(self):
        # 风力发电机的yaw angle范围
        self.env = FlorisEnv()
        self.yaw_angle_range = np.array([-1,1],dtype=np.float32)

        # 风速范围
        self.wind_speed_range = np.array([0, 2],dtype=np.float32)

        # 状态空间
        self.observation_space = spaces.Box(
            low=np.array([self.yaw_angle_range[0]] * 6 + [self.wind_speed_range[0]] * 6),
            high=np.array([self.yaw_angle_range[1]] * 6 + [self.wind_speed_range[1]] * 6),
            dtype=np.float32)

        # 动作空间
        self.action_space = spaces.Box(low=self.yaw_angle_range[0],
                                       high=self.yaw_angle_range[1],
                                       shape=(6,),
                                       dtype=np.float32)

        # 奖励函数
        self.reward_range = (0, np.inf)

    def reset(self):
        # 返回初始状态，所有发电机yaw angle随机分布
        return np.zeros((12,),dtype=np.float32)

    def step(self, action):
        difference, turbine_powers = self.env.RUN(angle=action)
        reward = difference
        done = False
        turbine_powers = np.array(turbine_powers).reshape(-1)/1000
        action_m = np.array(action).reshape(-1)
        turbine_powers, action_m = turbine_powers.tolist(),action_m.tolist()
        obs = np.array(action_m + turbine_powers).astype(np.float32)

        return obs, reward, done, {}

if __name__ == "__main__":
    from stable_baselines3.common.env_checker import check_env
    # 如果你安装了pytorch，则使用上面的，如果你安装了tensorflow，则使用from stable_baselines.common.env_checker import check_env
    env = WindTurbineEnv()
    check_env(env)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 19:07:44 2021

@author: johnviljoen
"""

from env_mk2 import F16

from parameters import initial_state_vector_ft_rad as x0
from parameters import simulation_parameters as paras_sim
from parameters import model_predictive_control_parameters as paras_mpc

import gym

from stable_baselines3 import A2C
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.policies import ActorCriticPolicy

from scipy.signal import cont2discrete

import numpy as np


from stable_baselines3.common.env_checker import check_env

from sys import exit

f16 = F16(x0, x0[12:16], paras_sim)
# u_opt = f16.calc_MPC_action_mk2(10,10,10,paras_mpc)
A,B,C,D = f16.linearise(f16.x_na, f16.u, calc_xdot=f16.calc_xdot_na, get_obs=f16.get_obs_na)
res = f16.calc_MPC_action(0, 0, 0, 0, paras_mpc)

# f16.sim(f16.x0)

# check_env(f16, warn=True)

# A_c, B_c, C_c, D_c = f16.linearise(f16.x, f16.u)
# A_d, B_d, C_d, D_d = cont2discrete((A_c, B_c, C_c, D_c), f16.dt)[0:4]

# K = np.zeros((4,18))

# K[0,12] = 1
# K[1,13] = 20.2
# K[2,14] = 20.2
# K[3,15] = 20.2

# R = 0.01



exit()


env = DummyVecEnv([lambda: F16(x0, x0[12:16], paras_sim)])

model = A2C('MlpPolicy', env, verbose=1)

# model.learn(total_timesteps=100)
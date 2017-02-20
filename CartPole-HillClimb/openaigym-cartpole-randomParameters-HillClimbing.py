
# coding: utf-8

# In[31]:

import gym
import numpy as np
env = gym.make('CartPole-v0')
env.reset()


# In[38]:

def getNextAction(parameters,observation):
    parameters = np.random.rand(4);
    action = 0 if np.matmul(parameters,observation) < 0 else 1;
    return action;


def testRun(env,parameters):
    currentBest = 0;
    action = 0;
    for _ in range(200):
        observation, reward, done, info = env.step(action);
        action = getNextAction(parameters,observation);       
        #env.render()       
        if done:
            env.reset();
            return currentBest;
        else:
            currentBest+=1;

noise = 0.1
parameters = np.random.rand(4) * 2 - 1;
for step in range(10000):
    parameters = parameters + (np.random.rand(4) * 2 - 1) * noise;
    curReward = testRun(env,parameters)
    if curReward > 150:
        print (step);
        print(parameters)
        break;





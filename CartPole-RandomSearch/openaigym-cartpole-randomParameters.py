
# coding: utf-8

# In[2]:

import gym
import numpy as np
env = gym.make('CartPole-v0')
env.reset()


# In[3]:

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
        env.render()       
        if done:
            env.reset();
            return currentBest
        else:
            currentBest+=1;


for _ in range(10000):
    parameters = np.random.rand(4);
    curReward = testRun(env,parameters)
    if curReward > 100:
        print(parameters)
        break;


# In[11]:




# In[ ]:




# In[ ]:




#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import choice

import numpy as np
import scipy as sp


# In[2]:


np.set_printoptions(formatter={'float_kind': lambda x: "{0:0.4f}".format(x)})


# ### 소재 수 = n
# ### 소재별 (노출 + 클릭 O, 노출 + 클릭 X, 베타 분포 샘플링 점수) = history
# ### history 행: 소재, history 열: [노출 수, 클릭 수, 선택된 x값]

# In[3]:


class Bandit:
    def __init__(self, n: int):
        self.history = np.zeros((n, 3), dtype=np.float32)
        
    def update(self, i: int, impression_count: int, click_count: int):
        self.history[i][0] += impression_count
        self.history[i][1] += click_count
        
    def select(self):
        for el in range(self.history.shape[0]):
            self.history[el][2] = np.random.beta(self.history[el][1] + 1, self.history[el][0] - self.history[el][1] + 1)

        return np.argmax(self.history, axis=0)[2]


# In[4]:


# i번째 소재가 노출되어 클릭될 확률 = prob[i]
prob = [0.03, 0.01, 0.02]


# In[5]:


def update():
    idx = bandit.select()
    result = np.random.choice([0,1], p=[prob[idx], 1 - prob[idx]])

    bandit.update(idx, 1, 1 if result == 0 else 0)


# In[16]:


bandit = Bandit(n=len(prob))

for el in range(1000):
    update()

# 전체 히스토리
print(bandit.history)

# 선택된 광고 소재
print(bandit.select())



# coding: utf-8

# In[1]:


import multiprocessing as mp
import random
import string


# In[5]:


output = mp.Queue()


# In[14]:


def rand_string(length, output):
    rand_str = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(length))
    output.put(rand_str)


# In[15]:


processes = [mp.Process(target=rand_string, args=(5, output))
             for x in range(4)]


# In[16]:


for p in processes:
    p.start()
for p in processes:
    p.join()


# In[17]:


results = [output.get() for p in processes]


# In[18]:


print(results)


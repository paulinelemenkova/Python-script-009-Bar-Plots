#!/usr/bin/env python
# coding: utf-8

# In[61]:


import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd
import os
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
sb.set_style("whitegrid")

fig = plt.figure()
st = fig.suptitle('Bar plots for the Mariana Trench geology: \nSediment thickness (left) and distance from igneous volcanic areas (right)', 
             fontsize=10)
ax1 = fig.add_subplot(1, 2, 1)
sb.catplot(x="profile", y="sedim_thick", data=df, kind="bar", palette='tab20b', ax=ax1)

ax2 = fig.add_subplot(1, 2, 2)
sb.catplot(x="profile", y="igneous_volc", data=df, kind="bar", palette='tab20c', ax=ax2)

plt.show()


# In[ ]:





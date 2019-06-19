#!/usr/bin/env python
# coding: utf-8
import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb

os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
sb.set_style("whitegrid")
sb.set_context('paper')

# define variables and plotting
fig = plt.figure(figsize=(10.0, 6.0), dpi=300)
fig.suptitle("Bar plots for the Mariana Trench geology: \nSediment thickness (left) and distance from igneous volcanic areas (right)",
             fontsize=10)
# subplot 1
ax1 = fig.add_subplot(1, 2, 1)
sb.catplot(x="profile", y="sedim_thick", data=df,
           kind="bar", palette='tab20b', ax=ax1
           )
# subplot 2
ax2 = fig.add_subplot(1, 2, 2)
sb.catplot(x="profile", y="igneous_volc", data=df,
           kind="bar", palette='tab20c', ax=ax2
           )

# printing and saving a file
plt.tight_layout()
plt.savefig('plot_Barplot.png', dpi=300)
plt.show()

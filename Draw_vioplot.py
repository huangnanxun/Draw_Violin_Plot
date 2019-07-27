#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
get_ipython().run_line_magic('matplotlib', 'inline')

sns.set_style("whitegrid")
sns.set_context("paper")
temp_data = pd.read_csv("E://code/Temperature_boxplot.csv")
print(temp_data.head())

tmp_value_list = [23,21,20,17,7,4]
y_len = [""] * 30
y_len[23] = 'NZ'
y_len[21] = 'NY'
y_len[20] = 'UK'
y_len[17] = 'CA'
y_len[7] = 'SCN'
y_len[4] = 'HK'
my_pal = {"NZ":"lime","NY":"cyan","UK":"cornflowerblue","CA":"yellow","SCN":"lightpink","HK":"fuchsia","":"white"} 
#my_pal = ["white"] * 60
#my_pal[46] = 'fluorescent green'
#my_pal[42] = 'bright cyan'
#my_pal[40] = 'periwinkle'
#my_pal[35] = 'bright yellow'
#my_pal[14] = 'soft pink'
#my_pal[9] = 'candy pink'
plt.subplots(figsize=(7, 6))
sns.set_style('white')
lime_patch = mpatches.Patch(color='lime', label='New Zealand')
cyan_patch = mpatches.Patch(color='cyan', label='New York')
cornflowerblue_patch = mpatches.Patch(color='cornflowerblue', label='United Kingdom')
yellow_patch = mpatches.Patch(color='yellow', label='California')
lightpink_patch = mpatches.Patch(color='lightpink', label='South China')
fuchsia_patch = mpatches.Patch(color='fuchsia', label='HongKong')
plt.plot([5.95,24.25],[24.2,5.10],linestyle = "--",color='black')
viop = sns.violinplot(x="temp", y="country", data=temp_data,
            linewidth = 1,   # 线宽
            width = 1.5,     # 箱之间的间隔比例
            palette = my_pal,#palette = 'hls', # 设置调色板
            order = y_len, #["HK","SCN","CA","UK","NY","NZ"],  # 筛选类别
            scale = 'count',  # 测度小提琴图的宽度：area-面积相同，count-按照样本数量决定宽度，width-宽度一样
            gridsize = 50,   # 设置小提琴图边线的平滑度，越高越平滑
            inner = 'box',   # 设置内部显示类型 → “box”, “quartile”, “point”, “stick”, None
            #bw = 0.8        # 控制拟合程度，一般可以不设置
            orient = 'h'
           )

#plt.legend([p1,p2],["New Zealand","New York","United Kingdom","California","South China","HongKong"],ncol=2,loc='upper left')
plt.legend(handles=[lime_patch,cyan_patch,cornflowerblue_patch,yellow_patch,lightpink_patch,fuchsia_patch],ncol=2,loc='upper left',handlelength=1.2,handleheight=1.2,frameon=False)
viop.set_yticks([25,22.5,20,17.5,15,12.5,10,7.5,5,2.5])#5.10,4.59,2.55,2.04,1.83,1.38
viop.set_yticklabels(["1.0","1.5","2.0","2.5","3.0","3.5","4.0","4.5","5.0","5.5"])
plt.xlabel('Temperature(°C)')
plt.ylabel('Effective Mutation Period(EMP)')
plt.text(6, 12, 'EMP ~ 0.21005 * Temperature - 0.09807', fontsize=10)
plt.text(6, 13, 'Adjusted R-squared:  0.727', fontsize=10)
viop.set(ylim=(25, 2.2))
plt.savefig("E://code/Temperature_boxplot_output.png",dpi=600)
plt.show()

# In[ ]:





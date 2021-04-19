import numpy as np
import seaborn as sns

def sns_his(obs,data_property):
    
    fig, axes = plt.subplots(1, 1, figsize=(8, 5), sharey=True)

    hist_kws = {'range':(0.3,1)} # depends on the scale of input data

    obs_visual = sns.distplot(obs,bins=20,kde=False,color='lime',hist_kws=hist_kws) # no. of bins depends on the input data

    obs_visual.set_xlabel("data_property,",fontsize=15)

    obs_visual.set_facecolor("floralwhite")
    obs_visual.set_alpha(0.2)

    axes.xaxis.set_tick_params(labelsize=15)
    axes.yaxis.set_tick_params(labelsize=15)
    
    return obs_visual

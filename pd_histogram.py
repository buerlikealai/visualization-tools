import numpy as np
import pandas as pd

def pd_his(a,b):
    """ this function is used to plot two arrays with different length"""

    # create the dataframe; enumerate is used to make column names
    df = pd.concat(
                   [pd.DataFrame(a, columns=[f'tree:probability{i}']) 
                   for i, a in enumerate([a, b], 1)],
                   axis=1
                   )

    # plot the data
    ax = df.plot.hist(stacked=True,bins=20, density=True, figsize=(6, 4), range=(0.35,1), fontsize=15, legend=True)
    ax.set_xlabel("predicted probability of pixel",fontsize=15)
    
    return ax
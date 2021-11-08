# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 18:04:53 2021

@author: pc
"""

#Import matplotlib for plotting
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

#Line Plot

#Random Data
x=np.linspace(0,10,1000)
#Plot
plt.plot(x,np.cos(x), label='cosine')
plt.plot(x,np.sin(x), label='sine')
plt.plot(x,np.tan(x), label='tan')


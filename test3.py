# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 13:58:14 2017

@author: bianl
"""

import numpy as np
from scipy import stats 

x=np.random.binomial(1000,0.5,200)
density=stats.kde.gaussian_kde(x)

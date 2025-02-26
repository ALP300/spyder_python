# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 20:21:46 2025

@author: aitor
"""

import pandas as pd
import numpy as np
datos = pd.read_csv("ATP.csv", encoding="latin1") 
print(datos.info())
print(datos.head())
nuevo= pd.DataFrame(datos)
print(nuevo)

nuevo2= nuevo.replace(np.nan, "0")
print(nuevo2.info())

print(nuevo2.describe())
print(nuevo.describe(include=[np.number]))

nuevo2= nuevo2.replace("N/A", "0")
nuevo2= nuevo2.replace("NR", "0")
print(nuevo.describe())
nuevo2['Wsets']= nuevo2.Wsets.astype(int)
nuevo2['WRank']= nuevo2.WRank.astype(int)
print(nuevo2.describe())
print(datos.head())

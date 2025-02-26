# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 21:38:39 2025

@author: aitor
"""
import pandas as pd
import numpy as np

datos= {'Nombres':['Leonardo','Yerson','Briyit','Marián'], 'Calificaciones':['20','15','19','13'],
        'Deportes':['running','fútbol','natación', 'basquet'], 'Materias':['Fabdig','física','química', 'biología']}

df= pd.DataFrame(datos)
print(df)
print('\n'*3)

datos2= {'Nombres':['Briyit','Yerson','N/A','Marián'], 'Calificaciones':['12','15','19','13'],
        'Deportes':['N/A','fútbol','natación', 'basquet'], 'Materias':['N/A','física','química', 'biología']}

df2= pd.DataFrame(datos2)
print(df2)
print('\n'*3)
print(df2.info())
print('\n'*4)
#ESTADÍSTICAS BÁSICAS
print(df2.describe())
print('\n'*4)
nuevo= pd.DataFrame(df2)
nuevo= nuevo.replace(np.nan, "0")
print(nuevo)
print('\n'*4)

nuevo['Calificaciones']= nuevo.Calificaciones.astype(int)
print(nuevo)
print(nuevo.describe())













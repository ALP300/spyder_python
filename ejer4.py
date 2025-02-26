# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:15:53 2025

@author: aitor
"""
import pandas as pd
datos = pd.read_csv("ATP.csv", encoding="latin1") 

print(datos.head())
datos.set_index("Location", inplace=True)
print("-------------------Melbourne------------------")
print(datos.loc['Melbourne'])
print("------------------Valencia y Houston---------------")
print(datos.loc[['Houston','Melbourne']])
print('\n')
print(datos.loc[['Houston','Melbourne'],['Series','Court']])
print("------SELECCIÓN CON RANGO-----------")
print(datos.loc[['Houston','Melbourne'], 'Series':'Round'])
print("--- SELECCIÓN SOLAMENTE GRAND SLAM ------")
print(datos.loc[datos['Series'].str.endswith("Slam")])
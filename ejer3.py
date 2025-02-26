import pandas as pd

datos = pd.read_csv("ATP.csv", encoding="latin1") 
print(datos.info())
print(datos.iloc[0:20])
print(datos.head())
print(datos.iloc[[0,3,4,5,12],])
print(datos.iloc[[0,3,5,25],[0,5,6]])
print(datos.iloc[:, 0:2])
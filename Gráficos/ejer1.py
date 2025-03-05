'''

 Por ejemplo, cómo han cambiado los 
 ingresos de las películas con el tiempo.
 
'''
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('MoviesDataset.csv')
print(df.head())
print(df.columns)

if 'release_date' in df.columns and 'revenue' in df.columns:
    df['release_date']= pd.to_datetime(df['release_date'], errors='coerce')
    df['year']= df['release_date'].dt.year
    print(df['year'])
    plt.figure(figsize=(10, 6))
    df.groupby('year')["revenue"].sum().plot(kind='line', marker= 'o', color='red')
    plt.title('Ingresos por Año')
    plt.xlabel('Año')
    plt.ylabel('Ingresos (en millones)')
    plt.grid(True)
    plt.show()
    
else:
    print("Las columnas no existen")
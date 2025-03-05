import pandas as pd
datos = pd.read_csv("ATP.csv", encoding="latin1") 
d= datos.head()
datos.set_index("Location", inplace=True)
print(datos.loc[datos['Court']=='Outdoor',['Surface']])
print(datos.loc[datos['Court']=='Outdoor',['Surface','Winner']])
print("*------------------MÁS DE UNA CONDICIÓN ---------------------------*")
print(datos.loc[datos['Series'].str.endswith("Slam")&(datos['Surface']=="Clay")
                &(datos['Winner']=="Federer R.") &(datos['Round']=='The Final ')])
# COLUMNA IMC
atletas['IMC'] = atletas['Weight'] / (atletas['Height']/100)**2
display(atletas.tail())
## ¿Que opina de esta nueva variable? ¿Tiene el mismo sentido en todos los deportes?
### No, puesto que el rendimiento de los distintos deportes se ve afectado por las características físicas de los atletas. 
### Además, hay valores ideales 'IMC' para obtener el mejor desempeño en distintos deportes. Por ejemplo, una persona delgada no va a desempeñarse igual haciendo atletismo que levantando pesas.

# Fusión de ambos archivos con NOC
## Utilizando .merge(), se han fusionado ambos data frames tomando como referencia la variable 'NOC', que se encuentra en ambos data frames. 
df_fusion.sort_values(by= 'ID' , ascending= True)

# FILAS CON NaN en NOC
display(df_fusion[df_fusion['region'].isna()])
## ¿Cuántas filas quedan sin region? ¿Por qué cree que ocurre esto?
### Por que en el dataframe de regiones, los valores 'TUV', 'ROT' y 'UNK' no tienen un valor en la columna 'NOC' por lo que llenan con NaN .

### ¿Qué tipo de fusión 'how' se usamos? ¿Porque?
###Usamos how='left'. Este tipo de fusión garantiza que el df de la izquierda(atletas) mantenga intactas todas sus filas incluso si algún atleta tiene un codigo NOC que no aparece en regiones.
###Además, se descartan aquellos valores que se encuentren en el data frame 'regiones' que no tengan coincidencia con ninguna fila del data frame 'atletas'.

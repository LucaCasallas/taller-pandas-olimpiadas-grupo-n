## Encontrar la proporcion de datos nulos.
## Obseervar si campia la proporcion de datos faltantes con respecto a la epoca.

df_nulls = df_fusion.drop('notes', axis=1) # Elimina columna que en su mayoria los datos son nulos
display(df_nulls.isnull().sum()) # Nulos totales por variable
df_antes = df_nulls[df_nulls['Year'] < 1960] # Dataset con datos antes de 1960
#display(df_antes[df_antes['Year'] >= 1960]) ~~~ Verificar que no hay ningun dato despues de 1960
df_despues = df_nulls[df_nulls['Year'] >= 1960] # Dataset con datos despues de 1960
#display(df_antes.isnull().sum())
#display(df_despues.isnull().sum())  ## Verificar datos nulos totales
####
display(df_antes[['Age','Height','Weight','IMC']].isnull().mean()*100) # Proporcion de datos nulos por etapa
display(df_despues[['Age','Height','Weight','IMC']].isnull().mean()*100) # ##

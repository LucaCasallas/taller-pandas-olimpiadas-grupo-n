# Nueva columna: Medalla
###Haciendo uso de .apply(), creamos la columna 'Medalla', que indica si un atleta ganó alguna medalla (ya sea de oro, plata o bronce).
###Esto lo hicimos limpiando los valores nulos de la columna 'Medal' y creando la función 'validarMedalla'.

# LIMPIEZA DE LA COLUMNA "MEDAL"
df_fusion['Medal'] = df_fusion['Medal'].fillna('Ninguna')
df_fusion

# CREACIÓN COLUMNA "MEDALLA"
def validarMedalla(x):
  if x == 'Ninguna':
    return 0
  return 1

df_fusion['Medalla'] = df_fusion['Medal'].apply(validarMedalla)
df_fusion

# MEDALLAS POR JUGADOR
display(df_fusion.groupby(['ID','Name'])['Medalla'].sum().sort_values(ascending=False))

# ATLETA CON MAS MEDALLAS
df_fusion[df_fusion['Name'] == 'Michael Fred Phelps, II']

## Comparación de la participación de los atletas

### PARTICIPACIÓN ANUAL (JUGADORES INDIVIDUALES)
df_base = df_fusion.groupby(['Year', 'Name'])['ID'].count()
df_base

### PARTICIPACIÓN ANUAL TOTAL
df_fusion.groupby('Year')['Name'].nunique()

### PARTICIPACIÓN FILTRADA POR AÑO, TEMPORADA Y SEXO
df_base = df_fusion.groupby(['Year', 'Season', 'Sex'])['Name'].nunique()
display(df_base[0:20])
#display(df_base[40:60])
df_base.xs((1924,'Winter','F'), level=['Year','Season','Sex'])

#df_base['Total'] = df_base.xs(1948, level='Year')

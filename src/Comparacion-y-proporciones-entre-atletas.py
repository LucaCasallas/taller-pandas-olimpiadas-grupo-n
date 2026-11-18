#A
genero = df_fusion.groupby('Sex').agg(
    atletas=('ID', 'nunique'),
    medallas=('Medalla', 'sum')
)
genero['proporcion'] = genero['medallas'] / genero['atletas']
print(genero)

#B
df_fusion['Menor_18'] = df_fusion['Age'] < 18
resumen_edad = df_fusion.groupby('Menor_18').agg(
    Atletas=('ID', 'nunique'),
    Medallas=('Medalla', 'sum')
)

resumen_edad['Proporcion'] = (resumen_edad['Medallas'] / resumen_edad['Atletas'])
resumen_edad['Porcentaje'] = (resumen_edad['Proporcion'] * 100).round(2)

display(resumen_edad)

#C
df_fusion['Edad'] = '18 a 34'
df_fusion.loc[df_fusion['Age'] < 18, 'Edad'] = 'Menor de 18'
df_fusion.loc[df_fusion['Age'] >= 35, 'Edad'] = '35 o mas'
tabla = df_fusion.groupby('Edad')['Medalla'].agg(
    participaciones='count',
    medallas='sum',
    proporcion='mean'
)

tabla['porcentaje'] = tabla['proporcion'] * 100
print(tabla)

#D
df_fusion['Pais'] = 'Otros'
df_fusion.loc[df_fusion['Team'] == 'United States', 'Pais'] = 'USA'
medallas = df_fusion.groupby('Pais')['Medalla'].sum()
proporcion = df_fusion.groupby('Pais')['Medalla'].mean()
porcentaje = proporcion * 100

print("Medallas:\n", medallas)
print("\nPorcentaje:\n", porcentaje)

#E
medallas = df_fusion.groupby('Season')['Medalla'].sum()
proporcion = df_fusion.groupby('Season')['Medalla'].mean()
porcentaje = proporcion * 100
print("Medallas:\n", medallas)
print("\nPorcentaje:\n", porcentaje)

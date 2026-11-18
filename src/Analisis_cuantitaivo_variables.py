# Edad promedio de los atletas.
print(f'A)\n-- La edad promedio es: {df_fusion['Age'].mean()}.')
# Cantidad de registros con medalla y sin medalla.
print(f'B)\n-- {df_fusion[df_fusion['Medalla'] == 0]['Medalla'].count()} registros terminaron con medalla.')
print(f'-- {df_fusion[df_fusion['Medalla'] != 0]['Medalla'].count()} registros terminaron sin medalla.')
# Estatura promedio de los atletas que ganaron medalla de oro.
print(f'C)\n-- La estatura promedio de los atletas que ganaron una medalla de oro es: {df_fusion[df_fusion['Medal'] == 'Gold']['Height'].mean()}.')
# Cantidad de ediciones y paises distintos en el dataset.
print(f'D)\n-- La cantidad de ediciones distintas en los juegos ha sido: {df_fusion['Games'].nunique()}.')
print(f'D)\n-- La cantidad de países distintos que han participado en los juegos ha son: {df_fusion['NOC'].nunique()}.')
# Edad mas joven, y mas vieja de los atletas.
print(f'E)\n-- La persona mas joven en participar en una edición de los juegos olimpicos es: {df_fusion['Age'].min()}.')
display(df_fusion[df_fusion['Age'] == 10])
print(f'E)\n-- La persona mas vieja en participar en una edición de los juegos olimpicos es: {df_fusion['Age'].max()}.')
display(df_fusion[df_fusion['Age'] == 97])
# Cantidad de registros por temporada ( Verano , Invierno ).
print(f'F)\n-- Registros que hay en summer y winter')
print(df_fusion["Season"].value_counts())   ## .values_counts() es para contar cada valor unico y los ordena de de mayor a menor
# Cantidad de atletas unicos que participaron en una, y mas de una edicion.
ediciones_por_atleta = df_fusion.groupby('ID')['Games'].nunique()
una = (ediciones_por_atleta == 1).sum()
mas= (ediciones_por_atleta > 1).sum()
print(f"G)\n --Atletas en una sola edición: {una}.")
print(f"G)\n--Atletas en más de una edición: {mas}.")

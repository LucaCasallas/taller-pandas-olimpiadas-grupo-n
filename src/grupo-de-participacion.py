## Distribución de participación de los atletas
atletas_edicion = df_fusion.groupby(['ID', 'Games']).agg(
    n_pruebas=('Event', 'count'),
    Sport=('Sport', 'first')
)
atletas_edicion['Grupo'] = 'Grupo 2: Moderada (2-3)'
atletas_edicion.loc[atletas_edicion['n_pruebas'] == 1, 'Grupo'] = 'Grupo 1: Una'
atletas_edicion.loc[atletas_edicion['n_pruebas'] >= 4, 'Grupo'] = 'Grupo 3: Alta (4 o ms)'
print("Total por grupo:")
print(atletas_edicion['Grupo'].value_counts())
print("\nTop deportes en Grupo 1:")
print(atletas_edicion[atletas_edicion['Grupo'] == 'Grupo 1: Una']['Sport'].value_counts().head()) ## .values_counts() es para contar cada valor unico y los ordena de de mayor a menor
print("\nTop deportes en Grupo 2:")
print(atletas_edicion[atletas_edicion['Grupo'] == 'Grupo 2: Moderada (2-3)']['Sport'].value_counts().head())
print("\nTop deportes en Grupo 3:")
print(atletas_edicion[atletas_edicion['Grupo'] == 'Grupo 3: Alta (4 o ms)']['Sport'].value_counts().head())

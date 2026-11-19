import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# --- GRAFICA #1 ---

# 1. Filtrar valores de IMC plausibles
df_IMC = df_fusion[df_fusion["IMC"].between(12, 50)]

# 2. Crear la gráfica
plt.figure(figsize=(8, 4.5))
sns.histplot(data=df_IMC, x="IMC", hue="Sex", bins=60,
             stat="density", common_norm=False, element="step")

# 3. Títulos y ejes
plt.title("Distribución del IMC por sexo")
plt.xlabel("IMC (kg/m²)")

# 4. Guardar y mostrar
plt.savefig("g01_imc_sexo.png", dpi=150, bbox_inches="tight")
plt.show()

# --- GRAFICA #2 --- 

# Requiere haber corrido antes el gráfico 1 (ahí se crea d, con IMC entre 12 y 50)

# 1. Elegir los deportes a comparar (10 con cuerpos muy distintos)
deportes = ["Gymnastics", "Athletics", "Swimming", "Football", "Basketball",
            "Rowing", "Judo", "Boxing", "Wrestling", "Weightlifting"]

# 2. Quedarnos solo con las filas de esos deportes
df_IMC_deportes = df_IMC[df_IMC["Sport"].isin(deportes)]

# 3. Calcular el orden: deportes de menor a mayor mediana de IMC
orden = df_IMC_deportes.groupby("Sport")["IMC"].median().sort_values().index

# 4. Crear el lienzo
plt.figure(figsize=(9, 5))

# 5. Dibujar un boxplot horizontal por deporte, en el orden calculado
sns.boxplot(data=df_IMC_deportes, x="IMC", y="Sport", order=orden)

# 6. Títulos y ejes
plt.title("IMC por deporte")
plt.xlabel("IMC (kg/m²)")
plt.ylabel("")  # los nombres de los deportes ya se explican solos

# 7. Guardar (antes de mostrar) y mostrar
plt.savefig("g02_imc_deporte.png", dpi=150, bbox_inches="tight")
plt.show()

# --- GRAFICA #3 ---

# 1. Contar registros con medalla por región y quedarnos con las 10 primeras
top = (df_fusion.groupby("region")["Medalla"]   # agrupar por región, tomar la columna Medalla
       .sum()                                    # sumar los 1 = registros con medalla
       .sort_values(ascending=False)             # de mayor a menor
       .head(10))                                # solo las 10 primeras

# 2. Crear el lienzo
plt.figure(figsize=(8, 4.5))

# 3. Barras horizontales: valores en x, nombres de región en y
sns.barplot(x=top.values, y=top.index, color="#4c72b0")

# 4. Títulos y ejes
plt.title("10 regiones con más registros con medalla")
plt.xlabel("Registros con medalla")
plt.ylabel("")

# 5. Guardar (antes de mostrar) y mostrar
plt.savefig("g03_top_regiones.png", dpi=150, bbox_inches="tight")
plt.show()

# --- GRAFICA #4 ---

# 1. Tasa de medalla por sexo
#    mean() sobre una variable 0/1 = proporción de registros con medalla
t = df_fusion.groupby("Sex")["Medalla"].mean().reset_index()

# 2. Crear el lienzo (pequeño: solo hay 2 barras)
plt.figure(figsize=(5, 4))

# 3. Barras: una por sexo
ax = sns.barplot(data=t, x="Sex", y="Medalla")

# 4. Escribir el porcentaje encima de cada barra
etiquetas = [f"{v*100:.1f}%" for v in t["Medalla"]]
ax.bar_label(ax.containers[0], labels=etiquetas)

# 5. Títulos y ejes
plt.title("Tasa de medalla por sexo")
plt.ylabel("Medallas / participaciones")

# 6. Guardar (antes de mostrar) y mostrar
plt.savefig("g04_tasa_sexo.png", dpi=150, bbox_inches="tight")
plt.show()

# --- GRAFICA #5 ---

# 1. Tasa de medalla por temporada (Summer / Winter)
#    mean() sobre una variable 0/1 = proporción de registros con medalla
tasa_temporada = df_fusion.groupby("Season")["Medalla"].mean().reset_index()

# 2. Lienzo pequeño (solo 2 barras)
plt.figure(figsize=(5, 4))

# 3. Una barra por temporada
ax = sns.barplot(data=tasa_temporada, x="Season", y="Medalla")

# 4. Porcentaje encima de cada barra
etiquetas = [f"{v*100:.1f}%" for v in tasa_temporada["Medalla"]]
ax.bar_label(ax.containers[0], labels=etiquetas)

# 5. Títulos y ejes
plt.title("Tasa de medalla por temporada")
plt.ylabel("Medallas / participaciones")

# 6. Guardar (antes de mostrar) y mostrar
plt.savefig("g05_tasa_temporada.png", dpi=150, bbox_inches="tight")
plt.show()


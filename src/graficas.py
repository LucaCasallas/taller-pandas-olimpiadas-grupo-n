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

### --- GRAFICA #3 ---

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
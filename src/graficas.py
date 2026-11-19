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
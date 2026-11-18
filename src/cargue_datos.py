# cargue_datos.py
# Este script carga el dataset de atletas olímpicos (athlete_events.csv)
# en un DataFrame de pandas y muestra las últimas filas.

import pandas as pd

atletas = pd.read_csv('data/athlete_events.csv')
print(atletas.tail())

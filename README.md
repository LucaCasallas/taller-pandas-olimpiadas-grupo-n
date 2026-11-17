# Proyecto_Programacion_2026-2-
Universidad Externado de Colombia
En este proyecto, se analizan los datos históricos de los Juegos Olímpicos.
Integrantes: Jerónimo Casallas, Ian García, Sebastián Martinez
Roles :
  Lıder de Repositorio: Jerónimo Casallas
  Lıder de Datos: Ian García
  Lıder de Reporte: Sebastián Martinez 
  
1) Objetivo general:
   Analizar con Pandas el conjuntos de datos de los Juegos Olimpicos de 1896 a 2016 (271,116 registros, cada fila es un atleta en una prueba, no atleta unico) para describir la participacion, medir cuantas meddallas ganaron    entre distintos grupos, en conteo y proporcion. Identificacion de datos faltantes y porque y discutir que caracteristicas se asocian con una mayor probabilidad de ganar una medalla.

1.2) Metodologia:
   1) Se cargaron los archivos athlete events.csv y noc regions.csv en dataframes separados y se unieron por NOC con una union left(sin cambiar el numero de filas)
   2) Se crearon las variables IMC, madalla(1 si Medal tiene valor), grupo etario, n_prueba y grupo de participacion.
   3) Las comparaciones entre grupos se hacen conteos y con tasas

  

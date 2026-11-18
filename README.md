# Proyecto_Programacion_2026-2-
## Universidad Externado de Colombia
En este proyecto, se analizan los datos históricos de los Juegos Olímpicos.
###  Integrantes: Jerónimo Casallas, Ian García, Sebastián Martinez
### Roles :
  * Líder de Repositorio: Jerónimo Casallas
  * Lıder de Datos: Ian García
  * Lıder de Reporte: Sebastián Martinez 
  
## 1. Objetivo general:
   Analizar con Pandas el conjuntos de datos de los Juegos Olimpicos de 1896 a 2016 (271,116 registros, cada fila es un atleta en una prueba, no atleta unico) para describir la participacion, medir cuantas meddallas ganaron    entre distintos grupos, en conteo y proporcion. Identificacion de datos faltantes y porque y discutir que caracteristicas se asocian con una mayor probabilidad de ganar una medalla.

## 1.2. Metodologia:
   1) Se cargaron los archivos athlete events.csv y noc regions.csv en dataframes separados y se unieron por NOC con una union left(sin cambiar el numero de filas)
   2) Se crearon las variables IMC, madalla(1 si Medal tiene valor), grupo etario, n_prueba y grupo de participacion.
   3) Las comparaciones entre grupos se hacen conteos y con tasas

  2) Descripción de variables de la base de datos
## 2. Descripción de las variables

**`athlete_events.csv`** (una fila = un atleta en una prueba de una edición)

| Variable | Tipo | Descripción |
|---|---|---|
| `ID` | entero | Identificador único del atleta |
| `Name` | texto | Nombre del atleta |
| `Sex` | categórica | `M` / `F` |
| `Age` | numérica | Edad en años (al momento de los Juegos) |
| `Height` | numérica | Estatura en cm |
| `Weight` | numérica | Peso en kg |
| `Team` | texto | Equipo / país por el que compitió |
| `NOC` | categórica | Código de 3 letras del Comité Olímpico Nacional |
| `Games` | texto | Edición (`Year` + `Season`) |
| `Year` | entero | Año de la edición |
| `Season` | categórica | `Summer` / `Winter` |
| `City` | texto | Ciudad sede |
| `Sport` | categórica | Deporte |
| `Event` | texto | Prueba específica dentro del deporte |
| `Medal` | categórica | `Gold`, `Silver`, `Bronze` o vacío (sin medalla) |

**`noc_regions.csv`** (una fila = un NOC)

| Variable | Tipo | Descripción |
|---|---|---|
| `NOC` | texto | Código del Comité Olímpico Nacional (llave de unión) |
| `region` | texto | País / región a la que corresponde el NOC |
| `notes` | texto | Notas (nombres históricos, territorios, etc.) |

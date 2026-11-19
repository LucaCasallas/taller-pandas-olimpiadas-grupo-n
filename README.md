# Proyecto_Programacion_2026-2-
## Universidad Externado de Colombia
En este proyecto, se analizan los datos históricos de los Juegos Olímpicos.
###  Integrantes: Jerónimo Casallas, Ian García, Sebastián Martinez
### Roles :
  * Líder de Repositorio: Jerónimo Casallas 
  * Líder de Datos: Ian García
  * Líder de Reporte: Sebastián Martinez
  
## 1.1. Objetivo general:
   Analizar con Pandas el conjunto de datos de los Juegos Olímpicos de 1896 a 2016 para describir la participación, medir cuantas medallas ganaron entre distintos grupos en cuanto a cantidad y proporción, y discutir que características se asocian con una mayor probabilidad de ganar una medalla.

## 1.2. Metodologia:
   1) Se cargaron los archivos athlete_events.csv y noc_regions.csv en dataframes separados y se unieron por NOC con una unión left (sin cambiar el número de filas).
   2) Se crearon las variables IMC, medalla, grupo etario, n_prueba y grupo de participación.
   3) Las comparaciones entre grupos se hacen conteos y proporciones.

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

3. * Más sobre el proyecto lo puedes encontrar en la carpeta /docs/informe-final

https://www.linkedin.com/in/daniel-vielma-10bb42269/
<h1 align='center'>
  PROYECTO INDIVIDUAL Nº2 

 <b> Data Analytics: Criptocurrencies</b>   
 Daniel Viema DTPT02
</h1>

## Descripcion General

Estudio detallado de 10 criptomonedas en el mercado actual, con el fin de obtener el suficiente entendimiento sobre dichos mercado y crear recomendaciones en base a los estudios de los datos obtenidos a traves de la API de Coingecko.

### *Contenido del repositorio:*

* Proceso ETL : el archivo `ETL_process.py` es un script de python donde se hace el proceso completo de ETL, donde con la libreria pycoingecko, se extraen los datos de la API  de coingecko, seguidamente se definen 3 funciones obtienen los datos de `price`(precio), `market_caps`(capitales de mercado) y `volumens`(volumenes de compra) de la criptomoneda que escojamos, la criptomoneda que se desea extraer los datos se selecciona en la variable `moneda`, definiendo tambien en `divisa` el cambio referencial a la criptomoneda seleccionada y en la variable `dias` se selecciona el intervalo de dias de los datos que se quiere extraer.

* EDAs (Exploratory Data Analysis): En la carpeta `EDAs` se puede encontrar el analisis exploratorio que
se realizo a los datos obtenidos en el proceso de ETL, basicamente el esquema de analisis exploratorio consiste en la busqueda de valores faltantes, valores duplicados, outliers y ver que relaciones hay entre las variables. Dicho esquema se aplico para cada una de las criptos (10 en total), dentro de la carpeta `EDAs` podemos encontrar los 10 notebooks con el analisis de cada criptomoneda.

## Criptomonedas seleccionadas
* Binancecoin
* Bitcoin
* Ethereum
* Litecoin
* Polkadot
* Quant
* Chainlink
* XRP
* Solana
* Tether Gold

## Reporte de Analisis.

Durante el analisis de los datos realizados durante el proceso de EDA y la elaboracion de los dashboards se obtuvieron conociemientos particulares de cada criptomoneda estudiada, pero tambien algunos patrones o tendencias que siguen las criptomodenas en general.
Algunas son:

* Alta volatilidad del precio.
* Los precios esta altamente correlacionados con los capitales del mercado.
* La cantidad de tokens en circulacion pueden afectar el capital de mercado, por ende el precio de la criptomoneda.

Ademas se plantearon 3 KPIs (medidor clave de desempeño) para poder tener un buen seguimiento de una criptomoneda y poder tener mas confiaza y seguridad en caso de querer realizar una inversion. Estos son:

1. Crecimiento porcentual: El crecimiento porcentual 
es un indicador clave para medir la variacion en el
precio de una criptomoneda a lo largo de un periodo
especifico. Se calcula como la diferencia entre el 
precio actual y el precio anterior dividido entre el
precio anterior, y se multiplica por 100 para 
expresarlo como porcentaje. Esto dara una idea
de cuanto ha aumentado o disminuido el precio
en relacion a su valor anterior.

FORMULA: ((precio actual - precio anterior)/ precio anterior) * 100

2.  relacion tokens en circulacion-capital(RTCC): Esta
relacion compara la cantidad de tokens en circulacion
con la capitalizacion del mercado. Un RTCC alto
sugiere que el valor de cada token en circulacion
es alto en comparacion con la capitalizacion del
mercado(precios altos), mientras un valor bajo indica
lo contrario(precios bajos).

FORMULA: RTCC = tokens_circulacion / capital_mercado

3. Volatilidad: La volatilidad mide la variabilidad
de los precios de una criptomoneda en un periodo de tiempo determinado.
Una mayor volatilidad indica fluctuaciones mas 
significativas en los precios, lo que puede ser
tanto como una oportunidad o un riesgo.

FORMULA: Desviacion estandar del precio



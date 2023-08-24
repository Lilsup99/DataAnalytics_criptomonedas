<h1 align='center'>
  PROYECTO INDIVIDUAL Nº2 

 <b> Data Analytics: Criptocurrencies</b>   
 Daniel Viema DTPT02
</h1>

## Descripcion General

Estudio detallado de 10 criptomonedas en el mercado actual, con el fin de obtener el suficiente entendimiento sobre dichos mercado y crear recomendaciones en base a los estudios de los datos obtenidos a traves de la API de Coingecko

### *Contenido del repositorio:*

* Proceso ETL : el archivo `ETL_process.py` es un script de python donde se hace el proceso completo de ETL, donde con la libreria pycoingecko, se extraen los datos de la API  de coingecko, seguidamente se definen 3 funciones obtienen los datos de `price`(precio), `market_caps`(capitales de mercado) y `volumens`(volumenes de compra) de la criptomoneda que escojamos, la criptomoneda que se desea extraer los datos se selecciona en la variable `moneda`, definiendo tambien en `divisa` el cambio referencial a la criptomoneda seleccionada y en la variable `dias` se selecciona el intervalo de dias de los datos que se quiere extraer. 
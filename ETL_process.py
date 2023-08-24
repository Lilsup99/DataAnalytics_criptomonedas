from pycoingecko import CoinGeckoAPI
import pandas as pd

client = CoinGeckoAPI()

'''
Se definen 3 funciones para extraer la data de coingecko 
y ademas se transforma el valor de time que esta en unix
a datetime. una funcion para cada feature: prices, market_caps,
total_volumens
'''

def marketprices(id, fiat, days):
  data = client.get_coin_market_chart_by_id(id=id, vs_currency=fiat,days=days)["prices"]
  data = pd.DataFrame(data, columns=["time","price"])
  data["time"] = pd.to_datetime(data["time"], unit = "ms")
  return data

def marketcaps(id, fiat, days):
  data = client.get_coin_market_chart_by_id(id=id, vs_currency=fiat,days=days)["market_caps"]
  data = pd.DataFrame(data, columns=["time","market_caps"])
  data["time"] = pd.to_datetime(data["time"], unit = "ms")
  return data

def volumen(id, fiat, days):
  data = client.get_coin_market_chart_by_id(id=id, vs_currency=fiat,days=days)["total_volumes"]
  data = pd.DataFrame(data, columns=["time","total_volumes"])
  data["time"] = pd.to_datetime(data["time"], unit = "ms")
  return data

#configuracion de datos

moneda = 'quant-network'
divisa = 'usd'
dias = '1825'

# generacion de los dataframes

df_prices = marketprices(moneda, divisa, dias)
df_caps = marketcaps(moneda, divisa, dias)
df_volumens = volumen(moneda, divisa, dias)

#uno los dataframes en uno solo

data = pd.merge(df_prices, df_caps, on='time')
data = pd.merge(data, df_volumens, on='time')

#Obtengo otra variable: Circulating supply

data['Circulating supply'] = data['market_caps'] / data['price']

#guardo los datos

data.to_csv(f'registros_{moneda}.csv')
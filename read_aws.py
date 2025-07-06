import pandas as pd

url = "url de teste do storage aqui"

df = pd.read_parquet(url)
print(df.head(5))

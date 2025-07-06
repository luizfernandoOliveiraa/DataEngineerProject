import requests
from contracts.schema import TransactionSchema
from typing import List
import pandas as pd
from io import BytesIO
import pyarrow.parquet as pq
import datetime


class APICollector:
    def __init__(self, schema, aws):
        self._aws = aws
        self._schema = schema
        self._buffer = None
        return
    
    def start(self, param,url):
        response = self.get_data(param,url)
        response = self.extract_data(response)
        response = self.transform_data(response)
        response = self.convertToParquet(response)
        
        if self._buffer is not None:
            file_name = self.fileName()
            print(file_name)
            self._aws.upload_file(response, file_name)
            return True
                
        return False
    
    def get_data(self, param,url):
        get_data = f"{url}/{param}" if param > 1 else url
        res = requests.get(get_data)

        try:
            data = res.json()
        except Exception as e:
            raise RuntimeError(f"Erro ao fazer parse do JSON: {e} - Conteúdo bruto: {res.text}")

        if res.status_code != 200:
            raise RuntimeError(f"Erro na API: {res.status_code} - {data}")
        
        return data
    
    def extract_data(self, response):
        result: List[TransactionSchema] = []  # type: ignore
        for item in response:
            validated_item = {}
            for key, expected_type in self._schema.items():
                raw_value = item.get(key)
                if raw_value is None:
                    validated_item[key] = None
                    continue
                
                try:
                    validated_item[key] = expected_type(raw_value)
                except (ValueError, TypeError):
                    validated_item[key] = None
            result.append(validated_item)
        return result
    
    def transform_data(self, response):
        result = pd.DataFrame(response)
        return result 
    
    def convertToParquet(self, response):
        self._buffer = BytesIO()
        try:
            response.to_parquet(self._buffer, index=False)            
            return self._buffer

        except Exception as e:
            self._buffer = None  # agora isso será executado antes de lançar a exceção
            raise RuntimeError(f"Erro ao converter para Parquet: {e}") 
            
            
    def fileName(self):
        data_atual = datetime.datetime.now().isoformat()
        match = data_atual.split(".")
        return f"api/api-response-compra{match[0]}.parquet"
        
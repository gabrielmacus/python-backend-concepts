from abc import abstractmethod
from abc import ABC
from ..base.model import BaseModel
from typing import List
import datetime

class BaseServices(ABC):

    def row_to_sql(self, item:dict):
        sql = ""
        for key in item:
            sql+=f"{key}={item[key]},"
        return sql.rstrip(",")
    
    @abstractmethod
    def item_to_row(self,item:BaseModel) -> dict:
        data = {}
        if item.created_at is not None:
            data['created_at'] = "'"+item.created_at.strftime("%Y-%m-%d %H:%M:%S")+"'"
        if item.updated_at is not None:
            data['updated_at'] = "'"+item.updated_at.strftime("%Y-%m-%d %H:%M:%S")+"'"
        return data
        
    @abstractmethod
    def row_to_item(self,row:dict) -> BaseModel:
        item = BaseModel()
        item.id = row['id']
        item.created_at = row['created_at']
        item.updated_at = row['updated_at']

        return item
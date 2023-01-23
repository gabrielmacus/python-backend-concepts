from .model import BaseModel
from .services import BaseServices
from ..db.services import DBServices
from typing import List
import datetime
from abc import abstractmethod
from abc import ABC

class BaseRepository(ABC):
    _module_services:BaseServices = None
    _db_services:DBServices = None
    _table_name:str = None
    

    def __init__(self, db_services:DBServices, module_services:BaseServices) -> None:
        self._db_services = db_services
        self._module_services = module_services

    def create(self,item:BaseModel) -> int:
        """Inserts model instance into db

        Args:
            item (BaseModel): Model instance

        Returns:
            int: Created items
        """
        item.created_at = datetime.datetime.now()
        row = self._module_services.item_to_row(item)
        sql = self._module_services.row_to_sql(row)
        return self._db_services.execute_db(f"INSERT INTO {self._table_name} SET {sql}")
        
    def read(self) -> List[BaseModel]:
        """Reads items from db

        Returns:
            List[BaseModel]: Item list
        """
        items:List[BaseModel] = []
        rows = self._db_services.query_db(f"SELECT * FROM {self._table_name}")
        for row in rows:
            items.append(self._module_services.row_to_item(row))
        return items

    def update(self, id:int, item:BaseModel) -> int:
        """Updates item from database

        Args:
            id (int): Id of the item to be updated
            item (BaseModel): BaseModel instance

        Returns:
            int: Updated rows. Should be 1
        """
        item.updated_at = datetime.datetime.now()
        row = self._module_services.item_to_row(item)
        sql = self._module_services.row_to_sql(row)
        return self._db_services.execute_db(f"UPDATE {self._table_name} SET {sql} WHERE id = {id}")

    def delete(self,id:int):
        self._db_services.execute_db(f"DELETE FROM {self._table_name} WHERE id = {id}")
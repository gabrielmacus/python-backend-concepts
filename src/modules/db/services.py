from typing import List
import pymysql


class DBServices:
    def connect_db(self) -> pymysql.Connection:
        """Establishes connection with mysql db

        Returns:
            pymysql.Connection: DB connection object
        """
        return pymysql.connect(
            host='localhost',
            port=8306,
            user='root',
            password='123456',
            database='python-backend-concepts',
            cursorclass=pymysql.cursors.DictCursor
        )

    def execute_db(self, sql:str) -> int:
        """Executes a write operation in db

        Args:
            sql (str): SQL query

        Returns:
            int: Number of affected rows
        """
        connection = self.connect_db()
        with connection.cursor() as cursor:
            cursor.execute(sql)
        connection.commit()
        return connection.affected_rows()

    def query_db(self, sql:str) -> List[dict]:
        """Executes a read operation in db

        Args:
            sql (str): SQL query

        Returns:
            List[dict]: Array of fetched rows
        """
        connection = self.connect_db()
        with connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
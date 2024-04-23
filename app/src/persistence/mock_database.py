from app.src.persistence.base_database import BaseDatabase


class MockDatabase(BaseDatabase):
    def __init__(self):
        self.tables = {}

    def add_table(self, table):
        self.tables.update(table)

    def get_tables(self):
        return self.tables

    def get_table(self, table_name):
        return self.tables.get(table_name, {})

    def is_empty(self):
        return self.tables == {}

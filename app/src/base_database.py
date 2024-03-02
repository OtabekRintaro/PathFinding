import abc


class BaseDatabase:
    @abc.abstractmethod
    def add_table(self, table):
        pass

    @abc.abstractmethod
    def get_tables(self):
        pass

    @abc.abstractmethod
    def get_table(self, table_name):
        pass

    @abc.abstractmethod
    def is_empty(self):
        pass

import abc


class BaseIDGenerator:

    @staticmethod
    @abc.abstractmethod
    def generate_id():
        pass

    @staticmethod
    @abc.abstractmethod
    def remove_id(id):
        pass

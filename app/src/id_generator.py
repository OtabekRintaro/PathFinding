import abc

class BaseIDGenerator():

    @abc.abstractstaticmethod
    def generate_id():
        pass

    @abc.abstractstaticmethod
    def remove_id(id):
        pass
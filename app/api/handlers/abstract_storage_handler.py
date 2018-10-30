import abc
class AbstractStorageHandler(abc.ABC):
    
    def __init__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def retrieve_users(self,user_id:int=None):
        pass

    @abc.abstractmethod
    def write(self):
        pass

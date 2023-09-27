class Singleton(type):
  _instances = {}
  def __call__(cls, *args, **kwargs):
      if cls not in cls._instances:
          instance = super().__call__(*args, **kwargs)
          cls._instances[cls] = instance
      return cls._instances[cls]
  
class DB_names(metaclass=Singleton):
    def __init__(self,):
        self._name = 0
        self._name_table = 0

    def get_name(self, ):
        return self._name
    
    def set_name(self, name):
        self._name = name
        return name
    
    def get_name_table(self, ):
        return self._name_table
    
    def set_name_table(self, name):
        self._name_table = name
        return name
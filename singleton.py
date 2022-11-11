class SingletonMeta(type):
    
    """
    La clase de singleton puede ser implementada de diferentes maneras en Python. Algunos
    métodos posibles clases base.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Posibles cambios del valor del argumento '__init__'
        no afectan la instancia devuelta
        
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finalmente, cualquier singleton debe definir algo
        de lógica empresarial
        """

        # ...


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton funciona, ambas variables contienen la misma instancia.")
    else:
        print("Singleton no funciono, las variables contienen diferentes instancias.")
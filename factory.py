from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    

    @abstractmethod
    def factory_method(self):
        
        pass

    def some_operation(self) -> str:
        
        product = self.factory_method()

        result = f"Creator: El mismo codigo creador realizado con{product.operation()}"

        return result


class ConcreteCreator1(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Resultado de ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Resultado de ConcreteProduct2}"


def client_code(creator: Creator) -> None:


    print(f"No conozco la clase creadora, pero aún funciono\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: iniciada con el concreteCreator1")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: iniciada con el ConcreteCreator2")
    client_code(ConcreteCreator2())
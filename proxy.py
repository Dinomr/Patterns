from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):

    def request(self) -> None:
        print("RealSubject: Manejando solicitud.")


class Proxy(Subject):

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Revisando acceso prioritario para realizar la solicitud.")
        return True

    def log_access(self) -> None:
        print("Proxy: Registro de la hora de solicitud del login.", end="")


def client_code(subject: Subject) -> None:

    subject.request()


if __name__ == "__main__":
    print("Client: Ejecutando el codigo cliente con un sujeto real:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Ejecutando el mismo codigo con un proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)
from typing import Protocol

class Walker(Protocol):
    def walk(self, destination: str)-> None:
        ...

    def run(self, destination:str) -> None:
        ...

class Swimmer(Protocol):

    def dive(self, depth: float) -> None:
        ...
    def swim(self, destination:str) -> None:
        ...

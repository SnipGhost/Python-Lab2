from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, name):
        self.name = name

    def name(self):
        return self.name

    @abstractmethod
    def area(self):
        pass

from abc import ABC, abstractmethod

from lib.context import Context

class Middleware(ABC):
    @abstractmethod
    def run(self, context: Context):
        pass
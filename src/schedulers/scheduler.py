from abc import ABC, abstractmethod

"""
    Interface for all other scheduling algorithms
"""
class Scheduler(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def choose_process(self):
        pass

    @abstractmethod
    def add_to_queue(self, process):
        pass

    @abstractmethod
    def get_name(self):
        pass
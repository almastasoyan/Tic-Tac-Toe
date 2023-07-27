from abc import abstractmethod
from Board import Board_Class



class Players:
    def __init__(self, valeu: str, board: Board_Class):
        self.valeu = valeu
        self.board = board

    @abstractmethod
    def move(self):
        pass







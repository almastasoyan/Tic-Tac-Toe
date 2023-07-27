from Players_Class import Players
import random



class Computer_Player(Players):
    def move(self):

        number = random.choice(self.board.get_free_slots())
        print()
        self.board.change_board(number, self.valeu)

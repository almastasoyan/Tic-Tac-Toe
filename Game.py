from Board import Board_Class
from Human_Player_Class import Human_Player
from Comp_Player import Computer_Player
from Players_Class import Players



class Game:
    def __init__(self):
        self.board = Board_Class()
        self.human = Human_Player('x', self.board)
        self.comuter = Computer_Player('o', self.board)


    def play(self):
        while True:
            self.human.move()
            self.board.print_board()
            if self.check_status(self.human):
                break
            self.comuter.move()
            self.board.print_board()
            if self.check_status(self.comuter):
                break
                
                

    def check_status(self, player: Players):
        board.state = self.board.board_sate
        for i in range(3):
            if  board.state[i * 3:(i + 1) * 3] == [player.valeu]*3:
                print(player.valeu, 'wins')
                return True
            

            if [board.state[i], board.state[i + 3], board.state[i + 6]] == [player.valeu] * 3:
                print(player.valeu, 'wins')
                return True
            

            if [board.state[0], board.state[4], board.state[8]] == [player.valeu]*3:
                print(player.valeu, 'wins')
                return True
            
            if [board.state[2], board.state[4], board.state[6]] == [player.valeu]*3:
                print(player.valeu, 'wins')
                return True
            
            if len(self.board.get_free_slots()) == 0:
                print ('Draw')
                return True
            return False
            




if __name__ == "__main__":
    board = Board_Class()
    game = Game()
    game.play()
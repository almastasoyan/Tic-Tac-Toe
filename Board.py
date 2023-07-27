class Board_Class:
    def __init__(self):
        self.board_sate = ['*', '*', '*', '*', '*', '*', '*', '*', '*']


    def change_board(self, number: int, string:str):

        '''fiksiruen izmineniya na doske
        
            number = koordinati
            string = x or o
        '''
        self.board_sate[number-1]= string


    def print_board(self):
        for row in range(3):
            for colum in range(3):
                print(self.board_sate[row * 3 + colum], end=' ')

            print()


    def get_free_slots(self):
        free_slots = []
        for index, valeu in enumerate(self.board_sate):
            if valeu == '*':
                free_slots.append(index +1)

        return free_slots


        





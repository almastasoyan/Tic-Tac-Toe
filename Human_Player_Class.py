from Players_Class import Players



class Human_Player(Players):
    def move(self):
        while True:
            number = input('Choose board coors from 1-9: ')
            if number.isdigit():
                number = int(number)
            else:
                print('Type integer from 1-9')
                continue
            
            if number not in list(range(1, 10)):
                print("integer should be from 1 to 9 range")
                continue

            if number not in self.board.get_free_slots():
                print("choose slot is not available")
                continue

            break


        print()
        self.board.change_board(number, self.valeu)





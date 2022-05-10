class CodeCS20:
    def __init__(self, message=''):
        self.__message = message
        self.__checker = True
        self.add_first_list()
        self.change_index(1)

    def change_index(self, index=1):
        if self.__checker:
            if index < 6 and index > 0:
                self.__index = index
                if self.__index == 1:
                    self.__second_list = ['(', 'Y', 'o', '7', 'E', ',', 'Z', 'M', '[', 'C', 'O', 'D', 'F', 'S', '5',
                                          ')', 'u', 'Q', '_', '}', 'L', 'X', 'h', 'B', '.', 'l', 'j', '0', 'd', 'k',
                                          '=', 't', 'N', 'f', 'R', 'J' 'I', 'A', 'T', ']', '+', 'q', 'z', 'y', 'm', 'w',
                                          'U', 'a', 'V', 'K', '8', 'b', '9', '%', 'v', '1', ';', 'x', 'e', 'W', '{',
                                          'g', 'i', '?', '!', '*', 'n', 'H', 's', 'r', '2', 'p', '6', 'P', '3', ':',
                                          '4', 'c', '-', 'G']
                if self.__index == 2:
                    self.__second_list = ['m', 'h', 'b', '!', 'S', '=', 'g', '(', 's', 'X', ',', 'z', 'D', 'u', 'R',
                                          'J', '+', '8', '[', '0', 'T', '*', '5', 'F', 'j', 'K', 'E', '%', 'x', 'H',
                                          '?', '-', 'G', 'r', '.', 'I', '3', ')', ']', '4', 'M', '1', 'i', '_', 'v',
                                          'W', 'C', 'A', '6', 'f', 'B', 'p', 'a', 'P', '9', 'Q', 'n', 'e', ':', '7',
                                          'y', '{', ';', 'N', '}', 'c', 'O', 'V', '2', 'k', 'U', 'o', 'Y', 'w', 'l',
                                          'd', 'L', 'q', 't', 'Z']
                if self.__index == 3:
                    self.__second_list = ['R', 'L', 'U', ')', '(', 'A', 'B', ';', '}', 'w', 'S', 'h', '5', 'f', '[',
                                          'y', 'P', 'g', 'o', 'e', ':', ',', 'W', 'O', '6', 'k', 'T', 'j', 'i', '1',
                                          '?', '8', '!', 't', '4', '2', 'N', '*', 'p', 'D', '0', 'Y', 'r', '9', 'I',
                                          '{', 's', 'l', '3', 'E', 'M', 'Z', 'Q', 'J', 'F', 'b', 'v', '-', '.', 'm',
                                          'X', '+', 'd', 'n', 'H', 'c', '7', 'C', '=', 'a', 'q', 'x', ']', 'G', 'K',
                                          'V', '_', 'u', 'z', '%']
                if self.__index == 4:
                    self.__second_list = ['L', 'a', 'X', '%', 'u', 'F', 'B', 'y', 'W', 'I', '5', 'c', '{', '1', '9',
                                          'b', 'w', 'g', 'x', 'J', 'r', 'A', 'N', '6', '2', 'Q', 'S', '3', 'H', 'V',
                                          'n', '-', ';', '(', '}', 'Y', '4', 'k', 'T', '=', '0', 'Z', 'm', 'E', '!',
                                          'v', 'f', '?', 'o', 's', 'l', 'e', 'j', 'p', 'q', ')', 'G', 'U', 'z', ']',
                                          ',', 'M', '.', '7', 'i', 'R', '[', 'h', '_', 'd', 't', 'O', 'K', 'C', 'D',
                                          'P', ':', '*', '+', '8']
                if self.__index == 5:
                    self.__second_list = ['H', '+', 'M', 's', '9', 'V', 'Z', 'J', 'w', 'j', '*', 'm', 'B', ']', 'F',
                                          'f', '0', 'u', 'g', 'b', 'W', 'K', ',', 'S', 'N', 'c', 'Y', 'v', '.', '5',
                                          'e', ';', 'L', ')', 'A', 'z', '}', '{', '!', '[', 'i', 'd', '?', '6', 'a',
                                          'U', '4', '8', ':', 'G', 'C', 'D', '3', '-', 'E', 'n', '(', '_', 'o', 'h',
                                          'X', '7', '%', 'Q', 'q', 'y', 'T', 'k', 'R', 'p', '=', 'r', 'l', 'x', 'I',
                                          '2', 'O', 't', 'P', '1']
            else:
                print("Wrong index. Index can be in [1, 5].")
        else:
            print("You can't change index because message encoded")

    def add_first_list(self):
        letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
                   'x', 'c', 'v', 'b', 'n', 'm']
        letters += [x.upper() for x in letters]
        letters += ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '!', '?', '{', '}', '[', ']', '(', ')',
                    '-', '_', '%', ':', ';', '=', '+', '*']
        self.__first_list = letters

    def decode(self):
        if not self.__checker:
            self.__checker = not self.__checker
            new_message = ''
            for rec in self.__message:
                try:
                    l = self.__second_list.index(rec)
                except:
                    new_message += rec
                else:
                    new_message += self.__first_list[l]
            self.__message = new_message
        else:
            print("Your message not encoded")

    def encode(self):
        if self.__checker:
            self.__checker = not self.__checker
            new_message = ''
            for rec in self.__message:
                try:
                    l = self.__first_list.index(rec)
                except:
                    new_message += rec
                else:
                    new_message += self.__second_list[l]
            self.__message = new_message
        else:
            print("Your message encoded")

    def get_message(self):
        print(self.__message)

    def set_message(self, message=False):
        if self.__checker:
            if message:
                self.__message = message
        else:
            print("You can't change message because message encoded")

    def __str__(self):
        if self.__checker:
            return f"{self.__message} index:{self.__index}, not encoded"
        else:
            return f"{self.__message} index:{self.__index}, encoded"


class CodeCS20:
  def __init__(self, message=''):
    self.__first_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x' ,'c' ,'v' ,'b' ,'n' ,'m']
    self.__message = message
    self.__checker = True
    self.change_index(1)

  def change_index(self, index=1):
    if self.__checker:
      if index < 6 and index > 0:
        self.__index = index
        match self.__index:
          case 1:
            self.__second_list = ['v', 't', 'w', 'n', 'q', 'u', 'g', 'i', 's', 'p', 'k', 'c', 'd', 'r', 'l', 'a', 'o', 'e', 'b', 'x', 'h', 'j', 'y', 'f', 'm', 'z']
          case 2:
            self.__second_list = ['h', 'x', 'p', 'c', 's', 'm', 'u', 'w', 'y', 'i', 'l', 'k', 'q', 'a', 'd', 'e', 't', 'v', 'f', 'n', 'g', 'o', 'j', 'r', 'z', 'b']
          case 3:
            self.__second_list = ['f', 'z', 'o', 's', 'w', 'v', 'a', 'u', 'g', 'b', 'n', 'x', 'c', 'j', 'p', 'd', 'e', 'l', 'm', 'i', 'y', 'q', 'h', 't', 'r', 'k']
          case 4:
            self.__second_list = ['c', 'k', 'p', 's', 'z', 't', 'm', 'o', 'x', 'l', 'd', 'a', 'y', 'r', 'q', 'v', 'g', 'f', 'e', 'w', 'u', 'b', 'h', 'j', 'n', 'i']
          case 5:
            self.__second_list = ['m', 't', 'i', 'w', 'q', 'g', 'v', 'r', 'j', 'o', 'd', 'f', 'b', 'u', 'e', 'k', 'x', 'n', 'h', 'l', 'y', 'p', 'z', 's', 'c', 'a']
      else:
        print("Wrong index. Index can be in [1, 5].")
    else:
      print("You can't change index because message encoded")

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

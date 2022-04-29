
class CodeCS20():
  def __init__(self, message='', index=1):
    self.first_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x' ,'c' ,'v' ,'b' ,'n' ,'m']
    self.index = index
    match index:
        case 1:
          self.second_list = ['v', 't', 'w', 'n', 'q', 'u', 'g', 'i', 's', 'p', 'k', 'c', 'd', 'r', 'l', 'a', 'o', 'e', 'b', 'x', 'h', 'j', 'y', 'f', 'm', 'z']
        case 2:
          self.second_list = ['h', 'x', 'p', 'c', 's', 'm', 'u', 'w', 'y', 'i', 'l', 'k', 'q', 'a', 'd', 'e', 't', 'v', 'f', 'n', 'g', 'o', 'j', 'r', 'z', 'b']
        case 3:
          self.second_list = ['f', 'z', 'o', 's', 'w', 'v', 'a', 'u', 'g', 'b', 'n', 'x', 'c', 'j', 'p', 'd', 'e', 'l', 'm', 'i', 'y', 'q', 'h', 't', 'r', 'k']
        case 4:
          self.second_list = ['c', 'k', 'p', 's', 'z', 't', 'm', 'o', 'x', 'l', 'd', 'a', 'y', 'r', 'q', 'v', 'g', 'f', 'e', 'w', 'u', 'b', 'h', 'j', 'n', 'i']
        case 5:
          self.second_list = ['m', 't', 'i', 'w', 'q', 'g', 'v', 'r', 'j', 'o', 'd', 'f', 'b', 'u', 'e', 'k', 'x', 'n', 'h', 'l', 'y', 'p', 'z', 's', 'c', 'a']
    self.message = message
    self.checker = True

  def decode(self):
    if not self.checker:
      self.checker = not self.checker
      new_message = ''
      for rec in self.message:
        try:
          l = self.second_list.index(rec)
        except:
          new_message += rec
        else:
          new_message += self.first_list[l]
      self.message = new_message
    else:
        print("Your message not encoded")

  def encode(self):
    if self.index < 6 and self.index > 0:
      if self.checker:
        self.checker = not self.checker
        new_message = ''
        for rec in self.message:
          try:
            l = self.first_list.index(rec)
          except:
            new_message += rec
          else:
            new_message += self.second_list[l]
        self.message = new_message
      else:
        print("Your message encoded")
    else:
      print("Wrong index. If you want to change index use function change_index()")


a = CodeCS20('hello my name12323', 4)
a.encode()
a.encode()
print(a.message)
a.decode()
a.decode()
print(a.message)
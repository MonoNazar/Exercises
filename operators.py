
class Operators:
  def __init__(self, first_number=1, second_number=1):
    self.first_number = first_number
    self.second_number = second_number
    self.result = 0

  def adding(self):
    self.result = self.first_number + self.second_number
    return self.result

  def subtraction(self):
    self.result = self.first_number - self.second_number
    return self.result
    
  def division(self, count=5):
    checker = False
    a, b = self.first_number, self.second_number
    if a < 0:
      a = abs(a)
      checker = True
    if b < 0:
      b = abs(b)
      checker = not checker
    if b == 0:
      self.result = "Ділення на 0"
    else:
      while a >= b:
        a -= b
        self.result += 1
      if a != 0:
        n = ''
        for x in range(count + 1):
          rec = 0
          a *= 10
          while a >= b:
            a -= b
            rec += 1
          n += str(rec)
        else:
          b = int(n[-1:])
          n = n[:-1]
          if b > 5:
            n = str(int(n) + 1)
        self.result = float(str(self.result) + "." + n)
      if checker:
        self.result = -1 * res
    return self.result

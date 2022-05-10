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
            a = self.adsol(a)
            checker = True
        if b < 0:
            b = self.adsol(b)
            checker = not checker
        self.result = 0
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
                self.result = -1 * self.result
        return self.result

    def adsol(self, number=False):
        if not number:
            number = self.first_number
        number = str(number)
        if number[0] == "-":
            number = number[1:]
        self.result = float(number)
        return self.result

    # def multi(self, count=5):
    #     a, b = self.first_number, self.second_number
    #     if a % 1 == 0:
    #         for rec in range(1, a+1):
    #             self.result += b
    #     else:
    #         for rec in range(1, int(a)+1):
    #             self.result += b
    #         a = str(a)
    #         l_1, l_2 = a.split(".")
    #
    #         iter_list = [0]
    #         iter_list += [x for x in l_2]
    #
    #         if count > len(iter_list) - 1:
    #             count = len(iter_list) - 1
    #         print(count)
    #         for x in range(1, count+1):
    #             for rec in range(1, int(iter_list[x])+1):
    #                 self.result += b / (10 ** x)
    #                 print(self.result)
    #     return self.result
    #
    # def power(self, count=2):
    #     number = 5
    #     res = 0
    #     for x in number:
    #         res += number



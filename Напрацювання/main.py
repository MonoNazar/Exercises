a = -22
b = -7
res = 0
checker = False
if a < 0:
  a = abs(a)
  checker = True
if b < 0:
  b = abs(b)
  checker = not checker
if b == 0:
  res = "Ділення на 0"
else:
  while a >= b:
    a -= b
    res += 1
  if a != 0:
    n = ''
    for x in range(10):
      rec = 0
      a *= 10
      while a >= b:
        a -= b
        rec += 1
      n += str(rec)
    res = float(str(res) + "." + n)
  if checker:
    res = -1 * res
print(res)
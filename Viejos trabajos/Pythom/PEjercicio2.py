a = 1
b = 0
c = 2
d = (a == b) or (not (c > a) and (b == 0))
e = (not (a != c) or (b < c)) and (not (d or (c == 2)))
print(e)
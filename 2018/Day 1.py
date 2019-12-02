import re
res = 0
a = "e"

while a != '':
    if a[0] == '-':
        res -= int(re.sub('-','',a))
    if a[0] == '+':
        res += int(a)
    a = input()
print(res)
#OpCodes
from time import sleep
import random
a = input()
ops = a.split(',')

print('\n\nStats:')
print('# of elements: {}'.format(len(ops)))

count = 0
for i in ops:
    if i == '99':
        print('Halt op is in element {}'.format(count))
    count += 1
    print('Scanning... [{}]        '.format(i),end='\r')
    sleep(random.randint(1,10)/100)
print('Done.                       ')


for i in range(0,len(ops),4):
    if int(ops[i]) == 99:
        break
    elif int(ops[i]) == 1:
        ops[int(ops[i+3])] = int(ops[int(ops[i+1])]) + int(ops[int(ops[i+2])])
    elif int(ops[i]) == 2:
        ops[int(ops[i+3])] = int(ops[int(ops[i+1])]) * int(ops[int(ops[i+2])])
    print('Array:{}'.format(ops),end='\r')
print('\n\n\nGot string: \n{}'.format(ops))
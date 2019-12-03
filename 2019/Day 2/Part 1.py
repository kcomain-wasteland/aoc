#OpCodes
a = input()
ops = a.split(',')

print('\n\nStats:')
print('# of elements: {}'.format(len(ops)))

for i in range(0,len(ops),4):
    if int(ops[i]) == 99:
        break
    elif int(ops[i]) == 1:
        ops[int(ops[i+3])] = int(ops[int(ops[i+1])]) + int(ops[int(ops[i+2])])
    elif int(ops[i]) == 2:
        ops[int(ops[i+3])] = int(ops[int(ops[i+1])]) * int(ops[int(ops[i+2])])
    print('Array:{}'.format(ops),end='\r')
print('\n\n\nGot string: \n{}'.format(ops))
inp = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,10,31,35,2,6,35,39,1,39,13,43,1,43,9,47,2,47,10,51,1,5,51,55,1,55,10,59,2,59,6,63,2,6,63,67,1,5,67,71,2,9,71,75,1,75,6,79,1,6,79,83,2,83,9,87,2,87,13,91,1,10,91,95,1,95,13,99,2,13,99,103,1,103,10,107,2,107,10,111,1,111,9,115,1,115,2,119,1,9,119,0,99,2,0,14,0]

def test(param1):
    ops = param1
    #print('\n\nStats:')
    #print('# of elements: {}'.format(len(ops)))
    for i in range(0,len(ops),4):
        if int(ops[i]) == 99:
            break
        elif int(ops[i]) == 1:
            ops[int(ops[i+3])] = int(ops[int(ops[i+1])]) + int(ops[int(ops[i+2])])
        elif int(ops[i]) == 2:
            ops[int(ops[i+3])] = int(ops[int(ops[i+1])]) * int(ops[int(ops[i+2])])
        #print('Array:{}'.format(ops),end='\r')
    #print('\n\n\nGot string: \n{}'.format(ops))
    return(ops)

count = 0
for noun in range(0,100):
    for verb in range(0,100):
        res = ""
        print(f'Testing #{count}...',end='\r')
        temparr = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,10,31,35,2,6,35,39,1,39,13,43,1,43,9,47,2,47,10,51,1,5,51,55,1,55,10,59,2,59,6,63,2,6,63,67,1,5,67,71,2,9,71,75,1,75,6,79,1,6,79,83,2,83,9,87,2,87,13,91,1,10,91,95,1,95,13,99,2,13,99,103,1,103,10,107,2,107,10,111,1,111,9,115,1,115,2,119,1,9,119,0,99,2,0,14,0]
        temparr[1] = noun
        temparr[2] = verb
        try:
            temp = test(temparr)
        except Exception as err:
            res = f'Error, LO: {temp[0]}'
            pass
        res = temp[0]
        print(f'#{count} Result: N:{noun} V:{verb} O:{res}'.format(noun,verb))
        count += 1
import math

a = 'OwO'

def fuelneed(mass):
    return int(math.floor(int(mass)/3))-2
fuel_counter_upper = 0

temp = input()
while temp != '':
    if temp != '':
        while True:
            a
        fuel_counter_upper += fuelneed(temp)
    temp = input()

print('Total required fuels: '+str(fuel_counter_upper))